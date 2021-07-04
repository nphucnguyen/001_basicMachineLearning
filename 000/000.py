import cv2
# doan code mo camera
# chon camera chinh
camera_id = 0

# open camera
cap = cv2.VideoCapture(camera_id)

# read frame from camera
while True:
    # read image
    ret, frame = cap.read()
    # show image
    cv2.imshow('Cam',frame)
    # check if press Q : exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#release camera
cap.release()
cv2.destroyWindow()

'''
# code for resize image
image_rs = cv2.resize(image, dsize = (200,200))
cv2.imshow("Anh rs", image_rs)

# rotate image
image_rotate = imutils.rotate(image, 90)

# threshold
image = cv2.imread("beauty.jpg")
image_gray = cv2.cvtColor(image, cv2.COLOR.BGR2GRAY)
ret, thresh_binary = cv2.threshold(image_gray, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("Anh threshold", thresh_binary)

#blur
blur = cv2.GaussianBlur(image, ksize = (31,51), sigmaX = 0)
cv2.imshow("anh blur", blur)

# contour
frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
cv2.imshow("anh tu webcam", frame)


'''