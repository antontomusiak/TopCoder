class BuyingTshirts:
	def meet(self, T, Q, P):
		Q_earn, P_earn = 0, 0
		q = []
		p = []
		for i in range(len(Q)):
			Q_earn += Q[i]
			P_earn += P[i]
			if Q_earn >= T:
				q.append(i)
				Q_earn -= T
			if P_earn >= T:
				p.append(i)
				P_earn -= T
		days = 0
		for d in q:
			if d in p: days += 1
		
		return days