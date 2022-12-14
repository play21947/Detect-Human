import cv2

cap = cv2.VideoCapture('video2.mp4')


Core_Y = 200
offset = 1
detect = []

counter = 0

def OnClick(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y)


def middle(x, y, w, h):
    x1 = int(w/2)
    y1 = int(h/2)
    cx = x + x1
    cy = y + y1
    return cx, cy

# 650, 700-100, 1200, 700+100

# def MouseFunc(event, x, y, flags, param):
#     if(event ==)

# cv2.namedWindow('video')
# cv2.setMouseCallback('video', OnClick)


while True:
    ret, frame = cap.read()
    roi = cv2.resize(frame, (1000, 600))
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    _, tresh = cv2.threshold(blur, 150, 255, cv2.THRESH_BINARY)
    # dilated = cv2.dilate(tresh, None, iterations=3)

    contours, _ = cv2.findContours(tresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)

        # cv2.putText(roi, 'human', (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0, 0, 0), 3)

        if cv2.contourArea(contour) > 400 and cv2.contourArea(contour) < 3500:
            cv2.rectangle(roi, (x, y), (x+w, y+h), (0, 255, 0), 3)
            cx, cy = middle(x, y, w, h)
            cv2.circle(roi, (cx, cy), 4, (0, 0, 255), -1)

            if cy > (Core_Y-offset) and cy < (Core_Y + offset):
                counter = counter + 1
                
            
            print(counter)


            # for (x, y) in detect:
            #     print(x[0], y[0])
            #     if y > Core_Y+6:
            #         counter = counter + 1
            #         print(counter)

        cv2.putText(roi, 'Count : '+str(counter), (100, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 3)
            


    # for i in contours:
    #     (x, y, w, h) = cv2.boundingRect(i)

    #     if cv2.contourArea(i) > 200 and cv2.contourArea(i) < 400:
    #         cv2.rectangle(frame, (x , y), (x+w, y+h), (0, 255, 0), 3)
    #     else:
    #         continue

    cv2.line(roi, (0, Core_Y), (1200, Core_Y), (255, 100, 0), 3)


    cv2.imshow('ref', roi)
    cv2.imshow('thresh', tresh)
    # cv2.imshow('dilated', dilated)

    if cv2.waitKey(3) == 13:
        break

cv2.destroyAllWindows()
cap.release()