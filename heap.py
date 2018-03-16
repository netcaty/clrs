class max_heap(list):
    def __init__(self, data):
        list.__init__(self, data)
        self.heap_size = len(data)
        self.build_max_heap()

    def _left(self, i):
        return 2 * i + 1

    def _right(self, i):
        return 2 * i + 2

    def _parent(self, i):
        assert i > 0, 'root node has no parent.'
        return (i - 1)//2

    def max_heapify(self, i):
        l = self._left(i)
        r = self._right(i)
        if l < self.heap_size and self[l] > self[i]:
            largest = l
        else:
            largest = i
        if r < self.heap_size and self[r] > self[largest]:
            largest = r
        if largest != i:
            self[i], self[largest] = self[largest], self[i]
            self.max_heapify(largest)

    def build_max_heap(self):
        for i in reversed(range(len(self) // 2)):
            self.max_heapify(i)

    def __str__(self):
        return super().__str__()

    def heap_maximum(self):
        return self[0]

    def heap_extract_maximum(self):
        if self.heap_size < 1:
            raise BufferError('heap underflow')
        max, self[0] = self[0], self[self.heap_size-1]
        self.heap_size -= 1
        self.max_heapify(0)
        return max

    def heap_increase_key(self, i, key):
        if key < self[i]:
            raise ValueError('new key is smaller than current key')

        while i > 0 and self[self._parent(i)] < key:
            self[i] = self[self._parent(i)]
            i = self._parent(i)
        self[i] = key

    def heap_insert(self, key):
        self.append(key)
        self.heap_size += 1
        self.heap_increase_key(self.heap_size-1, key)


def heapsort(a):
    h = max_heap(a)
    for i in range(len(h) - 1, 0, -1):
        h[0], h[i] = h[i], h[0]
        h.heap_size -= 1
        h.max_heapify(0)
    a[:] = h
