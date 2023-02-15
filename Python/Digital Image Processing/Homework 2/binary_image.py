class BinaryImage:
    def __init__(self):
        pass

    def compute_histogram(self, image):
        """Computes the histogram of the input image
        takes as input:
        image: a grey scale image
        returns a histogram as a list"""

        rows = image.shape[0]
        cols = image.shape[1]
        hist = [0] * 256

        for i in range(0, rows):
            for j in range(0, cols):
                intensity = image[i,j]
                hist[intensity] += 1

        return hist

    def find_otsu_threshold(self, hist):
        """analyses a histogram it to find the otsu's threshold assuming that the input hstogram is bimodal histogram
        takes as input
        hist: a bimodal histogram
        returns: an optimal threshold value (otsu's threshold)"""
        threshold = 0
        pixels = 0
        prob = [0] * 256

        for x in hist:
            pixels += x

        for i in range(len(hist)): #compute probabilities
            prob[i] = (hist[i] / sum(hist))

        threshold_holder = {}

        for t in range(0,255):
            q1, q2 = 0, 0
            u1t, u2t = 0, 0
            u1v, u2v = 0, 0
            o1, o2 = 0, 0

            for i in range(0, t):
                q1 += prob[i]
                u1v += i * hist[i]
                u1t += hist[i]
            q1 /= pixels
            if(u1t > 0):
                u1 = u1v / u1t
                for x in range(0,t):
                    o1 += (((x - u1) ** 2) * hist[x])
            if(u1t > 0):
                o1 /= u1t

            for i in range(t+1, 255):
                q2 += prob[i]
                u2v += i * hist[i]
                u2t += hist[i]
            q2 /= pixels
            if(u2t > 0):
                u2 = u2v / u2t
                for x in range(t + 1, 255):
                    o2 += (((x - u2) ** 2) * hist[x])
            if(u2t > 0):
                o2 /= u2t
                within = q1 * o1 + q2 * o2
                threshold_holder[t] = within
        threshold = min(threshold_holder.keys(), key=(lambda k: threshold_holder[k]))

        return threshold

    def binarize(self, image):
        """Computes the binary image of the input image based on histogram analysis and thresholding
        take as input
        image: a grey scale image
        returns: a binary image"""

        rows = image.shape[0]
        cols = image.shape[1]
        hist = self.compute_histogram(image)
        threshold = self.find_otsu_threshold(hist)
        bin_img = image.copy()
        for i in range(0, rows):
            for j in range(0, cols):
                if(image[i][j] < threshold):
                    bin_img[i][j] = 255
                else:
                    bin_img[i][j] = 0

        return bin_img
