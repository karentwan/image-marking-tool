import cv2


img_path = r'E:\water_meter\data\new_500/445.jpg'
label = r'E:\water_meter\data\label/445.txt'

img = cv2.imread(img_path)
[h, w, _] = img.shape
print('width:{}\theight:{}'.format(w, h))

f = open(label, 'r')
str = f.readlines()[0]
f.close()
s = str.split(',')
points = [float(s[i]) for i in range(1, 9)]

# print(points)

d_points = [(int(points[0] * w), int(points[4] * h)),
            (int(points[1] * w), int(points[5] * h)),
            (int(points[2] * w), int(points[6] * h)),
            (int(points[3] * w), int(points[7] * h))]
for p in d_points:
    print('坐标：{}'.format(p))
    cv2.circle(img, p, 1, (0, 0, 255), 4)


cv2.namedWindow('image show')

cv2.imshow('image show', img)
cv2.waitKey(0)
cv2.destroyAllWindows()