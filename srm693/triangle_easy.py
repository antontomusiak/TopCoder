class TriangleEasy:
	def find(self, n, x, y):
		g = [[False for j in range(n)] for i in range(n)]
		for i in range(len(x)):
			g[x[i]][y[i]] = True
			g[y[i]][x[i]] = True
		
		res = 3
		for i in range(n):
			for j in range(i+1, n):
				for k in range(j+1, n):
					connected = 0
					if g[i][j]: connected += 1
					if g[i][k]: connected += 1
					if g[j][k]: connected += 1
					res = min(res, 3 - connected) 
		return res