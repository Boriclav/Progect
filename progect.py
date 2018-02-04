wi = int(input())
print('input einbishen')
ei = int(input())
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
for i in range(lt + 1): 
	A[i][0] = i * st
#print(A)
for j in range(ls + 1):
	A[0][j] = j * st
#print(A)
for i in range(1, lt):
	for j in range(1, ls):
		if s[i-1] == t[j-1]:
			A[i][j] = max (A[i - 1][j] + st, A[i-1][j-1] + wi, A[i][j - 1] + st)
		else:
			A[i][j] = max (A[i - 1][j] + st, A[i-1][j-1] + ei, A[i][j - 1] + st)
print(A)

