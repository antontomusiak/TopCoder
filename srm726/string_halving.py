#Problem: 250
#Test Case: 7
#Succeeded: No
#Execution Time: 56 ms
#Peak memory used: 24,535MB
#Args:
#{"yckhtbgxpexorqidshtfuvakabynqdpluoslmvgjcmwijfnwre"}

#Expected:
#"b"

#Received:
#"a"

dd = "yckhtbgxpexorqidshtfuvakabynqdpluoslmvgjcmwijfnwre"

#class StringHalving:
def lexsmallest(s):
	a = len(s)/2
	b = len(s)
	c = s[:a]
	for i in range((a-1)):
		if (s[i] == s[i+1]): return s[i]
		
	return min(c)

ddd = lexsmallest(dd)

print(ddd)

		
