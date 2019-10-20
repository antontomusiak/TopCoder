'''
Problem Statement
    
Computers tend to store dates and times as single numbers which represent the number of seconds or milliseconds since a particular date. 
Your task in this problem is to write a method whatTime, which takes an integer, seconds, representing the number of seconds since midnight
on some day, and returns a string formatted as "<H>:<M>:<S>". Here, <H> represents the number of complete hours since midnight, 
<M> represents the number of complete minutes since the last complete hour ended, and <S> represents the number of seconds since the 
last complete minute ended. Each of <H>, <M>, and <S> should be an integer, with no extra leading 0's. Thus, if seconds is 0, you should 
return "0:0:0", while if seconds is 3661, you should return "1:1:1".

Definition
    
Class:
Time
Method:
whatTime
Parameters:
integer
Returns:
string
Method signature:
def whatTime(self, seconds):
'''

# Solution:
class Time:
	def whatTime(self, seconds):
		h = seconds/3600
		m = (seconds%3600) / 60
		s = seconds - h * 3600 - m * 60
		
		time = str(h)+ ':' + str(m) + ':' + str(s)
		return time  
