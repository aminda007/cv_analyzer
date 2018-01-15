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
import organizer
import json

import pdfminer

# Open a PDF file.
# fp = open('cv.pdf', 'rb')
fp = open('Chamod_Samarajeewa__CV.pdf', 'rb')

# Create a PDF parser object associated with the file object.
parser = PDFParser(fp)

# Create a PDF document object that stores the document structure.
# Password for initialization as 2nd parameter
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
outfp = open('cv.html', 'wb')

device = HTMLConverter(rsrcmgr,
                       outfp,
                       codec=codec,
                       scale=scale,
                       layoutmode=layoutmode,
                       laparams=laparams,
                       imagewriter=imagewriter)

# Create a PDF interpreter object.
interpreter = PDFPageInterpreter(rsrcmgr, device)


def parse_obj(lt_objs):
    # loop over the object list
    for obj in lt_objs:

        # if it's a textbox, print text and location
        if isinstance(obj, pdfminer.layout.LTTextBoxHorizontal):
            # print(obj)
            "%6d, %6d, %s" % (obj.bbox[0], obj.bbox[1], obj.get_text().replace('\n', '_'))
            # print(obj)

        # if it's a container, recurse
        elif isinstance(obj, pdfminer.layout.LTFigure):
            parse_obj(obj._objs)


# loop over all pages in the document
for page in PDFPage.create_pages(document):

    # convert the pdf pages into html format
    interpreter.process_page(page)

# outfp.getvalue()
device.close()



organizer.organize()


