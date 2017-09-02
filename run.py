import display
import commitFile
import argparse

if __name__ == "__main__":
	
	example = "Example : python run.py -v 0 text.txt"

	#Getting options from user
	parser = argparse.ArgumentParser(epilog = example)
	parser.add_argument('filepath',nargs=1,help="relative path of file from the './local/' or './repo/' directory that has to be commited or displayed")
	parser.add_argument('-v','--ver',nargs=1,help='displays the VER version of the file')
	args = parser.parse_args()
	filepath = args.filepath[0]
	#Commit operation
	if args.ver is None:
		commitFile.commitFile(filepath)
	#Display operation
	else:
		ver_no = args.ver[0]
		display.displayFile(ver_no,filepath)
