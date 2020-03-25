from ClipMaster.ClipMaster import ClipMaster
import cv2
import numpy as np


cm = ClipMaster()



#https://stackoverflow.com/questions/28327020/opencv-detect-mouse-position-clicking-over-a-picture
videoFile = 'cutAa.mp4'
video= cv2.VideoCapture(videoFile)

global mouseX,mouseY
mouseX,mouseY = 0,0
def draw_circle(event,x,y,flags,param):
    global mouseX,mouseY
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),100,(255,0,0),-1)
        mouseX,mouseY = x,y

def onMouse(event, x, y, flags, param):
	global mouseX,mouseY
	if event == cv2.EVENT_MOUSEMOVE:
		# draw circle here (etc...)
		#print('x = %d, y = %d'%(x, y))
		mouseX,mouseY = x,y


def onMouseClick(event, x, y, flags, param):
	global mouseX,mouseY
	if event == cv2.EVENT_LBUTTONDOWN:
		# draw circle here (etc...)
		#print('x = %d, y = %d'%(x, y))
		mouseX,mouseY = x,y


#img = np.zeros((512,512,3), np.uint8)
img = cv2.imread('1.jpg')
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)
#cv2.setMouseCallback('image', onMouse)
#cv2.setMouseCallback('image', onMouseClick)


i=0
while(video.isOpened()): #1

    ret, frame = video.read()
    if ret == False:
        break
    cv2.imshow('image',frame)

    


    k = cv2.waitKey(20) & 0xFF
    if k == 27:
        break
    elif k == ord('a'):
        print(mouseX,mouseY)
    elif k == ord('s'):
    	print("Video size",cm.clip(videoFile).video_info('video_size'))
    elif k == ord(' '):
    	#pause/on
    	k = 1
    	while (k != ord(' ')):
    		k = cv2.waitKey(20) & 0xFF
    		#print(mouseX,mouseY)

    #print(mouseX,mouseY)
    i+=1



"""


while(video.isOpened()):
	k = cv2.waitKey(20) & 0xFF
    if k == 27:
        break
    elif k == ord('a'):
        print(mouseX,mouseY)

    ret, frame = video.read()
    if ret == False:
        break
    cv2.imwrite('kang'+str(i)+'.jpg',frame)
    i+=1
 
video.release()
cv2.destroyAllWindows()
"""