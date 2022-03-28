#Dynamic array

import ctypes

import sys
class DynamicArray(object):

    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)

    def __len__(self):
        return self.n

    def __getitem__(self, k):
        if not 0 <= k < self.n:
            return IndexError('k is out of index')
        return self.A[k]

    def append(self, ele):
        if self.n == self.capacity:
            self._resize(2 * self.capacity)
        self.A[self.n] = ele
        self.n += 1

    def _resize(self, cap):
        B = self.make_array(cap)
        for k in range(self.n):
            B[k] = self.A[k]
        self.A = B
        self.capacity = cap

    def make_array(self, c):
        return(c * ctypes.py_object)()

arr = DynamicArray()
arr.append(1)
print(len(arr))
arr.append(2)
print(len(arr))
for i in range(100):
    arr.append(i)
    print(len(arr))
    print(sys.getsizeof(arr))
