import cv2
import numpy as np

# create list of alphabet upper case and lower case and numbers from 0 to 9
alphabet_list = []
#for i in range(65, 91):
    #alphabet_list.append(chr(i))
#for i in range(97, 123):
    #alphabet_list.append(chr(i))
for i in range(10):
    alphabet_list.append(str(i))
print(alphabet_list)
#exit()


def next_char_name():

    letter = alphabet_list.pop(0)
    return letter


img = cv2.imread("consolas_font.png")
print(img.shape) # Print image shape
cv2.imshow("original", img)


def just_print_for_all(event, x, y, flags, param):
    
   if event == 4:
    #cv2.rectangle(img, pt1=(x-20,y-35), pt2=(x+20, y+35),color=(0,0,255),thickness=1)
    cv2.imshow("original", img)

    cropped_image = img[y-35:y+35, x-20:x+20]
    cv2.imshow("cropped", cropped_image)
    file_name = next_char_name()
    cv2.imwrite( file_name + ".jpg", cropped_image)
    #print(next_char_name())

# set when to have a call back
#cv2.namedWindow("Title of Popup Window")

#what to happen on call back
cv2.setMouseCallback("original", just_print_for_all)

#show image to user with title
#cv2.imshow("Title of Popup Window", scaled_image)
cv2.waitKey()
cv2.destroyAllWindows()

cv2.waitKey(0)
cv2.destroyAllWindows()