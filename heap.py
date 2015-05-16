def min(minheap):
	return minheap[0]

def min_push(minheap, item):
	minheap.append(item)
	__min_shiftup(minheap, len(minheap) - 1)

def min_pop(minheap):
	minval = minheap[0]
	minheap[0] = minheap[len(minheap) - 1]
	del minheap[len(minheap) - 1]
	__min_shiftdown(minheap, 0)
	return minval

# pop then push, return minimum before push
def min_replace(minheap, item):
	minval = minheap[0]
	minheap[0] = item
	__min_shiftdown(minheap, 0)
	return minval

# push then pop, return minimum including new item
def min_pushpop(minheap, item):
	if item <= minheap[0]:
		return item
	return min_replace(minheap, item)

def min_heapify(x):
	# (len(x) - 1) // 2 is the last parent node of heap
	for i in range((len(x) - 1) // 2, -1, -1):
		__min_shiftdown(x, i)

def min_nlargest(minheap, n):
	copy = minheap[:]
	result = []
	for i in range(len(minheap)):
		result.append(min_pop(copy))
	return list(reversed(result))[:n]

def min_nsmallest(minheap, n):
	copy = minheap[:]
	result = []
	for i in range(n):
		result.append(min_pop(copy))
	return result

# advance
def min_merge(minheap1, minheap2):
	longcopy, shortcopy = minheap1[:], minheap2[:]
	if len(longcopy) < len(shortcopy):
		longcopy, shortcopy = shortcopy, longcopy
	for i in range(len(shortcopy)):
		min_push(longcopy, min_pop(shortcopy))
	return longcopy

# advance
def min_meld(minheap1, minheap2):
	for i in range(len(minheap2)):
		min_push(minheap1, min_pop(minheap2))
	return minheap1

def __min_shiftdown(x, idx):
	min_idx = idx
	if idx * 2 + 1 < len(x) and x[idx * 2 + 1] < x[idx]:
		min_idx = idx * 2 + 1
	if idx * 2 + 2 < len(x) and x[idx * 2 + 2] < x[min_idx]:
		min_idx = idx * 2 + 2
	if min_idx != idx:
		x[idx], x[min_idx] = x[min_idx], x[idx]
		__min_shiftdown(x, min_idx)

def __min_shiftup(x, idx):
	if idx <= 0:
		return
	if x[(idx - 1) // 2] > x[idx]:
		x[idx], x[(idx - 1) // 2] = x[(idx - 1) // 2], x[idx]
		__min_shiftup(x, (idx - 1) // 2)

