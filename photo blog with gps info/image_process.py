from PIL import Image
import os
def image_write(md5,pic):
	convert_image = {
	    1: lambda img: img,
	    2: lambda img: img.transpose(Image.FLIP_LEFT_RIGHT),                              
	    3: lambda img: img.transpose(Image.ROTATE_180),                                   
	    4: lambda img: img.transpose(Image.FLIP_TOP_BOTTOM),                              
	    5: lambda img: img.transpose(Image.FLIP_LEFT_RIGHT).transpose(Pillow.ROTATE_90),  
	    6: lambda img: img.transpose(Image.ROTATE_270),                                   
	    7: lambda img: img.transpose(Image.FLIP_LEFT_RIGHT).transpose(Pillow.ROTATE_270), 
	    8: lambda img: img.transpose(Image.ROTATE_90),                                    
	}
	f=open('pic/_%s.jpg'%md5,'wb')
	f.write(pic)
	f.close()
	img=Image.open('pic/_%s.jpg'%md5)
	exif = img._getexif()
	orientation = exif.get(0x112, 1)
	new_img = convert_image[orientation](img)
	new_img.save('pic/%s.jpg'%md5)
	new_img.close()
	try:
		img.close()
	except:
		pass
	os.remove('pic/_%s.jpg'%md5)