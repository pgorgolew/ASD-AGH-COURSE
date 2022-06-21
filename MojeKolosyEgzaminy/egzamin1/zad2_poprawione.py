from zad2testy import runtests
inf = float("inf")
# Pawel Gorgolewski
# Nalezy rozwazac rozne stany wierzcholkow (zalezne od odwrocenia) oraz predkosc
# do kolejki wrzucamy (dystans,y,x,kierunek,predksoc)
# niestety program wyrzuca zawsze inf, nie zdazylem
# zlozonosc to dijkstra dla grafu o k*w*4 wierzcholkach

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

def robot( L, A, B ):
    w = len(L)
    k = len(L[0])
    xp, yp = A
    xk, yk = B
    d = [[[inf,inf,inf,inf] for _ in range(k)] for _ in range(w)]
    # d[v][0] -> obrocony w prawo
    # d[v][1] -> obrocony w dol
    # d[v][2] -> obrocony w lewo
    # d[v][3] -> obrocont w gore
    done = [[[False,False,False,False] for _ in range(k)] for _ in range(w)]
    speed = [60,40,30]
    Q = PriorityTupleQ()
    d[yp][xp][0] = 0
    Q.put((0,yp,xp,0,0))
    while not Q.empty():
        dist,y,x,t,v = Q.get()
        if x==xk and y==yk: break
        if done[y][x][t]: continue
        
        if x+1 < k and L[y][x+1] == " ": #prawo
            if t==0 : #jestem skierowany w jego strone
                if v != 3: v+=1
                if d[y][x+1][0] > dist+speed[v-1]:
                    d[y][x+1][0] = dist+speed[v-1]
                    Q.put((d[y][x+1][0],y,x+1,0,v))
            elif t==2:
                if d[y][x][0] > dist + 2*45:
                    d[y][x][0] = dist + 2*45
                    Q.put((d[y][x][0],y,x,0,0))
            else:
                if d[y][x][0] > dist + 45:
                    d[y][x][0] = dist + 45
                    Q.put((d[y][x][0],y,x,0,0))
        
        if y+1 < w and L[y+1][x] == " ": #w dol
            if t==1 : #jestem skierowany w jego strone
                if v != 3: v+=1
                if d[y+1][x][1] > dist+speed[v-1]:
                    d[y+1][x][1] = dist+speed[v-1]
                    Q.put((d[y+1][x][1],y+1,x,1,v))
            elif t==3:
                if d[y][x][1] > dist + 2*45:
                    d[y][x][1] = dist + 2*45
                    Q.put((d[y][x][1],y,x,1,0))
            else:
                if d[y][x][1] > dist + 45:
                    d[y][x][1] = dist + 45
                    Q.put((d[y][x][1],y,x,1,0))

        if y-1 >= 0 and L[y-1][x] == " ": #w gore
            if t==3 : #jestem skierowany w jego strone
                if v != 3: v+=1
                if d[y-1][x][3] > dist+speed[v-1]:
                    d[y-1][x][3] = dist+speed[v-1]
                    Q.put((d[y-1][x][3],y-1,x,3,v))
            elif t==1:
                if d[y][x][3] > dist + 2*45:
                    d[y][x][3] = dist + 2*45
                    Q.put((d[y][x][3],y,x,3,0))
            else:
                if d[y][x][3] > dist + 45:
                    d[y][x][3] = dist + 45
                    Q.put((d[y][x][3],y,x,3,0))

        if x-1 >= 0 and L[y][x-1] == " ": #lewo
            if t==2 : #jestem skierowany w jego strone
                if v != 3: v+=1
                if d[y][x-1][2] > dist+speed[v-1]:
                    d[y][x-1][2] = dist+speed[v-1]
                    Q.put((d[y][x-1][2],y,x-1,2,v))
            elif t==0:
                if d[y][x][2] > dist + 2*45:
                    d[y][x][2] = dist + 2*45
                    Q.put((d[y][x][2],y,x,2,0))
            else:
                if d[y][x][2] > dist + 45:
                    d[y][x][2] = dist + 45
                    Q.put((d[y][x][2],y,x,2,0))

        done[y][x][t] = True
        
    res = min(d[yk][xk])
    return res if res < inf else None


    
runtests( robot )