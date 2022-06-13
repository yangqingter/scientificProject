import cv2
import matplotlib.pyplot as plt

def plt_show(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.show()

def im_show(win_name, img):
    cv2.imshow(win_name, img)
    cv2.waitKey()
    cv2.destroyAllWindows()

img = cv2.imread('big.jpg')
img_G = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
im_show("g",img_G)
ret, thresh = cv2.threshold(img_G, 127, 255, 0)
im_show("b",thresh)

img_Blur= cv2.GaussianBlur(thresh, (3,3),1)

contours, hierarchy = cv2.findContours(img_Blur, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

img_c = img.copy()
im_show("c",img_c)
t1= (hierarchy[:,:,2]==-1)[0]

cv2.drawContours(img_c, contours[2:], -1, (0,0,255), 1)
im_show("c",img_c)
plt_show(img_c)


print(t1)

area = cv2.contourArea(contours[3])
print(area)












