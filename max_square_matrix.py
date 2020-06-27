import numpy as np

def max_square_matrix():
	n=int(input("Enter length of rows: "))
	m=int(input("Enter length of columns: "))
	M= np.random.randint(2, size = (n,m))
	r=len(M)
	c=len(M[0])
	P=np.zeros((r+1,c+1), dtype=int)
	for i in range(1,r):
		for j in range(1,c):
			if M[i][j]==1:
				P[i][j]=min(P[i-1][j-1],P[i-1][j],P[i][j-1]) + 1
			else:
				P[i][j]=0
	max_diag=np.amax(P)
	print("Diagonal length of max square matrix with ones is: ", max_diag)

if __name__=="__main__":
	max_square_matrix()