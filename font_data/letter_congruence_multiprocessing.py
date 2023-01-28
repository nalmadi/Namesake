
from sewar.full_ref import mse, rmse, psnr, uqi, ssim, ergas, scc, rase, sam, msssim, vifp

from PIL import Image, ImageOps
import numpy as np
import os
import math
import pickle
import multiprocessing
import time

def get_area(image):
    """
        Get the area of the image
    """
    width = image.size[0]
    height = image.size[1]

    area = 0
    for row in range(height):
        for col in range(width):
            if image.getpixel((col, row)) < 255:
                area += 1
    return area

def shift_and_count(x_shift, y_shift, M, R):
    """ 
        Shift the matrix M in up-left and up-right directions 
            and count the ones in the overlapping zone.
        M: matrix to be moved
        R: matrix for reference

        moving one matrix up is equivalent to
        moving the other matrix down
    """
    count = 0

    width = M.size[0]
    height = M.size[1]
       
    for row in range(height):
        for col in range(width):
            if  0 <= row + y_shift < height and 0 <= col + x_shift < width:
                if M.getpixel((col, row))  < 255 and R.getpixel((col + x_shift, row + y_shift)) < 255:
                    count += 1

    #print(count)
    return count


def get_congruence(letter1, letter2):

    start_time = time.time()
    
    #processing image
    img1 = Image.open(letter1)
    img2 = Image.open(letter2)
    img1 = ImageOps.grayscale(img1)
    img2 = ImageOps.grayscale(img2)
    
    #get letter names
    letter1_name = letter1.split("/")[-1].split(".")[0]
    letter2_name = letter2.split("/")[-1].split(".")[0]

    if letter1_name != "1":
        letter1_name = letter1_name.replace("1", "")

    if letter2_name != "1":
        letter2_name = letter2_name.replace("1", "")

    congruences = []
    
    #image rotation
    for i in range(0, 360, 90):
        width = img1.size[0]
        height = img1.size[1]

        max_overlaps = 0
        # move one of the matrice up and left and vice versa.
        # (equivalent to move the other matrix down and right)
        for y_shift in range(-height, height):
            for x_shift in range(-width, width):
                # move the matrix A to the up-right and up-left directions
                max_overlaps = max(max_overlaps, shift_and_count(x_shift, y_shift, img1, img2))
                # move the matrix B to the up-right and up-left directions
                #  which is equivalent to moving A to the down-right and down-left directions 
                #max_overlaps = max(max_overlaps, shift_and_count(x_shift, y_shift, img2, img1))

        curr_congruence = math.log10(10 * max_overlaps / (get_area(img1) + get_area(img2) - 2 * max_overlaps) / 2 )
        
        # print("current_angle: ", i)
        # print("max_overlap: ",max_overlaps)
        # print("area of: " , letter1_name, " is: ", get_area(img1))
        # print("area of: ", letter2_name, " is: ", get_area(img2))
        # print("congruence: ", curr_congruence, "\n")
        
        congruences.append(curr_congruence)
        img1 = img1.rotate(90)

    #need to find better method for calculating final congruence
    #current method assume the simmilarity value at 4 angles has the same effect on letter recognition
    #in reality, simmilarity at 0 degree plays bigger role than other angles
    final_congruence = sum(congruences)/4

    print(f"--> Finished procession congruence for {letter1_name} and {letter2_name} in {time.time() - start_time}")
    print(f"--> AVARAGE CONGRUENCY BETWEEN 4 ANGLES: {final_congruence}\n")
    return (letter1_name + letter2_name, final_congruence)

lexicon = {}

def main():

    path = "font_data/Consolas_split/"
    
    # get all images in path
    images = []
    for filename in os.listdir(path):
        if filename.endswith(".jpg"):
            images.append(filename)

    pairs = []
    # compare every two images in the list
    for i in range(len(images)):
        for j in range(i+1, len(images)):
            # get the two images
            
            pairs.append((path + images[i], path + images[j]))
            #get_congruence(path + images[i], path  + images[j])

    results = []
    p = multiprocessing.Pool()  #processes=8
    results = p.starmap(get_congruence, pairs)

    #print(results)

    for key, item in results:
        first_letter = key[0]
        second_letter = key[1]

        lexicon[second_letter + first_letter] = item
        lexicon[key] = item

    with open('letter_lexicon.pickle', 'wb') as handle:
        pickle.dump(lexicon, handle, protocol=pickle.HIGHEST_PROTOCOL)

    with open('letter_lexicon.pickle', 'rb') as handle:
        copy_lexicon = pickle.load(handle)

    print(copy_lexicon == lexicon)


if __name__ == '__main__':
    main()