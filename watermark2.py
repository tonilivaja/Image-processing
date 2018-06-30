import Image, ImageEnhance
import os

os.system("convert -density 200 test.pdf page%01d.jpg")


def reduce_opacity(im, opacity):
	#reducing opacity
	assert opacity >= 0 and opacity <= 1
	if im.mode != 'RGBA':
		im = im.convert('RGBA')
	else:
		im = im.copy()
	alpha = im.split()[3]
	alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
	im.putalpha(alpha)
	
	return im

def watermark(im, mark, position, opacity=1):
	#adding watermark
	if opacity < 1:
		mark = reduce_opacity(mark, opacity)
	if im.mode != 'RGBA':
		im = im.convert('RGBA')
	layer = Image.new('RGBA', im.size, (0,0,0,0))
	layer.paste(mark, position)

	return Image.composite(layer, im, layer)

def run():
	im = Image.open("page0.jpg")
	mark = Image.open("zig2.png")
	watermark(im, mark, (400, 100), 0.7).save("page0.png","PNG")
	im = Image.open("page1.jpg")
	mark = Image.open("zig2.png")
	watermark(im, mark, (400, 100), 0.7).save("page1.png","PNG")
	im = Image.open("page2.jpg")
	mark = Image.open("zig2.png")
	watermark(im, mark, (400, 100), 0.7).save("page2.png","PNG")

if __name__ == '__main__':
	run()

os.system("convert page0.png page1.png page2.png rezultat.pdf")