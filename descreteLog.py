import math
import sys
p=14222331744261730109
q=6549179332223292769
message=5
e=7
N=p*q
Cipher=(message**e) % N
print ('Message=',message)
print ('N=',N)
print ('e=',e)
print ('Cipher=',Cipher)
print ('=============='Message = 10**(math.log10(Cipher)/e))
print ('Message is:',int(round(Message)), ' Calculated from log10(Cipher/e)')
if ((message**e) > N):
	print ('Method will not work as M^e is larger than N')
