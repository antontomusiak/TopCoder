import math

class TriangleMaking:
	def maxPerimeter(self, a, b, c):
		t_s = sorted(list([a, b, c]), reverse = True)
		for i in range(t_s[0], 0, -1):
			for angle in range(179, 0, -1):
				tmp = math.sqrt(i * i + t_s[1]*t_s[1] - 2*i*t_s[1]*math.cos(math.pi/180*angle))
				if math.ceil(tmp) <= t_s[2]: return math.ceil(tmp) + i + t_s[1]