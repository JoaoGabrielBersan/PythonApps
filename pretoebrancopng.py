import cv2

for n in range (69,74):

    imagepng = cv2.imread('image{}.png'.format(n))
    graypng = cv2.cvtColor(imagepng, cv2.COLOR_BGR2GRAY)
    
    cv2.imwrite('pb{}.png'.format(n), graypng)

cv2.waitKey(0)
cv2.destroyAllWindows()