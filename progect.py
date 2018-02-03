# Heir durfe wir ändern diese Mothode fur nuclear hochladenz
s = 'gatta'
t = 'gaattc' # We input 2  chains of nuclear
print('input straffe')
st = int(input())
print('input winner')
wi = int(input())
print('input einbishen')
ei = int(input())
s = s.split()
s = list(''.join(s))
t = t.split()
t = list(''.join(t)) 
ls = len(s)
lt = len(t)
A = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
for i in range(ls):
	A[i][0] = i * st
for j in range(lt):
	A[0][j] = j * st
for i in range(1, ls):
	for j in range(1, lt):
		if s[i-1] == t[j-1]:
			A[i][j] = max (A[i - 1][j] + st, A[i-1][j-1] + wi, A[i][j - 1] + st)
		else:
			A[i][j] = max (A[i - 1][j] + st, A[i-1][j-1] + ei, A[i][j - 1] + st)
print(A)
