import numpy as np
import cv2


class Operation:

    def __init__(self):
        pass

    def merge(self, image_left, image_right, column):
        """
        Merge image_left and image_right at column (column)
        
        image_left: the input image 1
        image_right: the input image 2
        column: column at which the images should be merged

        returns the merged image at column
        """
        
        # add your code here
        col = np.shape(image_right)[1]
        row = np.shape(image_right)[0]


        for i in range(0, row):
            for j in range(0, col):
                if int(j) > column:
                    image_left[i][j] = image_right[i][j]

        # Please do not change the structure
        return image_left  # Currently the original image is returned, please replace this with the merged image

    def intensity_scaling(self, input_image, column, alpha, beta):
        """
        Scale your image intensity.

        input_image: the input image
        column: image column at which left section ends
        alpha: left half scaling constant
        beta: right half scaling constant

        return: output_image
        """

        # add your code here

        newim = input_image.copy()

        icol = np.shape(newim)[1]
        irow = np.shape(newim)[0]

        for i in range(0,irow):
            for j in range(0,icol):
                if j < column:
                    newim[i][j] *= alpha
                if j > column:
                    newim[i][j] *= beta

        # Please do not change the structure
        return newim  # Currently the input image is returned, please replace this with the intensity scaled image

    def centralize_pixel(self, input_image, column):
        """
        Centralize your pixels (do not use np.mean)

        input_image: the input image
        column: image column at which left section ends

        return: output_image
        """

        # add your code here
        icol = np.shape(input_image)[1]
        irow = np.shape(input_image)[0]
        rtotal = 0 #pixel total
        ltotal = 0
        rcount = 0
        lcount = 0

        for i in range (0, irow):
            for j in range(0,icol):
                if(j < column):
                    ltotal += input_image[i][j]
                    lcount += 1
                else:
                    rtotal += input_image[i][j]
                    rcount += 1


        #mean calculation

        lmean = int(ltotal) / int(lcount)
        print(lmean)
        rmean = int(rtotal) / int(rcount)
        print(rmean)

        #offset calculation

        loffset = 128 - lmean
        roffset = 128 - rmean

        #adding offset to every pixel

        noffset = 0

        for i in range(0, irow):
            for j in range(0, icol):
                if j <= column:
                    noffset = input_image[i][j] + loffset
                    if(noffset < 0):
                        input_image[i][j] = 0
                    elif(noffset > 255):
                        input_image[i][j] = 255
                    else:
                        input_image[i][j] = noffset
                if j > column:
                    noffset = input_image[i][j] + roffset
                    if (noffset < 0):
                        input_image[i][j] = 0
                    elif (noffset > 255):
                        input_image[i][j] = 255
                    else:
                        input_image[i][j] = noffset


        return input_image   # Currently the input image is returned, please replace this with the centralized image
