import cv2
import numpy as np

#Question 2
#Loads color image
img = cv2.imread('input/p0-1-0.png')

#split into channels
b,g,r = cv2.split(img)

#merge back but changint red and blue
imgswaprb = cv2.merge((r, g, b))
cv2.imshow('image', imgswaprb)

#Show image for debugging purpose
cv2.waitKey(0)
cv2.destroyAllWindows()

#save it
cv2.imwrite('output/p0-2-a-0.png', imgswaprb)

#green channel img
#show and save
cv2.imshow('image', g)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('output/p0-2-b-0.png', g)

#red channel img
#show and save
cv2.imshow('image', r)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('output/p0-2-c-0.png', r)

#Question 3
answer = g
other = r

#now lets create A and B
A = answer
Bout = other.copy()

(rows, cols) = answer.shape

swidth = int(rows/2 - 50)
ewidth = swidth + 100
sheight = int(cols/2 - 50)
eheight = sheight + 100

Bout[swidth:ewidth, sheight:eheight] = A[swidth:ewidth, sheight:eheight]

cv2.imshow('Bout', Bout)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('output/p0-3-a-0.png', Bout)

#Now recreate the original image with the correct channel
#Since I think the answer is the red one, gonna change that

imgchangedred = cv2.merge((b, g, Bout))

cv2.imshow('imgchangedred', imgchangedred)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('output/p0-3-b-0.png', imgchangedred)

print("Min of green channel: %.2f" % g.min())
print("Max of green channel: %.2f" % g.max())
print("Mean of green channel: %.2f" % g.mean())
print("Std of green channel: %.2f" % g.std())

#question 4
#normalize g
gmean = float(g.mean())
gstd = float(g.std())

ng = g.astype(float)

ng = ng - gmean
ng /= gstd
ng *= 10
ng += gmean

ngout = ng.astype(int)

cv2.imshow('ng', ngout)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('output/p0-4-b-0.png', ngout)

print("The colors of the image are smoother")

#roll the green channel
shiftedgreen = np.roll(g, 2, axis=1)

#subtract
resultsubshift = g - shiftedgreen
if resultsubshift.min() < 0:
    resultsubshift += resultsubshift.min()
cv2.imshow('shiftedgreen', resultsubshift)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('output/p0-4-c-0.png', resultsubshift)

print("A imagem subtraida tem principalmente as bordas, porque eh onde muda de cor.. acho")

#Question 5
#create a matrix of the same size by copying
gaussian_noise = g.copy()
cv2.randn(gaussian_noise, 0, 30);

#add to the img
noisy_g = g + gaussian_noise
noisy_imgg = cv2.merge((b, noisy_g, r))
cv2.imshow('noisy_imgg', noisy_imgg)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('output/p0-5-a-0.png', noisy_imgg)

noisy_b = b + gaussian_noise
noisy_imgb = cv2.merge((noisy_b, g, r))
cv2.imshow('noisy_imgb', noisy_imgb)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('output/p0-5-b-0.png', noisy_imgb)

print("substituir azul ficou melhor, n sei pq")
