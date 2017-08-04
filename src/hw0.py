import cv2
import numpy as np

################  HW0  #####################
# Nathana Facion                 RA:191079
# Rafael Mariottini Tomazela     RA:192803 
############################################

DEBUG = True

def Questao2(r,g,b):
    #merge back but changint red and blue
    imgswaprb = cv2.merge((r, g, b))

    #show and save
    if DEBUG == True : debug('image', imgswaprb)
    cv2.imwrite('output/p0-2-a-0.png', imgswaprb)

    #green channel img / show and save
    if DEBUG == True : debug('image', g)
    cv2.imwrite('output/p0-2-b-0.png', g)

    #red channel img /show and save
    if DEBUG == True : debug('image', r)
    cv2.imwrite('output/p0-2-c-0.png', r)

def Questao3(r,g,b):
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

    if DEBUG == True : debug('Bout', Bout)
    cv2.imwrite('output/p0-3-a-0.png', Bout)

    #Now recreate the original image with the correct channel
    #Since I think the answer is the red one, gonna change that

    imgchangedred = cv2.merge((b, g, Bout))
    if DEBUG == True : debug('imgchangedred', imgchangedred)
    cv2.imwrite('output/p0-3-b-0.png', imgchangedred)

    print("Min of green channel: %.2f" % g.min())
    print("Max of green channel: %.2f" % g.max())
    print("Mean of green channel: %.2f" % g.mean())
    print("Std of green channel: %.2f" % g.std())

def Questao4(r,g,b):
    #normalize g
    gmean = float(g.mean())
    gstd = float(g.std())

    ng = g.astype(float)

    ng = ng - gmean
    ng /= gstd
    ng *= 10
    ng += gmean

    ngout = ng.astype(int)
    if DEBUG == True : debug('ng', ngout)
    cv2.imwrite('output/p0-4-b-0.png', ngout)

    print("The colors of the image are smoother")

    #roll the green channel
    shiftedgreen = np.roll(g, 2, axis=1)

    #subtract
    resultsubshift = g - shiftedgreen
    if resultsubshift.min() < 0:
        resultsubshift += resultsubshift.min()
 
    if DEBUG == True : debug('shiftedgreen',resultsubshift)
    cv2.imwrite('output/p0-4-c-0.png', resultsubshift)

    print("A imagem subtraida tem principalmente as bordas, porque eh onde muda de cor.. acho")


def Questao5(r,g,b):
    #Question 5
    #create a matrix of the same size by copying
    gaussian_noise = g.copy()
    cv2.randn(gaussian_noise, 0, 30);

    #add to the img
    noisy_g = g + gaussian_noise
    noisy_imgg = cv2.merge((b, noisy_g, r))
    if DEBUG == True : debug('noisy_imgg',noisy_imgg)
    cv2.imwrite('output/p0-5-a-0.png', noisy_imgg)

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

