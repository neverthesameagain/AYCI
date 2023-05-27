import cv2 as cv
import face_recognition as fr
import os
import tkinter as tk

window=None
name=""
tk_name=""
emotions=["sad","anger","normal","Smile","laugh",""]

def submit():
    global tk_name,name,window

    name=tk_name.get()

    if verify_name(name):
        window.destroy()
    
    pass

#To display an UI to get the name of new user
def input_name():
    global tk_name,name,window
    window=tk.Tk()
    window.geometry("400x100")
    window.title("Enter Your Name")
    tk_name=tk.StringVar()
    input_box=tk.Entry(window,textvariable=tk_name)
    submit_btn=tk.Button(window,text="Submit",command=submit)
    input_box.place(relx=0.5,rely=0.5,anchor=tk.CENTER)
    submit_btn.place(relx=0.5,rely=0.51)
    window.mainloop()



def verify_name(name):
    print("verifying..")
    if name=="":
        return False
    for kname in os.listdir("known_faces"):
        if kname==name:
            return False
    print("verified")
    return True


def embedit(frame,name,i):
    parent_dir="known_faces/"
    
    path=os.path.join(parent_dir,name)
    if i==0:
        os.mkdir(path)
    print("Saving")
    cv.imwrite(f"{path}/{name}[{i}].jpg",frame)
    print("Saved")

#To capture/Register a person
def capture_pic(frame,pic_no,capturing):
    global name,emotions
    if capturing==1:
        input_name()
    if capturing >=5.0:
        capturing=1.1
        embedit(frame,name,pic_no)
        pic_no+=1
    
    cv.putText(frame,f"Capturing photo NO.{pic_no+1} : Please {emotions[pic_no]}",(150,100),cv.QT_FONT_NORMAL,0.80,(200,20,30),1)
    
    return (frame,pic_no,capturing)

    
