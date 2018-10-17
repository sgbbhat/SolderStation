import time

start = time.time()

dictex = {}
listexp = ['one', 'two', 'three']

dictex[listexp[0]] = listexp[1:]

for key, value in dictex.items():
	print(key + " -> " + value[0])

end = time.time()

print(end-start)
