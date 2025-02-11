import cv2
import cvzone
import os
def glass(image,width,height,xa,ya ):
   cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
   overlay_file=image
    
   overlay=cv2.imread(overlay_file,cv2.IMREAD_UNCHANGED)
   cap=cv2.VideoCapture(0)
   while True:
        ret,frame=cap.read()
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces=cascade.detectMultiScale(gray)
        for (x, y, w, h) in faces:
            overlay_resize = cv2.resize(overlay,(int(w*width),int(h*height)))
            frame=cvzone.overlayPNG(frame,overlay_resize,[x+xa,y+ya])
        cv2.imshow("Your Filter",frame)
        if cv2.waitKey(10)==ord('q'):
            break
        cv2.waitKey(1)
   cap.release()
   cv2.destroyAllWindows()

while(1):
  print("***********************************************************************************************************************************")
  print("1. Rectangular\n2. Cat Eye\n ")
  print("    ")
  choice=input("Enter your choice:")
  print("  ")
  print("***********************************************************************************************************************************")
  if choice=='1':
            glass('f.png',1,0.5,0,40)

  elif choice=='2':
            glass('d.png',0.8,0.2,25,60)    
            
  else:  
            print("enter valid choice !!!")  

  a=input("Enter stop to stop the program:")
  if a=='stop':
        break

