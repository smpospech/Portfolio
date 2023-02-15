import math

from .interpolation import interpolation
import numpy as np
import cv2

class Geometric:
    def __init__(self):
        pass

    def forward_rotate(self, image, theta):
        """Computes the forward rotated image by an angle theta
                image: input image
                theta: angle to rotate the image by (in radians)
                return the rotated image"""
        rows = image.shape[0]
        cols = image.shape[1]

        TL, BL, TR, BR = ([0, 0]), ([rows, 0]), ([0, cols]), ([rows, cols])
        og_corners = [TL,BL,TR,BR]

        rotated_matrix = np.array([(math.cos(theta), -math.sin(theta)),(math.sin(theta), math.cos(theta))])
        rotated_corners = []

        for a in og_corners:
            holder = a
            xp = rotated_matrix[0][0] * a[0] + rotated_matrix[0][1] * a[1]
            yp = rotated_matrix[1][0] * a[0] + rotated_matrix[1][1] * a[1]
            holder = (xp,yp)
            rotated_corners.append(holder)

        minx = min(x[0] for x in rotated_corners)
        miny = min(y[1] for y in rotated_corners)
        maxx = max(x[0] for x in rotated_corners)
        maxy = max(y[1] for y in rotated_corners)

        newrows = int(maxx - minx)
        newcols = int(maxy - miny)
        rotated_image = np.zeros((newrows,newcols))

        for i in range(rows):
            for j in range(cols):
                newX = int(((i * math.cos(theta)) - (j * math.sin(theta))) - minx)
                newY = int(((i * math.sin(theta)) + (j * math.cos(theta))) - miny)

                if(newX >= rotated_image.shape[0]):
                    continue
                elif(newY >= rotated_image.shape[1]):
                    continue
                else:
                    rotated_image[newX][newY] = image[i][j]

        return rotated_image

    def reverse_rotation(self, rotated_image, theta, origin, original_shape):
        """Computes the reverse rotated image by an angle theta
                rotated_image: the rotated image from previous step
                theta: angle to rotate the image by (in radians)
                Origin: origin of the original image with respect to the rotated image
                Original shape: Shape of the orginal image
                return the original image"""

        inverse_rot_mat = np.array([[math.cos(theta), math.sin(theta)], [-math.sin(theta), math.cos(theta)]])

        original = np.zeros((original_shape[0], original_shape[1]))

        for i in range(rotated_image.shape[0]):
            for j in range(rotated_image.shape[1]):
                xp = i - origin[0]
                yp = j - origin[1]

                x = int(inverse_rot_mat[0][0] * xp + inverse_rot_mat[0][1] * yp)
                y = int(inverse_rot_mat[1][0] * xp + inverse_rot_mat[1][1] * yp)

                if(0 <= x < original_shape[0] and 0 <= y < original_shape[1]):
                    original[x][y] = rotated_image[i][j]

        return original

    def rotate(self, image, theta, interpolation_type):
        """Computes the rotated image by an angle theta and perfrom interpolation
                image: the input image
                theta: angle to rotate the image by (in radians)
                interpolation_type: type of interpolation to use (nearest_neighbor, bilinear)
                return the rotated image"""
        rot_mat = np.array([(math.cos(theta), -math.sin(theta)),(math.sin(theta), math.cos(theta))])
        inv_rot_mat = np.array([[math.cos(theta), math.sin(theta)], [-math.sin(theta), math.cos(theta)]])

        rows = image.shape[0]
        cols = image.shape[1]

        TL, BL, TR, BR = ([0, 0]), ([rows, 0]), ([0, cols]), ([rows, cols])
        og_corners = [TL, BL, TR, BR]

        rotated_corners = []

        for a in og_corners:
            holder = a
            xp = rot_mat[0][0] * a[0] + rot_mat[0][1] * a[1]
            yp = rot_mat[1][0] * a[0] + rot_mat[1][1] * a[1]
            holder = (xp, yp)
            rotated_corners.append(holder)

        minx = min(x[0] for x in rotated_corners)
        miny = min(y[1] for y in rotated_corners)
        maxx = max(x[0] for x in rotated_corners)
        maxy = max(y[1] for y in rotated_corners)

        newrows = int(maxx - minx)
        newcols = int(maxy - miny)
        rotated_image = np.zeros((newrows, newcols))

        for i in range(rows):
            for j in range(cols):
                newX = int(((i * math.cos(theta)) - (j * math.sin(theta))) - minx)
                newY = int(((i * math.sin(theta)) + (j * math.cos(theta))) - miny)

                if(newX >= rotated_image.shape[0]):
                    continue
                elif(newY >= rotated_image.shape[1]):
                    continue
                else:
                    rotated_image[newX][newY] = image[i][j]

        O = (-minx, -miny)

        if(interpolation_type == "nearest_neighbor"):
            interpolated = interpolation.linear_interpolation(self, image, rotated_image, inv_rot_mat, O, rows, cols)
        elif(interpolation_type == "bilinear"):
            interpolated = interpolation.bilinear_interpolation(self, image, rotated_image, inv_rot_mat, O, rows, cols)


        return interpolated


