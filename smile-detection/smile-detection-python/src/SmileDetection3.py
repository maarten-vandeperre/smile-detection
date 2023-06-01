import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_smile.xml')


def detect(img):
    # convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detects faces in the input image
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    print('Number of detected faces:', len(faces))

    # loop over all the faces detected
    for (x,y,w,h) in faces:

        # draw a rectangle in a face
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
        cv2.putText(img, "Face", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        # detecting smile within the face roi
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.8, 20)
        # if len(smiles) > 0:
        if len(smiles) > 1:
            print("smile detected")
            for (sx, sy, sw, sh) in smiles:
                cv2.rectangle(roi_color, (sx, sy), ((sx + sw), (sy + sh)), (0, 0, 255), 2)
                cv2.putText(roi_color, "smile", (sx, sy),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        else:
            print("smile not detected")

    return img


# faces = face_cascade.detectMultiScale(gray, 1.3, 5)

video_capture = cv2.VideoCapture(0)
while video_capture.isOpened():
    try:
        # Captures video_capture frame by frame
        _, frame = video_capture.read()

        # To capture image in monochrome
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # calls the detect() function
        canvas = detect(frame)

        # Displays the result on camera feed
        cv2.imshow('Video', canvas)

        # The control breaks once q key is pressed
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
    except Exception as inst:
        print(type(inst))
        print(inst.args)
        print(inst)


# Release the capture once all the processing is done.
video_capture.release()
cv2.destroyAllWindows()