import os
import comtypes.client
from pdf2image import convert_from_path, convert_from_bytes
from PIL import Image, ImageFont, ImageDraw

mimes = ['msword','msword','vnd.openxmlformats-officedocument.wordprocessingml.document','vnd.openxmlformats-officedocument.wordprocessingml.template','vnd.ms-word.document.macroEnabled.12','vnd.ms-word.template.macroEnabled.12','vnd.ms-excel','vnd.ms-excel','vnd.ms-excel','vnd.openxmlformats-officedocument.spreadsheetml.sheet','vnd.openxmlformats-officedocument.spreadsheetml.template','vnd.ms-excel.sheet.macroEnabled.12','vnd.ms-excel.template.macroEnabled.12','vnd.ms-excel.addin.macroEnabled.12','vnd.ms-excel.sheet.binary.macroEnabled.12','vnd.ms-powerpoint','vnd.ms-powerpoint','vnd.ms-powerpoint','vnd.ms-powerpoint','vnd.openxmlformats-officedocument.presentationml.presentation','vnd.openxmlformats-officedocument.presentationml.template','vnd.openxmlformats-officedocument.presentationml.slideshow','vnd.ms-powerpoint.addin.macroEnabled.12','vnd.ms-powerpoint.presentation.macroEnabled.12','vnd.ms-powerpoint.template.macroEnabled.12','vnd.ms-powerpoint.slideshow.macroEnabled.12','vnd.ms-access']
word_mime = ['msword','msword','vnd.openxmlformats-officedocument.wordprocessingml.document','vnd.openxmlformats-officedocument.wordprocessingml.template','vnd.ms-word.document.macroEnabled.12','vnd.ms-word.template.macroEnabled.12']
exel_mime = ['vnd.ms-excel','vnd.ms-excel','vnd.ms-excel','vnd.openxmlformats-officedocument.spreadsheetml.sheet','vnd.openxmlformats-officedocument.spreadsheetml.template','vnd.ms-excel.sheet.macroEnabled.12','vnd.ms-excel.template.macroEnabled.12','vnd.ms-excel.addin.macroEnabled.12','vnd.ms-excel.sheet.binary.macroEnabled.12']
ppt_mimes = ['vnd.ms-powerpoint','vnd.ms-powerpoint','vnd.ms-powerpoint','vnd.ms-powerpoint','vnd.openxmlformats-officedocument.presentationml.presentation','vnd.openxmlformats-officedocument.presentationml.template','vnd.openxmlformats-officedocument.presentationml.slideshow','vnd.ms-powerpoint.addin.macroEnabled.12','vnd.ms-powerpoint.presentation.macroEnabled.12','vnd.ms-powerpoint.template.macroEnabled.12','vnd.ms-powerpoint.slideshow.macroEnabled.12']
ext = ['doc','dot','docx','dotx','docm','dotm','xls','xlt','xla','xlsx','xltx','xlsm','xltm','xlam','xlsb','ppt','pot','pps','ppa','pptx','potx','ppsx','ppam','pptm','potm','ppsm']

def off_pdf_thum(django_mime_type,in_file,out_file):
    try:
        for mime in word_mime:
            if mime == django_mime_type:
                return doctopdf(in_file,out_file)
        for mime in exel_mime:
            if mime == django_mime_type:
                return exlstopdf(in_file,out_file)
        for mime in ppt_mimes:
            if mime == django_mime_type:
                return ppttopdf(in_file,out_file)
    except:
        pass
        
def exlstopdf(inputFileName, outputFileName):
    import pythoncom
    pythoncom.CoInitialize()
    app = comtypes.client.CreateObject('Excel.Application')
    app.Visible = False
    doc = app.Workbooks.Open(inputFileName) 
    doc.ExportAsFixedFormat(0, outputFileName, 1, 0)
    doc.Close()
    app.Quit()

def doctopdf(inputFileName, outputFileName):
    import pythoncom
    pythoncom.CoInitialize()
    wdFormatPDF = 17
    word = comtypes.client.CreateObject('Word.Application')
    # word.Visible = False
    doc = word.Documents.Open(inputFileName)
    doc.SaveAs(outputFileName, FileFormat=wdFormatPDF)
    doc.Close()
    word.Quit()


def ppttopdf(inputFileName, outputFileName):
    import pythoncom
    pythoncom.CoInitialize()
    formatType = 32
    powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
    # powerpoint.Visible = False
    if outputFileName[-3:] != 'pdf':
        outputFileName = outputFileName + ".pdf"
    deck = powerpoint.Presentations.Open(inputFileName)
    deck.SaveAs(outputFileName, formatType) # formatType = 32 for ppt to pdf
    deck.Close()
    powerpoint.Quit()

def pdf_con(media_dir,filename,user_id):
    filename = filename+".pdf"
    img = convert_from_bytes(open(os.path.join(media_dir,str(filename)), 'rb').read())
    thumb_img = os.path.join(media_dir,(str(filename)+'.png')) 
    img[0].save(thumb_img)
    thumb_path = os.path.join('media\\',str(user_id)+'\\','media\\',str(filename)+'.png')
    return thumb_path

def font_ext(media_dir,filename,user_id):
    image = Image.open(r'E:\Django\\git\\file_drive-master\\content\\media\\black.jpg')
    draw = ImageDraw.Draw(image) 
    ttf_file = os.path.join(media_dir,str(filename))
    font = ImageFont.truetype(ttf_file, 37)
    text = '               1 2 3 4 5 6 7 8 9 0 \n\n\n   A B C D E F G H I J K L M N O P Q \n                R S T U V W X Y Z\n\n \n  a b c d e f g h i j k l m n o p q r s\n                t u v w x y z\n\n \n   ` ~ ! @ # $ % ^ & * ( ) _ - + = { } [ ] \\ \n                | : ; " < > , . ? /'
    draw.text((10, 20), text, font = font) 
    thumb_img = os.path.join(media_dir,(str(filename)+'.png'))
    image.save(thumb_img)
    thumb_path = os.path.join('media\\',str(user_id)+'\\','media\\',str(filename)+'.png')
    return thumb_path