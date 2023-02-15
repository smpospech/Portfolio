import numpy as np

class Filtering:

    def __init__(self, image, filter_name, filter_size, var = None):
        """initializes the variables of spatial filtering on an input image
        takes as input:
        image: the noisy input image
        filter_name: the name of the filter to use
        filter_size: integer value of the size of the fitler
        global_var: noise variance to be used in the Local noise reduction filter
        S_max: Maximum allowed size of the window that is used in adaptive median filter
        """

        self.image = image

        if filter_name == 'arithmetic_mean':
            self.filter = self.get_arithmetic_mean
        elif filter_name == 'geometric_mean':
            self.filter = self.get_geometric_mean
        if filter_name == 'local_noise':
            self.filter = self.get_local_noise
        elif filter_name == 'median':
            self.filter = self.get_median
        elif filter_name == 'adaptive_median':
            self.filter = self.get_adaptive_median

        self.filter_size = filter_size
        self.global_var = var
        self.S_max = 15

    def get_arithmetic_mean(self, roi):
        """Computes the arithmetic mean of the input roi
        takes as input:
        roi: region of interest (a list/array of intensity values)
        returns the arithmetic mean value of the roi"""
        arithMean = 0
        meanSum = 0

        for i in roi:
            meanSum = meanSum + i
        arithMean = meanSum / (self.filter_size * self.filter_size)

        return arithMean

    def get_geometric_mean(self, roi):
        """Computes the geometric mean for the input roi
        takes as input:
        roi: region of interest (a list/array of intensity values)
        returns the geometric mean value of the roi"""
        meanMult = 1

        for i in roi:
            meanMult = meanMult * i #all of the intensities multiplied by each other
        geoMean = meanMult ** (1 / (len(roi)))#formula for geometric mean the nth root of the insitiies multiplied

        return geoMean

    def get_local_noise(self, roi):
        """Computes the local noise reduction value
        takes as input:
        roi: region of interest (a list/array of intensity values)
        returns the local noise reduction value of the roi"""

        localNoise = 0
        globalVar = self.global_var
        nPix = int(len(roi)/2)
        localMean = self.get_arithmetic_mean(roi)
        localVar = sum((i - localMean) ** 2 for i in roi) / len(roi)

        localNoise = roi[nPix] - ((globalVar / localVar) * (roi[nPix] - localMean))

        return localNoise

    def get_median(self, roi):
        """Computes the median for the input roi
        takes as input:
        roi: region of interest (a list/array of intensity values)
        returns the median value of the roi"""

        sortedList = sorted(roi)
        indicator = False
        mid = int(len(roi) / 2)

        if((len(roi) % 2) == 1): #length is odd
            indicator = True
        else: #length is even
            indicator = False

        if(indicator is True):
            listMed = sortedList[mid]
        elif(indicator is False):
            listMed = (sortedList[mid] + sortedList[mid+1]) / 2

        return listMed


    def get_adaptive_median(self, roi):
        """Use this function to implment the adaptive median.
        It is left up to the student to define the input to this function and call it as needed. Feel free to create
        additional functions as needed.
        """
        Zmin = np.min(roi)
        Zmax = np.max(roi)
        Zmed = self.get_median(roi)
        i = roi[int(len(roi)/2)]
        window = self.filter_size

        while True:
            A1 = Zmed - Zmin
            A2 = Zmed - Zmax

            if(A1 > 0 and A2 < 0):
                B1 = i - Zmin
                B2 = i - Zmax
                if(B1 > 0 and B2 > 0):
                    return i
                else:
                    return Zmed
            else:
                window += 1
                if(window <= self.S_max):
                    continue
                else:
                    return Zmed

    def filtering(self):
        """performs filtering on an image containing gaussian or salt & pepper noise
        returns the denoised image
        ----------------------------------------------------------
        Note: Here when we perform filtering we are not doing convolution.
        For every pixel in the image, we select a neighborhood of values defined by the kernal and apply a mathematical
        operation for all the elements with in the kernel. For example, mean, median and etc.

        Steps:
        1. add the necesssary zero padding to the noisy image, that way we have sufficient values to perform the operati
        ons on the pixels at the image corners. The number of rows and columns of zero padding is defined by the kernel size
        2. Iterate through the image and every pixel (i,j) gather the neighbors defined by the kernel into a list (or any data structure)
        3. Pass these values to one of the filters that will compute the necessary mathematical operations (mean, median, etc.)
        4. Save the results at (i,j) in the ouput image.
        5. return the output image

        Note: You can create extra functions as needed. For example if you feel that it is easier to create a new function for
        the adaptive median filter as it has two stages, you are welcome to do that.
        For the adaptive median filter assume that S_max (maximum allowed size of the window) is 15
        """
        rows = self.image.shape[0]
        cols = self.image.shape[1]

        filtered_image = self.image.copy()
        pads = int(self.filter_size / 2)
        lower = -pads
        upper = pads + 1

        for x in range(pads, rows-pads):
            for y in range(pads, cols-pads):
                temp = []
                for i in range(lower, upper):
                    for j in range(lower, upper):
                        temp.append(self.image[x+i][y+j])
                filtered_image[x][y] = self.filter(temp)

        return filtered_image