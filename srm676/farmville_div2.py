class FarmvilleDiv2:
	def minTime(self, time, cost, budget):
		p = [[cost[i], time[i]] for i in range(len(time))]
		p = sorted(p, key = lambda x: x[0])
		for i in range(len(p)):
			current_time = min(budget // p[i][0], p[i][1])
			budget -= current_time * p[i][0]
			p[i][1] -= current_time
			
				
		return sum([x[1] for x in p])