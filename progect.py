# Heir durfe wir ändern diese Mothode fur nuclear hochladenz
k = 0
l = 0
s = 'gatta'
t = 'gaattc' # We input 2  chains of nuclear
print('input straffe')
st = -2 #int(input())
print('input winner')
wi = 2 #int(input())
print('input einbishen')
ei = -1 #int(input())
s = s.split()
s = list(''.join(s))
t = t.split()
t = list(''.join(t)) 
ls = len(s)
lt = len(t) # j ist Linie, i ist Kolonne
A = [[0,0,0,0,0,0],
	 [0,0,0,0,0,0],
	 [0,0,0,0,0,0],
	 [0,0,0,0,0,0],
	 [0,0,0,0,0,0],
	 [0,0,0,0,0,0],
	 [0,0,0,0,0,0]]
for i in range(lt+1):
	A[i][0] = i * st
	#l +=1
#print(A)
for j in range(ls+1):
	A[0][j] = j * st
	#k +=1
#print(A)
for j in range(1, ls+1):
	k +=1
	for i in range(1, lt+1):
		l += 1
		if s[j-1] == t[j-1]:
			A[i][j] = max (A[i - 1][j] + st, A[i-1][j-1] + wi, A[i][j - 1] + st)
		else:
			A[i][j] = max (A[i - 1][j] + st, A[i-1][j-1] + ei, A[i][j - 1] + st)
		#print(A)
for r in A:
	print(r)

#print(A[2][2])
print('k=', k)
print('l=', l)
# j ist Linie, i ist Kolonne
