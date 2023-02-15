import cv2

class CellCounting:
   def __init__(self):
       pass

   def blob_coloring(self, image):
       """Implement the blob coloring algorithm
       takes a input:
       image: binary image
       return: a list/dict of regions"""
       rows = image.shape[0]
       cols = image.shape[1]

       s = [[0] * cols for _ in range(rows)]
       k = 1
       regions = dict()

       for r in range (0, rows):
           for c in range(0, cols):
               if(r == 0 and c == 0):
                   if(image[r][c] == 0):
                       s[r][c] = k
                       k += 1
               elif(r == 0):
                   if(image[r][c] == 0 and image[r][c-1] == 0):
                       s[r][c] = s[r][c-1]
               elif(c == 0):
                   if(image[r][c] == 0 and image[r-1][c] == 0):
                       s[r][c] = s[r-1][c]
               else:
                   if(image[r][c] == 0 and image[r][c-1] == 255 and image[r-1][c] == 255):
                       s[r][c] = k
                       k += 1
                   if(image[r][c] == 0 and image[r][c-1] == 255 and image[r-1][c] == 0):
                       s[r][c] = s[r-1][c]
                   if(image[r][c] == 0 and image[r][c-1] == 0 and image[r-1][c] == 255):
                       s[r][c] = s[r][c-1]
                   if(image[r][c] == 0 and image[r][c-1] == 0 and image[r-1][c] == 0):
                       s[r][c] = s[r-1][c]
                       if(s[r][c-1] != s[r-1][c]):
                           for i in range(0, r):
                               for j in range (0,c):
                                   if s[i][j] == s[r][c-1]:
                                       s[i][j] = s[r-1][c]
       for r in range(0,len(s)):
           for c in range(len(s[0])):
               if(s[r][c] in regions.keys() and s[r][c] != 0):
                   regions.setdefault(s[r][c], []).append([r,c])
               elif(s[r][c] != 0):
                   regions[s[r][c]] = [[r,c]]

       return regions

   def compute_statistics(self, region):
       """Compute cell statistics area and location
       takes as input
       region: a list/dict of pixels in a region
       returns: region statistics"""

       total = 0
       stats = []

       for k in region.keys():
           if(len(region[k]) > 15):
               area = len(region[k])
               num = region[k]
               i = 0
               j = 0
               total += 1
               for coordinates in num:
                   i += coordinates[0]
                   j += coordinates[1]
               i /= len(region[k])
               j /= len(region[k])
               cent = (int(i), int(j))
               stats.append([total,area,cent])
               print("Region: ", total, " Area: ", area, " Centroid: ", cent)

       # Please print your region statistics to stdout
       # <region number>: <location or center>, <area>
       # print(stats)

       return stats

   def mark_image_regions(self, image, stats):
       """Creates a new image with computed stats
       takes as input
       image: a list of pixels in a region
       stats: stats regarding location and area
       returns: image marked with center and area"""
       for line in stats:
           area = str(line[1])
           cent = line[2]
           font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
           color = (255, 0, 0)
           image = cv2.putText(image, "*", (cent[0], cent[1]), font, 0.25, color, 2)
           image = cv2.putText(image, area, (cent[0] + 2, cent[1] + 2), font, 0.3, color, 2)

       return image


