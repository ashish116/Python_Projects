import cv2

#image whose quality to be increased is parsed using cv2
img = cv2.imread('image.png')

#clahe is image enhancement technique that uses histogram
clahe = cv2.createCLAHE()

#convert image to grayscale image
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#enhancement
enh_img = clahe.apply(gray_img)

#save to new file
cv2.imwrite('enhanced.png',enh_img)
print('Done enhancing')
