
import sys
from math import cos, sin, radians

# Create a string with spaces proportional to a cosine of x in degrees
# Create a string with spaces proportional to a cosine of x in degrees
def make_dot_string(x):
    rad = radians(x)                             # cos works with radians
    numspaces = int(20 * cos(radians(x)) + 20)   # scale to 0-40 spaces
    str = ' ' * numspaces + 'o'                  # place 'o' after the spaces
    return str

def main():
    for i in range(360):
        s=make_dot_string(i)
        print(s)

 
main()

