def min_top(minheap):
	if len(minheap) == 0:
		return None
	return minheap[0]

def max_top(maxheap):
	if len(maxheap) == 0:
		return None
	return maxheap[0]

def min_push(minheap, item):
	minheap.append(item)
	_min_shiftup(minheap, len(minheap) - 1)

def max_push(maxheap, item):
	maxheap.append(item)
	__max_shiftup(maxheap, len(maxheap) - 1)

def min_pop(minheap):
	if len(minheap) == 0:
		return None
	minval = minheap[0]
	minheap[0] = minheap[len(minheap) - 1]
	del minheap[len(minheap) - 1]
	__min_shiftdown(minheap, 0)
	return minval

def max_pop(maxheap):
	if len(maxheap) == 0:
		return None
	maxval = maxheap[0]
	maxheap[0] = maxheap[len(maxheap) - 1]
	del maxheap[len(maxheap) - 1]
	__max_shiftdown(maxheap, 0)
	return maxval

# pop then push, return minimum before push
def min_replace(minheap, item):
	minval = minheap[0]
	minheap[0] = item
	__min_shiftdown(minheap, 0)
	return minval

def max_replace(maxheap, item):
	maxval = maxheap[0]
	maxheap[0] = item
	__max_shiftdown(maxheap, 0)
	return maxval

# push then pop, return minimum including new item
def min_pushpop(minheap, item):
	if item <= minheap[0]:
		return item
	return min_replace(minheap, item)

def max_pushpop(maxheap, item):
	if item >= maxheap[0]:
		return item
	return max_replace(maxheap, item)

def min_heapify(x):
	# (len(x) - 1) // 2 is the last parent node of heap
	for i in range((len(x) - 1) // 2, -1, -1):
		__min_shiftdown(x, i)

def max_heapify(x):
	for i in range((len(x) - 1) // 2, -1, -1):
		__max_shiftdown(x, i)

def min_nlargest(minheap, n):
	copy = minheap[:]
	result = []
	for i in range(len(minheap)):
		result.append(min_pop(copy))
	return list(reversed(result))[:n]

def max_nlargest(maxheap, n):
	copy = maxheap[:]
	result = []
	for i in range(min(n, len(copy))):
		result.append(max_pop(copy))
	return result

def min_nsmallest(minheap, n):
	copy = minheap[:]
	result = []
	for i in range(min(n, len(copy))):
		result.append(min_pop(copy))
	return result

def max_nsmallest(maxheap, n):
	copy = maxheap[:]
	result = []
	for i in range(len(maxheap)):
		result.append(max_pop(copy))
	return list(reversed(result))[:n]

# advance
def min_merge(minheap1, minheap2):
	longcopy, shortcopy = minheap1[:], minheap2[:]
	if len(longcopy) < len(shortcopy):
		longcopy, shortcopy = shortcopy, longcopy
	for i in range(len(shortcopy)):
		min_push(longcopy, min_pop(shortcopy))
	return longcopy

def max_merge(maxheap1, maxheap2):
	longcopy, shortcopy = maxheap1[:], maxheap2[:]
	if len(longcopy) < len(shortcopy):
		longcopy, shortcopy = shortcopy, longcopy
	for i in range(len(shortcopy)):
		max_push(longcopy, max_pop(shortcopy))
	return longcopy

# advance
def min_meld(minheap1, minheap2):
	for i in range(len(minheap2)):
		min_push(minheap1, min_pop(minheap2))
	return minheap1

def max_meld(maxheap1, maxheap2):
	for i in range(len(maxheap2)):
		max_push(maxheap1, max_pop(maxheap2))
	return maxheap1

def __min_shiftdown(x, idx):
	min_idx = idx
	if idx * 2 + 1 < len(x) and x[idx * 2 + 1] < x[idx]:
		min_idx = idx * 2 + 1
	if idx * 2 + 2 < len(x) and x[idx * 2 + 2] < x[min_idx]:
		min_idx = idx * 2 + 2
	if min_idx != idx:
		x[idx], x[min_idx] = x[min_idx], x[idx]
		__min_shiftdown(x, min_idx)

def __max_shiftdown(x, idx):
	max_idx = idx
	if idx * 2 + 1 < len(x) and x[idx * 2 + 1] > x[idx]:
		max_idx = idx * 2 + 1
	if idx * 2 + 2 < len(x) and x[idx * 2 + 2] > x[max_idx]:
		max_idx = idx * 2 + 2
	if max_idx != idx:
		x[idx], x[max_idx] = x[max_idx], x[idx]
		__max_shiftdown(x, max_idx)

def _min_shiftup(x, idx):
	if idx <= 0:
		return
	if x[(idx - 1) // 2] > x[idx]:
		x[idx], x[(idx - 1) // 2] = x[(idx - 1) // 2], x[idx]
		_min_shiftup(x, (idx - 1) // 2)

def __max_shiftup(x, idx):
	if idx <= 0:
		return
	if x[(idx - 1) // 2] < x[idx]:
		x[idx], x[(idx - 1) // 2] = x[(idx - 1) // 2], x[idx]
		__max_shiftup(x, (idx - 1) // 2)

class MinHeapQueue:
	REMOVED = -1

	def __init__(self):
		self.q = []
		self.map = {}
		self.push_cnt = 0

	def top(self):
		if len(self.q) == 0:
			return None
		priority, push_cnt, item = self.q[0]
		return item

	def push(self, item, priority=0):
		qitem = self.__to_qitem(item, priority)
		min_push(self.q, qitem)

	def pop(self):
		if len(self.q) == 0:
			return None
		return self.__from_qitem(min_pop(self.q))

	def pushpop(self, item, priority):
		qitem = self.__to_qitem(item, priority)
		return self.__from_qitem(min_pushpop(self.q, qitem))

	def replace(self, item, priority):
		qitem = self.__to_qitem(item, priority)
		return self.__from_qitem(min_replace(self.q, qitem))

	def topn(self, n):
		if n < 0:
			raise ValueError("n value {0} is less than zero".format(n))
		top_qitems = min_nsmallest(self.q, n)
		top_items = [self.__from_qitem(qitem, delete=False) for qitem in top_qitems]
		return top_items

	def remove(self, item):
		if item not in self.map:
			raise KeyError('item {0} not in queue'.format(item))
		minpriority, push_cnt, topitem = min_top(self.q)
		self.__decrease_priority(item, minpriority - 1)
		self.__from_qitem(min_pop(self.q))

	def exists(self, item):
		return item in self.map

	def update(self, item, priority):
		if item not in self.map:
			raise KeyError('item {0} not in queue'.format(item))
		self.remove(item)
		self.push(item, priority)

	def empty(self):
		self.map.clear()
		self.q = []

	def len(self):
		return len(self.q)

	def __to_qitem(self, item, priority):
		if item in self.map:
			raise ValueError("duplicate item '{0}' push".format(item))
		qitem = [priority, self.push_cnt, item]
		self.map[item] = qitem
		self.push_cnt += 1
		return qitem

	def __from_qitem(self, qitem, delete=True):
		priority, push_cnt, item = qitem
		if delete:
			del self.map[item]
		return item

	def __decrease_priority(self, item, newpriority):
		qitem = self.map[item]
		if qitem[0] < newpriority:
			raise ValueError('new priority {0} is higher than original priority {1}'.format(newpriority, oldpriority))
		idx = self.q.index(qitem)
		qitem[0] = newpriority
		_min_shiftup(self.q, idx)


