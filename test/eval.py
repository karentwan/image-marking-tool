import cv2



img_path = r'E:\water_meter\data\all_img/0.jpg'
label = r'E:\water_meter\data\label/0.txt'

img = cv2.imread(img_path)
cv2.namedWindow('image show')
cv2.imshow('image show', img)
cv2.waitKey(0)
cv2.destroyAllWindows()