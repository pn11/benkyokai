import numpy as np

N = int(input())
x0, y0 = [float(x) for x in input().split()]
xm, ym = [float(x) for x in input().split()]

p0 = np.array([[x0],[y0]])
pm = np.array([[xm],[ym]])
pc = 0.5 * (p0+pm)
#print(p0, pm, pc)
r = np.linalg.norm(p0-pc)

theta = np.radians(360/N)
c, s = np.cos(theta), np.sin(theta)
R = np.array(((c, -s), (s, c)))

ans = pc + R.dot(p0-pc)
print(ans[0,0], ans[1,0])
