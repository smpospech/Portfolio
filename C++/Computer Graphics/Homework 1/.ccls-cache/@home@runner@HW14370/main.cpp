#include "BMP.h"
#include <cmath>
#include <iostream>

using namespace std;

int main() {

  int x0 = 768;
  int y0 = 384;

  BMP bmpNew(1000, 1000, false);
  bmpNew.fill_region(0, 0, 200, 200, 0, 0, 0, 0);
  for (int i = 0; i < bmpNew.bmp_info_header.width; i++) {
    bmpNew.set_pixel(i, (sqrt((x0 + i) * (x0 - i)) / 2) + 500, 255, 255, 255, 0); //plotting the original for solving the y
    bmpNew.set_pixel(i, (-sqrt((x0 + i) * (x0 - i)) / 2) + 500, 255, 255, 255, 0); // the negative
  }
  bmpNew.write("output.bmp");
}
