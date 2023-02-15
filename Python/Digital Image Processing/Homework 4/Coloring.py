import numpy as np

class Coloring:

    def intensity_slicing(self, image, n_slices):
        '''
       Convert greyscale image to color image using color slicing technique.
       takes as input:
       image: the grayscale input image
       n_slices: number of slices
       '''

        rows = image.shape[0]
        cols = image.shape[1]

       #Steps:
        #1. Split the exising dynamic range (0, k-1) using n slices (creates n+1 intervals)
        intervals = np.linspace(0, image.max(), n_slices + 1)

        #2. Randomly assign a color to each interval
        colors = np.random.randint(0, 255, (n_slices, 3))

        #3. Create and output color image
        colored_image = np.zeros((rows, cols, 3), dtype=np.uint8)

        #4. Iterate through the image and assign colors to the color image based on which interval the intensity belongs to
        for i in range(rows):
            for j in range(cols):
                for k in range(n_slices):
                    if(image[i][j] <= intervals[k+1]):
                        colored_image[i,j] = colors[k]
                        break
 
        return colored_image #returns colored image

    def color_transformation(self, image, n_slices, theta):
        '''
        Convert greyscale image to color image using color transformation technique.
        takes as input:
        image:  grayscale input image
        colors: color array containing RGB values
        theta: (phase_red, phase,_green, phase_blue) a tuple with phase values for (r, g, b)
        '''

        rows = image.shape[0]
        cols = image.shape[1]

        # Steps:
        #      1. Split the exising dynamic range (0, k-1) using n slices (creates n+1 intervals)
        intervals = np.linspace(0, 255, n_slices + 1)

        #     2. create red values for each slice using 255*sin(slice + theta[0])
        #       similarly create green and blue using 255*sin(slice + theta[1]), 255*sin(slice + theta[2])
        red = np.array([255 * np.sin(intervals + theta[0])])
        green = np.array([255 * np.sin(intervals + theta[1])])
        blue = np.array([255 * np.sin(intervals + theta[2])])

        #   3. Create and output color image
        colored_image = np.zeros((rows, cols, 3), dtype=np.uint8)

        #  4. Iterate through the image and assign colors to the color image based on which interval the intensity belongs to
        for i in range(rows):
            for j in range(cols):
                for k in range(n_slices):
                    if(intervals[k] <= image[i][j] < intervals[k+1]):
                        colored_image[i][j][0] = red[0][k]
                        colored_image[i][j][1] = green[0][k]
                        colored_image[i][j][2] = blue[0][k]

        return colored_image # returns colored image



        

