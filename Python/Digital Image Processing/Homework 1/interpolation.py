import math


class interpolation:

    def linear_interpolation(self, image, rotated_image, inv_rot_mat, O, rows, cols):
        """Computes the linear interpolation value at some iD location x between two 1D points (Pt1 and Pt2).
        
        There are no arguments defined in the function definition on purpose. It is left upto the student to define any requierd arguments.
        Please change the signature of the function and add the arguments based on your implementation.
        
        The function ideally takes two 1D points Pt1 and Pt2, and their intensitites I(Pt1), I(Pt2).
        return the interpolated intensity value (I(x)) at location x """

        # Write your code for linear interpolation here

        for i in range(rotated_image.shape[0]):
            for j in range(rotated_image.shape[1]):
                ip = int(i) - O[0]
                jp = int(j) - O[1]

                io = int(inv_rot_mat[0][0] * ip + inv_rot_mat[0][1] * jp)
                jo = int(inv_rot_mat[1][0] * ip + inv_rot_mat[1][1] * jp)

                if(io >= 0 and jo >= 0 and math.ceil(io) < rows and math.ceil(jo) < cols):
                    neighbor = (round(io), round(jo))
                    rotated_image[i][j] = image[neighbor]

        return rotated_image

    def bilinear_interpolation(self, image, rotated_image, inv_rot_mat, O, rows, cols):
        """Computes the bilinear interpolation value at some 2D location x between four 2D points (Pt1, Pt2, Pt3, and Pt4).

        There are no arguments defined in the function definition on purpose. It is left upto the student to define any requierd arguments.
        Please change the signature of the function and add the arguments based on your implementation.
        
        The function ideally takes four 2D points Pt1, Pt2, Pt3, and Pt4, and their intensitites I(Pt1), I(Pt2), I(Pt3), and I(Pt4).
        return the interpolated intensity value (I(x)) at location x """

        # Write your code for bilinear interpolation here
        # Recall that bilinear interpolation performs linear interpolation three times
        # Please reuse or call linear interpolation method three times by passing the appropriate parameters to compute this task
        one = interpolation.linear_interpolation(self, image, rotated_image, inv_rot_mat, O, rows, cols)
        two = interpolation.linear_interpolation(self, image, one, inv_rot_mat, O, rows, cols)
        three = interpolation.linear_interpolation(self, image, two, inv_rot_mat, O, rows, cols)

        return three #if bilinear is just linear interpolation 3 times then this is bilinear
