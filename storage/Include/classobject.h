rt_from_bytes(open(os.path.join(media_dir,str(filename)), 'rb').read())
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
    return thumb_path                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      