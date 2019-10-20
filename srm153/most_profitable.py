class MostProfitable:
	def bestItem(self, costs, prices, sales, items):
		profit = []
		for i in range(len(costs)):
			profit.append((prices[i]-costs[i])*sales[i])
			
		
		if all([x <= 0 for x in profit]): return ''
		return items[profit.index(max(profit))]