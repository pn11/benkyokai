import numpy as np
from PIL import Image
import pptk

def plot_points():
    pts = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    v = pptk.viewer(pts)    
    v.set(point_size=0.01)
    labels = [1, 2, 3]
    colors = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    ii = [1, 2, 3]
    v.attributes(colors, ii, labels)

def plot_images():
    img = Image.open("cat.png")
    rows, cols = img.size
    
    pts = []
    for r in range(rows):
        for c in range(cols):
            pts.append([r/1.414, c, -r/1.414])
    
    v = pptk.viewer(pts)
    colors = np.array(img.getdata())/255
    v.attributes(colors)

    
if __name__ == "__main__":
    #plot_points()
    plot_images()
