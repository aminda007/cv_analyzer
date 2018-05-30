from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator
from pdfminer.converter import HTMLConverter
from pdfminer.image import ImageWriter
from io import StringIO
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from bs4 import BeautifulSoup
import re
from .models import Words


def score_resume(fp):

    # Create a PDF parser object associated with the file object.
    parser = PDFParser(fp)

    # Create a PDF document object that stores the document structure.
    document = PDFDocument(parser)

    # Check if the document allows text extraction. If not, abort.
    if not document.is_extractable:
        raise PDFTextExtractionNotAllowed

    # Create a PDF resource manager object that stores shared resources.
    rsrcmgr = PDFResourceManager()

    # Create a PDF device object.
    device = PDFDevice(rsrcmgr)

    # BEGIN LAYOUT ANALYSIS
    # Set parameters for analysis.
    laparams = LAParams()

    # Create a PDF page aggregator object.
    device = PDFPageAggregator(rsrcmgr, laparams=laparams)

    outfp = StringIO()
    codec = 'utf-8'
    scale = 1
    layoutmode = 'normal'
    imagewriter = ImageWriter('image.jpg')
    outfp = open('cv_analyzer/resume.txt', 'wb')

    # device = TextConverter(rsrcmgr, outfp, imagewriter=imagewriter, codec=codec)
    device = HTMLConverter(rsrcmgr,
                           outfp,
                           codec=codec,
                           scale=scale,
                           layoutmode=layoutmode,
                           laparams=laparams,
                           pagemargin=0,
                           fontscale=1.0,
                           debug=0,
                           imagewriter=imagewriter)

    # Create a PDF interpreter object.
    interpreter = PDFPageInterpreter(rsrcmgr, device)


    # loop over all pages in the document
    for page in PDFPage.create_pages(document):

        # convert the pdf pages into html format
        interpreter.process_page(page)

    device.close()
    outfp.close()

    html = open('cv_analyzer/resume.txt', 'rb', buffering=1).read(1000000)
    soup = BeautifulSoup(html, 'html.parser')
    div = soup.find_all('span', style=True)

    filtered_words = []
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()
    gpa_found = False
    c_found = False
    gpa = ''
    linked_in_url = ''
    for data in div:
        style_set = data["style"]
        if 'font' in style_set:
            lines = data.text.split('\n')
            for ln in lines:
                if ln != '':
                    #  replace unwanted characters
                    ln = ln.replace('(', ' ').replace(')', ' ').replace(',', ' ')
                    words = ln.strip().split()
                    for word in words:
                        # extract linkedin url
                        if 'linked' in word:
                            linked_in_url = word
                        word = word.replace('-', '')
                        word = re.sub(r'(?<!\d)\.(?!\d)', '', word)  # remove pull stops
                        #  the only word with one letter is C
                        if not c_found:
                            if word == 'C':
                                filtered_words.append('c')
                                c_found = True
                        word = word.lower()  # convert to lower case
                        if word not in stop_words:
                            # check for numbers and minimum word length is 2
                            if len(word) > 1 and not bool(re.search(r'\d', word)):
                                # extract gpa
                                if word == 'gpa':
                                    gpa_found = True
                                filtered_words.append(lemmatizer.lemmatize(word, pos="n"))
                            else:
                                if gpa_found and not bool(re.search('[a-zA-Z]', word)) and len(word) > 2:
                                    gpa = word
                                    gpa_found = False
    print('gpa is ' + gpa)
    # print('linkedin url is ' + linked_in_url)

    score = 0;
    for item in filtered_words:
        # print(item)
        obj_list = Words.objects.filter(word=item)
        if len(obj_list) > 0:
            w_model = obj_list[0]
            w_model_count = w_model.count
            score = w_model_count + score
    # print(Words.objects.all())

    if gpa == '':
        gpa = 2.0

    print('model score is ' + str(score))
    return linked_in_url, score, float(gpa)