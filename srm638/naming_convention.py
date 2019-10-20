class NamingConvention:
	def toCamelCase(self, variableName):
		v_l = variableName.split('_')
		cam = v_l[0]
		for i in range(1, len(v_l)):
			cam += v_l[i].capitalize()
		
		return cam