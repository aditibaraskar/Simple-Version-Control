#This function reconstructs the previous version specified 
#using the .dif file created"""

import re
import os.path
def displayFile(version_no,filename):
	repofile="./repo/"+filename
	fileWOext, ext = os.path.splitext(filename)
	remoteDiff = "./repo/"+fileWOext+".dif"
	
	fdiff=open(remoteDiff,'r')
	f=open(repofile,'r')
	curr_ver = re.search('(?<=Current version = )\w+',fdiff.readline())
	
	if int(curr_ver.group(0))<int(version_no):
		print "Version no.",version_no,"does not exist!"
		return
		
	n=int(curr_ver.group(0))-int(version_no)
	lines=reversed(fdiff.readlines())
	final_ver = []
	for l in f.readlines():
		final_ver.append(l.rstrip('\n '))
	while(n!=0):	#traces back all changes between the two versions
		token=next(lines)
		pattern=re.compile(r'^([\d]+):\s([\w]+)[\s]*([\d]*)[\s]*([\w ]*)') #tokenising the contents of .dif file
		found=pattern.match(token)
		ver=found.groups()[0]
		operation=found.groups()[1]
		line_no = found.groups()[2]
		text = found.groups()[3]
		if(operation=="add"): #delete the last line as the previous function did not contain it
			final_ver.pop()
		elif (operation=="del"): # add the line specified to the specific line number
			index=int(line_no)-1
			final_ver.insert(index,text)
		n=n-1
	print "File :",filename,",v.",version_no
	for l in final_ver:
		print l
