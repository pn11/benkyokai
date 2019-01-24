import pptk

xyz = pptk.rand(100, 3)
v = pptk.viewer(xyz)
v.set(point_size=0.005)
v.capture('screenshot1.png')

rgb = pptk.rand(100, 3)
v = pptk.viewer(xyz, rgb)
v.set(point_size=0.005)

rgb1 = pptk.rand(100, 3)
rgb2 = pptk.rand(100, 3)
v = pptk.viewer(xyz, rgb1, rgb2)
v.set(point_size=0.005)


import numpy as np
from PIL import Image
import pptk

imgs = [Image.open(fname) for fname in ['wanihakase.jpg', 'sugamon.jpg','okazaki.jpg']]
rows, cols = imgs[0].size

pts = [[r/1.414, c, -r/1.414] for  r in range(rows) for c in range(cols)]
v = pptk.viewer(pts)

colors = [np.array(img.getdata())/255 for img in imgs]
v.attributes(*colors)
