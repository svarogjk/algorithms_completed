from math import log2


class Heap():

    def __init__(self, array: list):
        self.array = array
        self.heap_height = log2(len(self.array))


    def parent(self, i: int)->int:
        return i // 2


    def left(self, i: int)->int:
        return 2 * i + 1


    def right(self, i: int)->int:
        return 2 * i + 2


    def max_heap_prop(self):
        for i in range(len(self.array)):
            _parent = self.parent(i)
            if self.array[_parent] < self.array[i]:
                return False
        return True


    def max_heapify(self, array, i):
        l = self.left(i)
        r = self.right(i)
        if l <= len(array) - 1 and array[l] > array[i]:
            largest = l
        else:
            largest = i
        if r <= len(array) - 1 and array[r] > array[largest]:
            largest = r
        if largest != i:
            array[i], array[largest] = array[largest], array[i]
            self.max_heapify(array, largest)


    def build_max_heap(self):
        for i in range(len(self.array) // 2 - 1, -1, -1):
            self.max_heapify(self.array, i)


    def heap_sort(self):
        self.build_max_heap()
        for i in range(len(self.array) - 1, 0, -1):
            self.array[0], self.array[i] = self.array[i], self.array[0]
            _array = self.array[:i]
            self.max_heapify(_array, 0)
            self.array = _array +  self.array[i:]
            print(self.array)


class HeapQueue(Heap):


    def heap_maximum(self):
        return self.array[0]


    def heap_extract_max(self):
        if self.array == []:
            raise ValueError("empty array!!!")
        self.array[0], self.array[len(self.array) - 1] = self.array[len(self.array) - 1], self.array[0]
        _max = self.array.pop()
        self.max_heapify(self.array, 0)
        return _max


    def heap_increase_key(self):
        i = len(self.array) - 1
        while i > 0 and self.array[self.parent(i)] < self.array[i]:
            self.array[i], self.array[self.parent(i)] = self.array[self.parent(i)], self.array[i]
            i = self.parent(i)


    def max_heap_insert(self, key):
        self.array.append(key)
        self.heap_increase_key()


if __name__ == '__main__':
    from unittest import TestCase, main

    # array = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
    array = [15, 13, 9, 5, 12, 8, 7, 4, 0, 6, 2, 1]

    h = HeapQueue(array)
    # h.max_heapify(h.array, 1)
    # h.heap_sort()
    h.build_max_heap()
    print(h.array)

    insert_array = [20, 2, 25, 3, 26, 5]
    for e in insert_array:
        h.max_heap_insert(e)
        print(h.array)


    # class SimpleTest(TestCase):
    #
    #     def test(self):
    #         self.assertEqual(h.array, sorted(A))
    #
    # main()