class TaxTable:
	def income(self, taxAmount):
		if taxAmount < 18475:
			return -1
		if taxAmount >= 18475 and taxAmount < 22787.5:
			return round(float(taxAmount + 6525) / .25)
		if taxAmount >= 22787.5 and taxAmount < 39980:
			return round(float(taxAmount + 10042.5) / .28)
		if taxAmount >= 39980 and taxAmount < 86328:
			return round(float(taxAmount + 18975) / .33)
		else:
			return round(float(taxAmount + 25357) / .35)