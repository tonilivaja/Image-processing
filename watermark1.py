import Image, ImageEnhance
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True)
ap.add_argument("-w", "--watermark", required=True)
ap.add_argument("-t", "--transparency", type=float, default=0.4)
ap.add_argument("-l", "--left", type=int, default=100)
ap.add_argument("-v", "--top", type=int, default=100)
args = vars(ap.parse_args())

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
	im = Image.open(args["input"])
	mark = Image.open(args["watermark"])
	watermark(im, mark, ((args["left"]), (args["top"])), (args["transparency"])).show()

if __name__ == '__main__':
	run()

#python zadatak.py -i primjer1.jpg -w zig1.png -t 0.7 -l 1200 -v 800