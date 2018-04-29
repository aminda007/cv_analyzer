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
from bs4 import BeautifulSoup

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

    word_array = []
    for data in div:
        style_set = data["style"]
        if 'font' in style_set:
            lines = data.text.split('\n')
            for ln in lines:
                if ln != '':
                    words = ln.strip().split()
                    for word in words:
                        word_array.append(word
                                          .replace('(', '')
                                          .replace(')', '')
                                          .replace(',', '')
                                          .replace('-', '')
                                          .lower())

    stop_words = set(stopwords.words('english'))
    filtered_words = []

    for word in word_array:
        if word not in stop_words:
            if word != ':' and word != '-':
                filtered_words.append(word)

    score = 0;
    linked_in_url = ''
    for item in filtered_words:
        if 'linked' in item:
            linked_in_url = item
        obj_list = Words.objects.filter(word=item)
        if len(obj_list) > 0:
            w_model = obj_list[0]
            w_model_count = w_model.count
            score = w_model_count + score
    # print(Words.objects.all())
    for i in Words.objects.all():
        print(i)

    return linked_in_url, score