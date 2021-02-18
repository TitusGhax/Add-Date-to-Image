from PIL import Image
from PIL.ExifTags import TAGS
from PIL import ImageFont
from PIL import ImageDraw 
import os

x = 0

for img in os.listdir("input"):
	data = ""
	image = Image.open("input/{}".format(img))
	exifdata = image.getexif()
	for tag_id in exifdata:
		tag = TAGS.get(tag_id,tag_id)
	
		if tag == "DateTimeOriginal":
			data = exifdata.get(tag_id)
		if isinstance(data, bytes):
			data = data.decode()
	
	
	draw = ImageDraw.Draw(image)
	font = ImageFont.truetype("Aaargh.ttf",160)
	draw.text((2950,2700),data[0:10],(255,255,255),font=font)
	image.save("output/{}.jpg".format(x))
	print("Bild: [{}.jpg] generiert".format(x))
	x += 1
print("-> Abgeschlossen")