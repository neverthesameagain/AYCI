import subprocess
import copy
import cv2 as cv
import face_recognition as fr
import time
from datetime import datetime
import os
import sys   #just for testing...
import pickle as pkl
import embed
import recog

known_faces=dict()

vid=cv.VideoCapture(0)     #capturing the video/webcam    'nebula.mp4'
ptime=0.0                                       #previous time
count=0
process_frame=True
capturing=0
tk_name=""
name=""
match=None
start_wait=0
left_point=()
right_point=()
recognize_time=0
ctime=0
pic_no=0

#To display a rectangle on a face and display the current process on top of that ractangle
def draw_face(result_location,frame):
    actual_frame=copy.copy(frame)   #to store the actual frame to send it to capture_pic function.
    
    global match,capturing,left_point,right_point,ctime,ptime,recognize_time,pic_no
    if result_location:
        for face_loc in result_location:
            left_point=(int(face_loc[3]*4*1.5),int(face_loc[0]*4*1.5))
            
            right_point=(int(face_loc[1]*4*1.5),int(face_loc[2]*4*1.5))
            #displaying a rectangle around the face
            cv.rectangle(frame,left_point,right_point,(140,4,90),1)
            #display the information of current process going on...
            display_process_info(frame)
            
            if capturing>0:

                frame,pic_no,capturing=embed.capture_pic(actual_frame,pic_no,capturing)
                if ctime-ptime <1:
                    capturing+=ctime-ptime
                if(pic_no>4):
                    know_the_faces()
                    capturing=0
                    recognize_time=0
                    pic_no=0

    return frame

def display_process_info(frame):
    global match,recognize_time,capturing,ctime,ptime

    #If person is recognized:
    if match is not None:
                cv.rectangle(frame,(left_point[0],right_point[1]),(right_point[0],right_point[1]+25),(140,4,90),cv.FILLED)
                cv.putText(frame,f"Match Found: {match}",(left_point[0]+10,right_point[1]+15),cv.FONT_HERSHEY_SCRIPT_SIMPLEX,0.45,(104,154,196),1)
                capturing=0  
                print("Taking you to the AYCI app.....")
                subprocess.call(["python","the initial home page.py"])
                sys.exit(0)

                   
    else:
        if ctime-ptime<1:
            recognize_time+=ctime-ptime
        #Do not ask for a capture until recognize_time is not greater than 5.4 i.e. giving some time to recognize:
        if recognize_time>=5.4:
            backup_frame=frame  #backup of the frame to display a different message if required.

            #If capturing is not yet started then ask the user to start it by pressing 'c'
            if capturing==0:
                cv.putText(frame,"Hold 'c' to register"+("."*count),(left_point[0],left_point[1]-5),cv.FONT_HERSHEY_DUPLEX,0.37,(0,0,255),1)
            
            #If 'c' pressed then start capturing i.e. capturing=1 => capturing>0
                if cv.waitKey(2) & 0xFF==ord('c'):
                    capturing=1

            if capturing>0:
                frame=cv.putText(backup_frame,"Registering. PLease be Still"+("."*count),(left_point[0],left_point[1]-5),cv.FONT_HERSHEY_DUPLEX,0.37,(4,100,255),1)

        else:
            cv.putText(frame,"Recognizing"+("."*count),(left_point[0],left_point[1]-5),cv.FONT_HERSHEY_COMPLEX,0.37,(255,255,0),1)



#To get the embeding of all the known faces in a dicionary
def know_the_faces():
    global known_faces

    try:
        file=open("data.pickle","rb")
        known_faces=pkl.load(file=file)
        file.close()
    except:
        known_faces=dict()
    for name in os.listdir("known_faces"):
        if name in known_faces.keys():
            if len(known_faces[name])==5:
                continue
        for i in range(5):
            image=fr.load_image_file(f"known_faces/{name}/{name}[{i}].jpg")
            encoding=fr.face_encodings(image)
            if encoding:
                    if name in (known_faces.keys()):
                        known_faces[name]+=[encoding]
                    else:
                        known_faces[name]=[encoding]
    file=open("data.pickle","wb")
    pkl.dump(known_faces,file)
    file.close()
                    

#To apply some decoration to the frame:
def decorator(img):
    h,w=img.shape[:2]
    t=datetime.now().strftime("%H:%M:%S")
    cv.putText(img,f"Time: {t}",(w-150,20),cv.FONT_HERSHEY_COMPLEX,0.5,(255,25,255),1)

    return img

#To rescale the image :
def rescale(img,scale=0.50):
    img=cv.flip(img,1)
    width=(int)(img.shape[1]*scale)
    height=(int)(img.shape[0]*scale)

    return cv.resize(img,(width,height),interpolation=cv.INTER_AREA)


know_the_faces()

#Whie loop for each frame to be displayed until 'd' is pressed
while True:
    #Calculating fps
    ctime=time.time()                           #crrent time i.e after 1 frame
    fps=2/(ctime-ptime)
    if ctime-ptime<1.0 and start_wait<=6.0:
        start_wait+=ctime-ptime

    #Capturing a frame
    isTrue,frame=vid.read()
    frame = cv.normalize(frame,None, alpha=0, beta=350, norm_type=cv.NORM_MINMAX, dtype=cv.CV_8U)

    small_frame=rescale(frame,0.25)
    frame=rescale(frame,1.5)

    cv.putText(frame,f"FPS: {int(fps)}",(20,20),cv.FONT_HERSHEY_COMPLEX,0.5,(0,255,0),1)

    if(process_frame):
        #detecting face    
        small_frame=cv.cvtColor(small_frame,cv.COLOR_BGR2RGB)
        result_location = recog.detect_face(small_frame)
        
        #recognizing face after waiting for some time 
        #1. "start_wait" -->So that the camera may start.
        #2. "recognize_time"--> recognizing only for a fixed amount of time
        if(recognize_time>=5.0 and start_wait>=4.0):
            match=recog.recognize_face(small_frame,known_faces)

        # count variable for how uch "." to print   ;)
        count+=1
        if(count==4):
            count=0
    #To take every second frame of the webcame for recogintion and detection purpose
    process_frame=not process_frame  

    frame= decorator(frame)

    frame=draw_face(result_location,frame)
    
    cv.imshow("Webcam",frame)
    ptime=ctime
        

    if cv.waitKey(2)  & 0xFF==ord('d'):
        break

vid.release()
cv.destroyAllWindows()
