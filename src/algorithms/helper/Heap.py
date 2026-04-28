class Heap():
    #simple heap implementation for the heapprims algorithm,
    """
    supports push, pop, peek, and len operations. Auto heapifies on input if given an initial list of items
    """
    def __init__(self, items=None):
        if items is None:
            self.heap = []
        else:
            #heapify the input list in-place, for notable speed increase when seeding the heap with all edges from the start node
            self.heap = list(items) 
            #walk every non-leaf node in reverse order and sift it down to fix subtree heap property
            #range args: start at last non-leaf (len//2 - 1), stop before -1 (so we hit 0), step by -1
            for i in range(len(self.heap) // 2 - 1, -1, -1):
                self._sift_down(i)

    def __len__(self):
        #return the number of items in the heap
        return len(self.heap)
    
    def peek(self):
        #return the smallest item without removing it
        return self.heap[0] if self.heap else None
    
    def push(self, item):
        #add an item to the heap and maintain the heap property
        self.heap.append(item)
        self._sift_up(len(self.heap) - 1)

    def pop(self):
        #remove and return the smallest item from the heap
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)
        return root
    
    def _sift_up(self, idx):
        heap = self.heap
        while idx > 0:
            parent = (idx - 1) // 2
            if heap[idx] < heap[parent]:
                heap[idx], heap[parent] = heap[parent], heap[idx]
                idx = parent
            else:
                return

    def _sift_down(self, idx):
        n = len(self.heap)
        heap = self.heap          # local binding, faster lookups
        while True:
            left = 2 * idx + 1
            right = 2 * idx + 2
            smallest = idx
            if left  < n and heap[left]  < heap[smallest]: smallest = left
            if right < n and heap[right] < heap[smallest]: smallest = right
            if smallest == idx:
                return
            heap[idx], heap[smallest] = heap[smallest], heap[idx]
            idx = smallest