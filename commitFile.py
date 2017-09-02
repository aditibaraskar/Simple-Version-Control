#This function uses the function findDiff to fetch the operation to 
#be performed and creates or updates the copy of the current version 
#in repo directory and a .dif file for maintaining the differences 
#between different versions

import findDiff
import os.path
import shutil
import re
def commitFile(filename):
	localfile = "./local/"+filename
	remotefile = "./repo/"+filename
	fileWOext, ext = os.path.splitext(filename)
	remoteDiff = "./repo/"+fileWOext+".dif"
	if not os.path.isfile(localfile):
		print "File ",filename ," not found in local directory!"
		exit(1)
	flocal = open(localfile,'r')
	if not os.path.isfile(remotefile):
		print "Creating copy in remote directory"
		shutil.copyfile(localfile,remotefile)
		fdiff = open(remoteDiff,"w+")
		fdiff.write("Current version = 0\n")
		fdiff.close()
	else:
		fdiff = open(remoteDiff,'r')
		op_type,op_line_no,op_message = findDiff.findDiff(localfile,remotefile)
		if not op_type == '':
			m = re.search('(?<=Current version = )\w+',fdiff.readline())
			new_ver = int(m.group(0))+1
			lines = fdiff.readlines()
			fdiff.close()
			fdiff = open(remoteDiff,'w')
			fdiff.write("Current version = "+str(new_ver)+"\n")
			for line in lines:
				fdiff.write(line)
			fdiff.write("\n"+str(new_ver)+": " + op_type +" " + str(op_line_no) + " " + str(op_message))
			shutil.copyfile(localfile,remotefile)
			print "Commit successful for",filename,",v."+str(new_ver)
		fdiff.close
	flocal.close()