class PriorityQ():
    def __init__(self):
        self.queue = []
    
    def put(self,data):
        self.queue.append(data)
        i = len(self.queue)-1
        while i > 0:
            p = (i-1)//2
            if self.queue[i] < self.queue[p]:
                self.queue[i], self.queue[p] = self.queue[p], self.queue[i]
                i = p
            else: break
    
    def get(self):
        n = len(self.queue)
        self.queue[n-1], self.queue[0] = self.queue[0], self.queue[n-1]
        v = self.queue.pop()
        n-=1
        self.heapify(0,n)
        return v
    
    def heapify(self,i,n):
        l = 2*i + 1
        r = 2*i + 2
        m = i
        if l < n and self.queue[l] < self.queue[m]: m = l
        if r < n and self.queue[r] < self.queue[m]: m = r
        if m != i:
            self.queue[m], self.queue[i] = self.queue[i], self.queue[m]
            self.heapify(m,n)

    def empty(self):
        return [] == self.queue

class PriorityTupleQ(): #tuple[0] -> value, rest -> extraData
    def __init__(self):
        self.queue = []
    
    def put(self,dataTuple):
        self.queue.append(dataTuple)
        i = len(self.queue)-1
        while i > 0:
            p = (i-1)//2
            if self.queue[i][0] < self.queue[p][0]:
                self.queue[i], self.queue[p] = self.queue[p], self.queue[i]
                i = p
            else: break
    
    def get(self):
        n = len(self.queue)
        self.queue[n-1], self.queue[0] = self.queue[0], self.queue[n-1]
        v = self.queue.pop()
        n-=1
        self.heapify(0,n)
        return v
    
    def heapify(self,i,n):
        l = 2*i + 1
        r = 2*i + 2
        m = i
        if l < n and self.queue[l][0] < self.queue[m][0]: m = l
        if r < n and self.queue[r][0] < self.queue[m][0]: m = r
        if m != i:
            self.queue[m], self.queue[i] = self.queue[i], self.queue[m]
            self.heapify(m,n)

    def empty(self):
        return [] == self.queue

        
# Q = PriorityQ()
# Q.put(4)
# Q.put(6)
# Q.put(-1)
# print(Q.get())
# print(Q.empty())
# print(Q.get())
# print(Q.empty())
# print(Q.get())
# print(Q.empty())

Q = PriorityTupleQ()
Q.put((4,"samolot"))
Q.put((6, "auto"))
Q.put((-1, "pieszo"))
print(Q.get())
print(Q.empty())
print(Q.get())
print(Q.empty())
print(Q.get())
print(Q.empty())