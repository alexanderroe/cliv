import sys
import math
import os.path
import numpy as np
from PIL import Image


# convert (r, g, b) triple into ANSI color code (0 ~ 255)
def rgbToAnsi(r, g, b):
	
	if r == g and g == b:

		if r < 8:

			return 16

		if r > 248:

			return 231

		return int ((r-8) / 247 * 24 + 232)

	return 16 + (36 * int(r / 255 * 5)) + (6 * int(g / 255 * 5)) + int(b / 255 * 5)
	

def display_image(imgpath : str) -> None:

	img = Image.open(imgpath)
	img = img.convert('RGB')

	# arr is 3d numpy array, holding rgb values for each pixel in img
	arr = np.array(img)

	# get current command line window dimensions
	# multiply y by 2 since Unicode block characters allow two colors per character space
	scaled_x = int(os.popen('tput cols').read().strip('\n'))
	scaled_y = 2 * int(os.popen('tput lines').read().strip('\n'))

	skip_size = -1

	# if image is wider than window
	if (img.width / img.height) > (scaled_x / scaled_y):
		skip_size = math.ceil(img.width / (0.9 * scaled_x)) # *0.9 for some space

	# if image is taller than window
	else:
		skip_size = math.ceil(img.height / (0.9 * scaled_y))

	for i in range(0, img.height - int(skip_size), 2 * skip_size): # *2 to work 2 rows every iteration

		color = 'echo \"'

		for j in range(0, img.width, skip_size):

			i2 = i + skip_size

			top = rgbToAnsi(arr[i][j][0], arr[i][j][1], arr[i][j][2])
			bottom = rgbToAnsi(arr[i2][j][0], arr[i2][j][1], arr[i2][j][2])

			color += '\033[48;5;{}m\033[38;5;{}m▄'.format(top, bottom)

		color += '\033[48;5;0m\"'
		os.system(color)

	# set colors back to normal
	print('\033[48;5;0m\033[38;5;255m')

	# print metadata
	print('Image: {}\n'.format(sys.argv[1]))


def main():

	n = len(sys.argv)

	if n >= 2:

		for i in range(1, n):

			imgpath = sys.argv[i]

			# accidentally passed in directory
			if os.path.isdir(imgpath):
				print('{} is a directory. Supply an image file instead.'.format(imgpath))
				sys.exit()

			# path does not exist
			if not os.path.isfile(imgpath):
				print('Image filepath does not exist!\nThe file must be in the current working directory.')

			display_image(imgpath)

	else:
		print('Usage: python3 cliv.py file1 file2 ...')


if __name__ == "__main__":
	main()
