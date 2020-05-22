import numpy as np
import sys
sys.setrecursionlimit(1000000)
def time():
	if not hasattr(time, "counter"):
		time.counter = 0

	time.counter +=1

def dps(v):
	time()
	t[v] = l[v] = time.counter
	for i in adj[v]:
		if visited[i[1]]: continue
		visited[i[1]] = True
		if edges[i[1]][0] == v+1:
			orient.append((v + 1, edges[i[1]][1]))
		else:
			orient.append((v + 1, edges[i[1]][0]))
		next_v = i[0] - 1
		if t[next_v] == -1:
			dps(next_v)
			l[v] = min(l[v],l[next_v])
			if l[next_v] > t[v]:
				cut.append((v+1, next_v+1))
		else:
			l[v] = min(l[v], l[next_v])




with open('test_12.in') as f:

    array = [[int(x) for x in line.split()] for line in f]
adj = [[] for i in range(array[0][0])]
edges = [None] * array[0][1]
orient = []
cut = []

for i in range(1, array[0][1]+1):
	adj[array[i][0]-1].append((array[i][1],i-1))
	adj[array[i][1]-1].append((array[i][0],i-1))
	edges[i-1] = (array[i][0], array[i][1])
t = -np.ones(array[0][0])
l = -np.ones(array[0][0])
visited = [False] * array[0][1]
for j in range(array[0][0]):
	if t[j] == -1:
		dps(j)
if len(cut) != 0:
	print("NO")
	print(len(cut))
	for i in range(len(cut)):
		print(cut[i][0], cut[i][1])
else:
	print("YES")
	print(len(orient))
	for i in range(len(orient)):
		print(orient[i][0], orient[i][1])



