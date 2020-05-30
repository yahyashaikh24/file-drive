from PIL import Image, ImageFont, ImageDraw
import filetype
kind = filetype.guess('E:\\Django\\git\\file_drive-master\\filesystem\\Adca.ttf')
print(kind.mime)
# image = Image.open(r'E:\Django\\git\\file_drive-master\\content\\media\\black.jpg')
# draw = ImageDraw.Draw(image) 
# font = ImageFont.truetype(r'E:\\Django\\git\\file_drive-master\\filesystem\\Adca.ttf', 37)
# text = '               1 2 3 4 5 6 7 8 9 0 \n\n\n   A B C D E F G H I J K L M N O P Q \n                R S T U V W X Y Z\n\n \n  a b c d e f g h i j k l m n o p q r s\n                t u v w x y z\n\n \n   ` ~ ! @ # $ % ^ & * ( ) _ - + = { } [ ] \ \n                | : ; " < > , . ? /'
  
# draw.text((10, 20), text, font = font) 
  
# image.save('E:\\Django\\git\\file_drive-master\\filesystem\\Adca.png')