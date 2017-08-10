import cv2
import numpy as np

################  HW0  #####################
# Nathana Facion                 RA:191079
# Rafael Mariottini Tomazela     RA:192803
############################################

DEBUG = False

def Questao2(r,g,b):
    #merge back but changint red and blue
    imgswaprb = cv2.merge((r, g, b))

    #show and save // letter a
    if DEBUG == True : debug('image', imgswaprb)
    cv2.imwrite('output/p0-2-a-0.png', imgswaprb)

    #green channel img / show and save // letter b
    if DEBUG == True : debug('image', g)
    cv2.imwrite('output/p0-2-b-0.png', g)

    #red channel img /show and save // letter c
    if DEBUG == True : debug('image', r)
    cv2.imwrite('output/p0-2-c-0.png', r)

def Questao3(r,g,b):
    # take the center square region
    squareregion = 100

    answer = g
    other = r

    #now lets create A and B
    A = answer
    Bout = other.copy()

    (rows, cols) = answer.shape

    swidth = int(rows/2 - squareregion/2)
    ewidth = swidth + squareregion
    sheight = int(cols/2 - squareregion/2)
    eheight = sheight + squareregion

    Bout[swidth:ewidth, sheight:eheight] = A[swidth:ewidth, sheight:eheight]

    if DEBUG == True : debug('Bout', Bout)
    cv2.imwrite('output/p0-3-a-0.png', Bout)

    #Now recreate the original image with the correct channel
    #Since I think the answer is the red one, gonna change that

    imgchangedred = cv2.merge((b, g, Bout))
    if DEBUG == True : debug('imgchangedred', imgchangedred)
    cv2.imwrite('output/p0-3-b-0.png', imgchangedred)

def Questao4(r,g,b):
    # letter a
    print("Min of green channel: %.2f" % g.min())
    print("Max of green channel: %.2f" % g.max())
    print("Mean of green channel: %.2f" % g.mean())
    print("Std of green channel: %.2f" % g.std())


    # letter b
    #normalize g
    gmean = float(g.mean())
    gstd = float(g.std())

    ng = g.astype(float)

    ng = ng - gmean # That is, subtract the mean from all pixels
    ng /= gstd # Then divide them by the standard deviation
    ng *= 10 #  Then multiply by 10
    ng += gmean # Now add the mean back to each pixel

    ngout = ng.astype(int)
    if DEBUG == True : debug('ng', ngout)
    cv2.imwrite('output/p0-4-b-0.png', ngout)

    # letter c
    #roll the green channel
    shiftedgreen = np.roll(g, 2, axis=1) #   Shift img-green to the left by 2 pixels

    #subtract
    resultsubshift = g - shiftedgreen #  Subtract the shifted version to the original, and save the difference image
    resultsubshift[resultsubshift < 0] = 0

    if DEBUG == True : debug('shiftedgreen',resultsubshift)
    cv2.imwrite('output/p0-4-c-0.png', resultsubshift)

def Questao5(r,g,b):
    #create a matrix of the same size by copying
    gaussian_noise = g.copy()
    cv2.randn(gaussian_noise, 0, 30);

    # letter a
    # add Gaussian noise to the pixels in the green channel
    noisy_g = g + gaussian_noise
    noisy_imgg = cv2.merge((b, noisy_g, r))
    if DEBUG == True : debug('noisy_imgg',noisy_imgg)
    cv2.imwrite('output/p0-5-a-0.png', noisy_imgg)

    #letter b
    # add the noise using the same sigma to the blue
    noisy_b = b + gaussian_noise
    noisy_imgb = cv2.merge((noisy_b, g, r))
    if DEBUG == True : debug('noisy_imgg',noisy_imgg)
    cv2.imwrite('output/p0-5-b-0.png', noisy_imgb)


def debug(name,img):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    #Loads color image
    img = cv2.imread('input/p0-1-0.png')

    #split into channels
    b,g,r = cv2.split(img)

    Questao2(r,g,b)
    Questao3(r,g,b)
    Questao4(r,g,b)
    Questao5(r,g,b)


if __name__ == '__main__':
   main()
