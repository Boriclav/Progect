
# Heir durfe wir ändern diese Mothode fur nuclear hochladenz
s = 'gatta'
t = 'gaattc' # We input 2  chains of nuclear
#print('input straffe')
st = -2 #int(input())
#print('input winner')
wi = 2 #int(input())
#print('input einbishen')
ei = -1 #int(input())
s = s.split()
s = list(''.join(s))
t = t.split()
t = list(''.join(t)) 
ls = len(s)
lt = len(t) # j ist Linie, i ist Kolonne
aat = '0'
aas = '0' 
for i in range (lt+1):
	
p = [[0,0,0,0,0,0],
	 [0,0,0,0,0,0],
	 [0,0,0,0,0,0],
	 [0,0,0,0,0,0],
	 [0,0,0,0,0,0],
	 [0,0,0,0,0,0],
	 [0,0,0,0,0,0]]
A = [[0,0,0,0,0,0],
	 [0,0,0,0,0,0],
	 [0,0,0,0,0,0],
	 [0,0,0,0,0,0],
	 [0,0,0,0,0,0],
	 [0,0,0,0,0,0],
	 [0,0,0,0,0,0]]
B = A
for i in range(lt+1):
	A[i][0] = i * st
	#l +=1
#print(A)
for j in range(ls+1):
	A[0][j] = j * st
	#k +=1
#print(A)
for j in range(1, ls+1):
	#k +=1
	for i in range(1, lt+1):
		#l += 1
		if s[j-1] == t[i-1]:
			A[i][j] = max (A[i - 1][j] + st, A[i-1][j-1] + wi, A[i][j - 1] + st)
			a1 = A[i - 1][j] + st
			a2 = A[i-1][j-1] + wi
			a3 = A[i][j - 1] + st
			if a1 > a2 and a1 > a3:
				p[i][j]= 'l'+ ' ' + str(a1) + ' '+ str(a2) + ' ' +str(a3) #L - max from Left 
			elif a2 > a1 and a2 > a3:
				p[i][j]= 'd'+ ' ' + str(a1) + ' '+ str(a2) + ' ' +str(a3) #D - max from Diagonal 
			elif a3 > a1 and a3 > a2: 
				p[i][j]= 'u'+ ' ' + str(a1) + ' '+ str(a2) + ' ' +str(a3) #U - max from Up
			elif a1 == a2 and a1 > a3: 
				p[i][j]= 'ld'+ ' ' + str(a1) + ' '+ str(a2) + ' ' +str(a3)
			elif a2 == a3 and a2 > a1:
				p[i][j]= 'du'+ ' ' + str(a1) + ' '+ str(a2) + ' ' +str(a3)
			else:
				p[i][j]= 'ul'+ ' ' + str(a1) + ' '+ str(a2) + ' ' +str(a3)
		else:
			A[i][j] = max (A[i - 1][j] + st, A[i-1][j-1] + ei, A[i][j - 1] + st)
			a1 = A[i - 1][j] + st
			a2 = A[i-1][j-1] + ei
			a3 = A[i][j - 1] + st
			if a1 > a2 and a1 > a3:
				p[i][j]= 'l'+ ' ' + str(a1) + ' '+ str(a2) + ' ' +str(a3)#L - max from Left 
			elif a2 > a1 and a2 > a3:
				p[i][j]= 'd'+ ' ' + str(a1) + ' '+ str(a2) + ' ' +str(a3) #D - max from Diagonal 
			elif a3 > a1 and a3 > a2: 
				p[i][j]= 'u'+ ' ' + str(a1) + ' '+ str(a2) + ' ' +str(a3) #U - max from Up
			elif a1 == a2 and a1 > a3: 
				p[i][j]= 'ld'+ ' ' + str(a1) + ' '+ str(a2) + ' ' +str(a3)
			elif a2 == a3 and a2 > a1:
				p[i][j]= 'du'+ ' ' + str(a1) + ' '+ str(a2) + ' ' +str(a3)
			else:
				p[i][j]= 'ul'+ ' ' + str(a1) + ' '+ str(a2) + ' ' +str(a3)
		#print(A)
for r in A:
	print(r)
for g in p:
	print(g)
	
