import unittest
from .. import heap

class test_heap(unittest.TestCase):
	def test_min_heapify(self):
		a = [10, 9]
		heap.min_heapify(a)
		self.assertEqual(a[0], 9)
		self.assertEqual(a[1], 10)
		
		b = [30, 29, 20, 19, 10, 9]
		heap.min_heapify(b)
		self.assertTrue(b[0] < b[1])
		self.assertTrue(b[0] < b[2])
		self.assertTrue(b[1] < b[3])
		self.assertTrue(b[1] < b[4])
		self.assertTrue(b[2] < b[5])

	def test_min_pop(self):
		a = [100, 99, 89, 90, 90, 100, 2, 54]
		heap.min_heapify(a)
		prev = heap.min_pop(a)
		for i in range(len(a) - 1):
			cur = heap.min_pop(a)
			self.assertTrue(cur >= prev)
			prev = cur

		b = [5, 5, 4, -10]
		heap.min_heapify(b)
		self.assertEqual(heap.min_pop(b), -10)
		self.assertEqual(heap.min_pop(b), 4)
		self.assertEqual(heap.min_pop(b), 5)
		self.assertEqual(heap.min_pop(b), 5)

		c = [1]
		heap.min_heapify(c)
		self.assertEqual(heap.min_pop(c), 1)
		self.assertEqual(c, [])

		e = []
		heap.min_heapify(e)
		self.assertEqual(heap.min_pop(e), None)

	def test_min_top(self):
		a = [10, 5, 1]
		heap.min_heapify(a)
		self.assertEqual(heap.min_top(a), 1)

		b = [3, 2, 7, 10, 5, 2]
		heap.min_heapify(b)
		self.assertEqual(heap.min_top(b), 2)

		e = []
		heap.min_heapify(e)
		self.assertEqual(heap.min_top(e), None)

	def test_min_push(self):
		a = []
		heap.min_push(a, 5)
		self.assertEqual(a[0], 5)
		heap.min_push(a, 7)
		self.assertEqual(a[0], 5)
		heap.min_push(a, 3)
		self.assertEqual(a[0], 3)
		heap.min_push(a, 3)
		self.assertEqual(a[0], 3)
		self.assertEqual(len(a), 4)

		b = [100, 7, 14, 25]
		heap.min_heapify(b)
		heap.min_push(b, 35)
		self.assertEqual(b[0], 7)
		heap.min_push(b, 3)
		self.assertEqual(b[0], 3)
		heap.min_push(b, -2)
		self.assertEqual(b[0], -2)
		heap.min_push(b, -5)
		self.assertEqual(b[0], -5)

	def test_min_nsmallest(self):
		a = [10, 20, 25, 5, -1, 100]
		heap.min_heapify(a)
		self.assertEqual(heap.min_nsmallest(a, 0), [])
		self.assertEqual(heap.min_nsmallest(a, 1), [-1])
		self.assertEqual(heap.min_nsmallest(a, 2), [-1, 5])
		self.assertEqual(heap.min_nsmallest(a, 3), [-1, 5, 10])
		self.assertEqual(heap.min_nsmallest(a, 4), [-1, 5, 10, 20])
		self.assertEqual(heap.min_nsmallest(a, 5), [-1, 5, 10, 20, 25])
		self.assertEqual(heap.min_nsmallest(a, 6), [-1, 5, 10, 20, 25, 100])
		self.assertEqual(heap.min_nsmallest(a, 7), [-1, 5, 10, 20, 25, 100])

	def test_min_nlargest(self):
		a = [10, 20, 25, 5, -1, 100]
		heap.min_heapify(a)
		self.assertEqual(heap.min_nlargest(a, 0), [])
		self.assertEqual(heap.min_nlargest(a, 1), [100])
		self.assertEqual(heap.min_nlargest(a, 2), [100, 25])
		self.assertEqual(heap.min_nlargest(a, 3), [100, 25, 20])
		self.assertEqual(heap.min_nlargest(a, 4), [100, 25, 20, 10])
		self.assertEqual(heap.min_nlargest(a, 5), [100, 25, 20, 10, 5])
		self.assertEqual(heap.min_nlargest(a, 6), [100, 25, 20, 10, 5, -1])
		self.assertEqual(heap.min_nlargest(a, 7), [100, 25, 20, 10, 5, -1])

	def test_min_replace(self):
		a = [10, 20, 25, 5, -1, 100]
		heap.min_heapify(a)
		self.assertEqual(heap.min_replace(a, -4), -1)
		self.assertEqual(a[0], -4)
		self.assertEqual(heap.min_replace(a, 7), -4)
		self.assertEqual(a[0], 5)

	def test_min_pushpop(self):
		a = [10, 20, 25, 5, -1, 100]
		heap.min_heapify(a)
		self.assertEqual(heap.min_pushpop(a, -4), -4)
		self.assertEqual(a[0], -1)
		self.assertEqual(heap.min_pushpop(a, 7), -1)
		self.assertEqual(a[0], 5)

	def test_min_merge(self):
		a = [5, 3, 1]
		b = [6, 4, 2, 1]
		heap.min_heapify(a)
		heap.min_heapify(b)
		c = heap.min_merge(a, b)
		prev = heap.min_pop(c)
		for i in range(len(c)):
			cur = heap.min_pop(c)
			self.assertTrue(cur >= prev)
			prev = cur

	def test_min_meld(self):
		a = [5, 3, 1]
		b = [6, 4, 2, 1]
		heap.min_heapify(a)
		heap.min_heapify(b)
		heap.min_meld(a, b)
		self.assertEqual(len(a), 7)
		self.assertEqual(len(b), 0)
		prev = heap.min_pop(a)
		for i in range(len(a)):
			cur = heap.min_pop(a)
			self.assertTrue(cur >= prev)
			prev = cur

if __name__ == '__main__':
	unittest.main(verbosity=2)
