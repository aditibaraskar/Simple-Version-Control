#This function finds the difference in the current and the previous version
#and specifies what to write to the .dif file. This function returns three parameters
#First is operation which can be either add or delete. If the operation is delete two more
#parameters line_no (to specify what line has been deleted) and text (what has been deleted)
#is specified. Incase of add both these fields are null

def findDiff(local_path,repo_path):
	f1=open(local_path,'r')
	f2=open(repo_path,'r')
	current=f1.readline().rstrip('\n')
	old=f2.readline().rstrip('\n')
	count_current=0
	count_old=0
	operation = ""
	line_no = ""
	while (current!="" and old!=""): #loops gets executed till end of file is reached for anyone of the files
		flag=0
		truth_value=(current==old)
											#checking if both lines are identical
		if (truth_value):
			current=f1.readline().rstrip('\n')
			old=f2.readline().rstrip('\n')
			count_old=count_old+1
			count_current=count_current+1
			#checking if a line has been deleted by incrementing the pointer and comparing the values of 
			#old and current files. If the values match implies a line has been deleted"""
		else: 								 
			pos_old=f2.tell()
			token=old
			old=f2.readline().rstrip('\n')
			truth_value=(current==old)
			if(old!="" and truth_value):
				operation="del"
				line_no=count_old+1
				text=token
				return operation,line_no,text
			else:   #checks if no line is inserted in the middle 
				f2.seek(pos_old)
				if(old==''):
					old=f2.readline()
				pos_curr=f1.tell()
				current=f1.readline().rstrip('\n')
				truth_value=(current==old)
				if(truth_value):
					operation=""
					text=""
					print "Error : Insertion in the middle is not allowed"
					return operation,"",text
	if (current=="") and (old!=""): #for checking end line deletion
		operation="del"
		line_no=count_old+1
		text=old
		return operation,line_no,text
	elif ((current!="") and (old=="")): #for checking if something has been appended
		operation="add"
		return operation,"",""
	elif(count_old==count_current): 
		print "Both Versions identical. No Changes"
		return "","",""