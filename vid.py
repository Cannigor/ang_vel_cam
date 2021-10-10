import cv2
import numpy as np
import datetime

camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while camera.isOpened():
    success, img = camera.read()

    img = cv2.resize(img, (img.shape[1] * 2, img.shape[0] * 2))
    h = len(img)
    w = len(img[0])
    angle = np.pi / 4

    x_up, y_up = w // 2, h // 4
    x_down, y_down = w // 2, h - h // 4
    x_right, y_right = w - w // 4, h // 2
    x_left, y_left = w // 4, h // 2

    # print('яркость_верх', img[y_up][x_up])
    # print('яркость_низ', img[y_down][x_down])
    # print('яркость_прав', img[y_right][x_right])
    # print('яркость_лев', img[y_left][x_left])

    B_up, G_up, R_up = img[y_up][x_up]
    avg_up = sum([R_up, G_up, B_up]) // 3
    if avg_up < 60:
        avg_up = 0
    else:
        avg_up = 255
    print('средняя яркость верх', avg_up)
    
    B_down, G_down, R_down = img[y_down][x_down]
    avg_down = sum([R_down, G_down, B_down]) // 3
    if avg_down < 60:
        avg_down = 0
    else:
        avg_down = 255
    print('средняя яркость низ', avg_down)
    
    B_right, G_right, R_right = img[y_right][x_right]
    avg_right = sum([R_right, G_right, B_right]) // 3
    if avg_right < 60:
        avg_right = 0
    else:
        avg_right = 255
    print('средняя яркость прав', avg_right)
    
    B_left, G_left, R_left = img[y_left][x_left]
    avg_left = sum([R_left, G_left, B_left]) // 3
    if avg_left < 60:
        avg_left = 0
    else:
        avg_left = 255
    print('средняя яркость лев', avg_left)

    print('***************')

    if avg_up == 0:
        start_time = datetime.datetime.now().time()
        print('still black')
        print('st', start_time)
    else:
        end_time = datetime.datetime.now().time()
        print('white')
        print('end', end_time)

    # print('delta', start_time - end_time)
    # omega = angle / delta

    print('------------------------')

    cv2.line(img, (0, h // 2), (w, h // 2), (0, 0, 255), thickness=2)  # center
    cv2.line(img, (w // 2, 0), (w // 2, h), (0, 0, 255), thickness=2)

    cv2.line(img, (0, h // 4), (w, h // 4), (255, 0, 0), thickness=1)  # up
    cv2.line(img, (w // 4, 0), (w // 4, h), (255, 0, 0), thickness=1)  # left
    cv2.line(img, (w - w // 4, 0), (w - w // 4, h), (255, 0, 0), thickness=1)  # right
    cv2.line(img, (0, h - h // 4), (w, h - h // 4), (255, 0, 0), thickness=1)  # down

    cv2.imshow('circle_test', np.hstack([img]))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
