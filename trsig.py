import cv2


car_cascade = cv2.CascadeClassifier('cars.xml')

im1 = cv2.imread('trafficimages/car1.jpg')
im2 = cv2.imread('trafficimages/car2.jpg')
im3 = cv2.imread('trafficimages/car3.jpg')
im4 = cv2.imread('trafficimages/car4.jpg')



gray = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)

cars = car_cascade.detectMultiScale(gray, 1.1, 1)
for (x,y,w,h) in cars:
	cv2.rectangle(im3,(x,y),(x+w,y+h),(0,0,255),2)

var1 = len(cars)


gray = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)

cars = car_cascade.detectMultiScale(gray, 1.1, 1)
for (x,y,w,h) in cars:
	cv2.rectangle(im3,(x,y),(x+w,y+h),(0,0,255),2)

var2 = len(cars)


gray = cv2.cvtColor(im3, cv2.COLOR_BGR2GRAY)

cars = car_cascade.detectMultiScale(gray, 1.1, 1)

for (x,y,w,h) in cars:
	cv2.rectangle(im3,(x,y),(x+w,y+h),(0,0,255),2)
var3 = len(cars)


gray = cv2.cvtColor(im4, cv2.COLOR_BGR2GRAY)

cars = car_cascade.detectMultiScale(gray, 1.1, 1)

for (x,y,w,h) in cars:
	cv2.rectangle(im4,(x,y),(x+w,y+h),(0,0,255),2)
var4 = len(cars)

# print(max)


# print("The lane " +str(flag)+ " is open")


cv2.imshow('image1',im1)
cv2.imshow('image2',im2)
cv2.imshow('image3',im3)
cv2.imshow('image4',im4)




cv2.waitKey(0)
cv2.destroyAllWindows()
