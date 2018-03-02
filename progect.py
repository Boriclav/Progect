# Heir durfe wir ändern diese Mothode fur nuclear hochladenz
print ('Enter 1 nuclears code')
s = input() #'gatta' 
print ('Enter 2 nuclears code')
t = input() #'gaattc' # We input 2  chains of nuclear
print('input straffe')
st = int(input())#-2 
print('input winner')
wi = int(input()) #2 
print('input einbishen')
ei = int(input()) #-1 
s = s.split()
s = list(''.join(s))
t = t.split()
t = list(''.join(t)) 
ls = len(s)
lt = len(t) # j ist Linie, i ist Kolonne
aat = '0'
aas = '0' 
w = []
Т1 = []  #for chain t
S = []   #for chain s
S1 = []  
A = []
P = []
'''
A = [[0,0,0,0,0,0],
	 [0,0,0,0,0,0],
	 [0,0,0,0,0,0],
	 [0,0,0,0,0,0],
	 [0,0,0,0,0,0],
	 [0,0,0,0,0,0],
	 [0,0,0,0,0,0]]
P = [[0,0,0,0,0,0],
	 [0,0,0,0,0,0],
	 [0,0,0,0,0,0],
	 [0,0,0,0,0,0],
	 [0,0,0,0,0,0],
	 [0,0,0,0,0,0],
	 [0,0,0,0,0,0]]
'''
for r in range(lt+1):
	A.append([])
	for c in range(ls+1):
		A[r].append([0])
for q in range(lt+1):
	P.append([])
	for d in range(ls+1):
		P[q].append([0])
for i in range(lt+1):
	A[i][0] = i * st
for j in range(ls+1):
	A[0][j] = j * st
for j in range(1, ls+1):
	for i in range(1, lt+1):
		if s[j-1] == t[i-1]:
			a1 = A[i - 1][j] + st
			a2 = A[i-1][j-1] + wi
			a3 = A[i][j - 1] + st
			A[i][j] = max (a1, a2, a3)
			if a1 > a2 and a1 > a3:
				P[i][j]= 'l' #L - max from Left 
			elif a2 > a1 and a2 > a3:
				P[i][j]= 'd' #D - max from Diagonal 
			elif a3 > a1 and a3 > a2: 
				P[i][j]= 'u'#U - max from Up
			elif a1 == a2 and a1 > a3: 
				P[i][j]= 'ld'
			elif a2 == a3 and a2 > a1:
				P[i][j]= 'du'
			else:
				P[i][j]= 'ul'
		else:
			a1 = A[i - 1][j] + st
			a2 = A[i-1][j-1] + ei
			a3 = A[i][j - 1] + st
			A[i][j] = max (a1, a2, a3)
			if a1 > a2 and a1 > a3:
				P[i][j]= 'l'#L - max from Left 
			elif a2 > a1 and a2 > a3:
				P[i][j]= 'd' #D - max from Diagonal 
			elif a3 > a1 and a3 > a2: 
				P[i][j]= 'u' #U - max from Up
			elif a1 == a2 and a1 > a3: 
				P[i][j]= 'ld'
			elif a2 == a3 and a2 > a1:
				P[i][j]= 'du'
			else:
				P[i][j]= 'ul'
'''
for r in A:
	print(r)
for g in P:
	print(g)
'''
i = lt
j = ls
while i!=0 and	j!=0:
	#global T,S,T1,S1
	if P[i][j] == 'd':
		w.append(t[i-1])
		S.append(s[j-1])
		i -= 1
		j -= 1
	elif P[i][j] == 'u':
		w.append('-')
		S.append(s[j-1])
		j -= 1
	elif P[i][j] == 'l':
		w.append(t[i-1])
		S.append('-')
		i -= 1
	elif P[i][j] == 'du':
		w.append(t[i-1])
		S.append(s[j-1])
		i -= 1
		j -= 1
	elif P[i][j] == 'ld':
		w.append(t[i-1])
		S.append(s[j-1])
		i -= 1
		j -= 1
print('Chain 1:=', w[::-1])
print('Chain 2:=', S[::-1])
