#!/usr/bin/python3



f = open('faceRecFrame1.py',"r+")



#line = []
#line.append(StdID)
#line.append(FirstName)

import sys 


FirstName = str(sys.argv[1])
StdID = str(sys.argv[2])

Lines = f.readlines()
searchquery0 = "video_capture = cv2.VideoCapture(0)"
searchquery1 = "known_face_encodings = ["
searchquery2 = "known_face_names = ["


for i, line in enumerate(Lines):
    
    
    if line.startswith(searchquery0):
        
        Lines[i+1] = '\n\n{}'.format(FirstName) + "_image = face_recognition.load_image_file(./images/\"" + '{}'.format(FirstName) + ".jpg\")\n"
        Lines[i+2] = '\n\n{}'.format(FirstName) +"_face_encoding = face_recognition.face_encodings(" + '{}'.format(FirstName) + "_image)[0]\n\n"
    
    
    if line.startswith(searchquery1):
        #f.write(FirstName + "_face_encoding,\n")
        Lines[i+1] = "\n" + FirstName + "_face_encoding,\n"
        
       
        
    elif line.startswith(searchquery2):
        Lines[i+1] = '\n"{}",\n'.format(FirstName)
        #Lines[i+1] = "\n" + FirstName + ",\n"
        
    f.seek(0)
    f.writelines(Lines) 
        

        
f.close()








