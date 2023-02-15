# For this part of the assignment, You can use inbuilt functions to compute the fourier transform
# You are welcome to use fft that are available in numpy and opencv

import numpy as np


class Filtering:

    def __init__(self, image):
        """initializes the variables frequency filtering on an input image
        takes as input:
        image: the input image
        """
        self.image = image
        self.mask = self.get_mask

    def get_mask(self, shape):
        """Computes a user-defined mask
        takes as input:
        shape: the shape of the mask to be generated
        rtype: a 2d numpy array with size of shape
        """

        #within my filter function

        return np.zeros(shape)

    def post_process_image(self, image):
        """Post processing to display DFTs and IDFTs
        takes as input:
        image: the image obtained from the inverse fourier transform
        return an image with full contrast stretch
        -----------------------------------------------------
        You can perform post processing as needed. For example,
        1. You can perfrom log compression
        2. You can perfrom a full contrast stretch (fsimage)
        3. You can take negative (255 - fsimage)
        4. etc.
        """

        rows = image.shape[0]
        cols = image.shape[1]

        result = np.zeros((image.shape))

        big = 0
        smol = 255

        for r in range(rows):
            for c in range(cols):
                if image[r, c] > big:
                    big = image[r, c]
                if image[r, c] < smol:
                    smol = image[r, c]

        for r in range(rows):
            for c in range(cols):
                result[r, c] = int((255/(big-smol)) * (image[r, c]-smol) + .5)

        return result

    def filter(self):
        """Performs frequency filtering on an input image
        returns a filtered image, magnitude of DFT, magnitude of filtered DFT
        ----------------------------------------------------------
        You are allowed to used inbuilt functions to compute fft
        There are packages available in numpy as well as in opencv
        Steps:
        1. Compute the fft of the image
        2. shift the fft to center the low frequencies
        3. get the mask (write your code in functions provided above) the functions can be called by self.filter(shape)
        4. filter the image frequency based on the mask (Convolution theorem)
        using ideal low pass filters
        5. compute the inverse shift
        6. compute the inverse fourier transform
        7. compute the magnitude
        8. You will need to do post processing on the magnitude and depending on the algorithm (use post_process_image to write this code)
        Note: You do not have to do zero padding as discussed in class, the inbuilt functions takes care of that
        filtered image, magnitude of DFT, magnitude of filtered DFT: Make sure all images being returned have grey scale full contrast stretch and dtype=uint8"""

        image2 = self.image.copy()
        fft = np.fft.fft2(image2)

        fft = np.fft.fftshift(fft)
        mag = 15*np.log(np.abs(fft))

        h = np.zeros((fft.shape))
        for i in range(h.shape[0]):
            for j in range(h.shape[1]): # every point below was hardcoded to place perfectly on the filtered dft
                a = np.sqrt(((i - h.shape[0] / 2 + h.shape[0] / 2 - 282) ** 2) + ((j - h.shape[1] / 2 + h.shape[1] / 2 - 213) ** 2))
                b = np.sqrt(((i - h.shape[0] / 2 - h.shape[0] / 2 - 282) ** 2) + ((j - h.shape[1] / 2 - h.shape[1] / 2 - 213) ** 2))
                c = np.sqrt(((i - h.shape[0] / 2 + h.shape[0] / 2 - 230) ** 2) + ((j - h.shape[1] / 2 + h.shape[1] / 2 - 299) ** 2))
                d = np.sqrt(((i - h.shape[0] / 2 - h.shape[0] / 2 - 230) ** 2) + ((j - h.shape[1] / 2 - h.shape[1] / 2 - 299) ** 2))
                e = np.sqrt(((i - h.shape[0] / 2 + h.shape[0] / 2 - 272) ** 2) + ((j - h.shape[1] / 2 + h.shape[1] / 2 - 276) ** 2))
                f = np.sqrt(((i - h.shape[0] / 2 - h.shape[0] / 2 - 272) ** 2) + ((j - h.shape[1] / 2 - h.shape[1] / 2 - 276) ** 2))
                g = np.sqrt(((i - h.shape[0] / 2 + h.shape[0] / 2 - 240) ** 2) + ((j - h.shape[1] / 2 + h.shape[1] / 2 - 236) ** 2))
                s = np.sqrt(((i - h.shape[0] / 2 - h.shape[0] / 2 - 240) ** 2) + ((j - h.shape[1] / 2 - h.shape[1] / 2 - 236) ** 2))
                if a <= 5 or b <= 5 or c <= 5 or d <= 5 or e <= 5 or f <= 5 or g <= 5 or s <= 5:
                    h[i, j] = 0.0
                else:
                    h[i, j] = 1.0
        filtered = fft * h
        shift = np.fft.ifftshift(filtered)
        ifft = np.fft.ifft2(shift)
        result = self.post_process_image(ifft)
        return [result, mag, mag * h]


