import sys
import os.path
from display import *

def print_usage():
	pass


def main():

	n = len(sys.argv)


	if 2 <= n and n <= 4:

		imgpath = sys.argv[1]

		# accidentally passed directory name case
		if os.path.isdir(imgpath):
			print('{} is a directory. Supply an image file instead.'.format(imgpath))
			sys.exit()

		# path does not exist case
		if not os.path.isfile(imgpath):
			print('image filepath does not exist!\nThe file must be in the current working directory.')
			sys.exit()

		# cliv <imgpath>
		# display whole image
		if n == 2:
			display_entire_image(imgpath)
	
		# cliv <imgpath> -g grid_section
		# display one section of the image
		elif n == 4:
			if not sys.argv[2].isnumeric() or not sys.argv[3].isnumeric():
				print_usage()
			else:
				display_entire_image(imgpath, int(sys.argv[2]), int(sys.argv[3]))


		else:
			print_usage()

# end def main()



# call main
main()
