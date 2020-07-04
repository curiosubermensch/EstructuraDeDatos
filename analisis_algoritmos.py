import time

def sumatoria(n):
	t_inicio=time.time()
	suma=0
	for i in range(1,n+1): #maxima eficiencia por eso parte del 1
		suma+=i
	
	t_final=time.time()
	return suma,t_final-t_inicio

print(sumatoria(10000))