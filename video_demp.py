import cv2

video = cv2.VideoCapture(r"C:\Users\Himanshu\Downloads\855289-hd_1920_1080_25fps.mp4")
while True:
    status, frame = video.read()
    if not status:break
    #make changes from this line
    newframe=frame *10
    bw=cv2.cvtColor(frame,cv2.COLOR_BAYER_BG2GRAY)
    rgb=cv2.cvtColor(frame,cv2.COLOR_BAYER_BG2RGB)
    cv2.imshow("Video", frame)
    cv2.imshow("new video frame",newframe)
    cv2.imshow("b/w",bw)
    cv2.imshow("rgb",rgb)
    if cv2.waitKey(1) == 27:
        break

video.release()
cv2.destroyAllWindows()