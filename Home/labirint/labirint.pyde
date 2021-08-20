a = [
    [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
    [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
    [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
    [2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3],
    [2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3],
    [3,3,3,3,3,3,3,3,3,3,3,2,2,3,3,3,3,3,3,3,3,3,3,3,3],
    [3,3,3,5,5,5,5,5,5,3,3,2,2,3,3,3,3,3,3,3,3,3,3,3,3],
    [3,3,5,5,5,5,5,5,5,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [3,5,5,5,10,10,10,5,5,5,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [3,5,5,5,10,10,10,10,5,5,3,1,1,3,15,15,3,15,15,15,15,15,15,15,3],
    
    [3,5,5,5,10,10,10,10,5,5,3,1,1,3,15,15,3,3,3,15,15,15,15,15,3],
    [5,5,5,10,10,10,10,10,5,5,3,1,1,3,15,15,3,3,3,15,15,15,15,15,15],
    [5,5,10,10,10,10,10,10,5,5,3,1,1,3,15,15,15,15,15,15,15,15,15,15,15],
    [5,5,10,10,10,10,10,10,5,5,3,1,1,3,15,15,15,15,15,15,15,15,15,15,3],
    [5,5,10,10,10,10,10,10,5,5,3,1,1,3,15,15,15,15,15,15,15,15,15,15,3],
    [5,5,10,10,10,10,10,10,5,5,3,1,1,3,15,15,15,15,15,15,15,15,15,15,3],
    [5,5,10,10,10,10,10,10,5,5,3,1,1,3,15,15,15,15,15,15,15,15,15,15,3],
    [5,5,10,10,10,10,10,10,5,5,3,1,1,3,3,3,3,3,3,3,3,3,15,15,3],
    [5,5,10,10,10,10,5,5,5,5,3,1,1,2,2,2,2,2,2,2,2,3,15,15,3],
    [5,5,5,5,5,5,5,5,5,3,3,1,1,3,3,3,3,3,3,3,2,3,15,15,3],
    
    [5,5,5,5,5,5,5,3,3,3,3,1,1,3,5,5,5,5,5,5,2,3,3,3,3],
    [3,5,5,5,5,3,3,3,3,3,3,1,1,3,3,5,5,5,5,5,2,3,3,3,3],
    [3,3,3,3,3,3,3,3,3,3,3,1,1,3,3,3,3,3,3,3,2,3,3,3,3],
    [3,3,3,3,3,3,3,3,3,3,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [3,3,3,3,3,3,3,3,3,3,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]

start = 3, 0
end_ = 10, 0

m = []

def make_step(k):
  for i in range(len(m)):
    for j in range(len(m[i])):
      if m[i][j] == k:
        if i>0 and m[i-1][j] == 0 and a[i-1][j] == 0:
          m[i-1][j] = k + 1
        if j>0 and m[i][j-1] == 0 and a[i][j-1] == 0:
          m[i][j-1] = k + 1
        if i<len(m)-1 and m[i+1][j] == 0 and a[i+1][j] == 0:
          m[i+1][j] = k + 1
        if j<len(m[i])-1 and m[i][j+1] == 0 and a[i][j+1] == 0:
           m[i][j+1] = k + 1

k = 0

d = 0
sh = 0
b = False
time = 0
t = False
v = 1
def setup():
    global d,sh,k,m,start,end_,the_path
    size(800,800)
    d = 32
    sh = 32
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] == 1:
                fill(118)
            elif a[i][j] == 2:
                fill("#835421")
            elif a[i][j] == 3:
                fill("#38C61C")
            elif a[i][j] == 5:
                fill("#2AD8D7")
            elif a[i][j] == 10:
                fill("#1D5EB2")
            elif a[i][j] == 15:
                fill("#239D4E")
            rect(j * d,i * sh,d,sh)
    y_start, x_start = start
    y_end, x_end = end_
    fill(255,0,0)
    rect((x_start * d) + d / 4, (y_start * sh) + sh / 4,d / 2,sh / 2)
    fill(0,255,0)
    rect((x_end * d) + d / 4, (y_end * sh) + sh / 4,d / 2,sh / 2)

    frameRate(25)
def draw():
    global d,sh,k,m,start,end_,the_path,b,time,t,v

    if mousePressed == True:
        b = True
    if b == True:
        for i in range(len(a)):
            m.append([])
            for j in range(len(a[i])):
                m[-1].append(0)
        i,j = start
        m[i][j] = 1
        
        while m[end_[0]][end_[1]] == 0:
            k += 1
            make_step(k)
        
        i, j = end_
        k = m[i][j]
        the_path = [(i,j)]
        while k > 1:
            if i > 0 and m[i - 1][j] == k-1:
                i, j = i-1, j
                the_path.append((i, j))
                k-=1
            elif j > 0 and m[i][j - 1] == k-1:
                i, j = i, j-1
                the_path.append((i, j))
                k-=1
            elif i < len(m) - 1 and m[i + 1][j] == k-1:
                i, j = i+1, j
                the_path.append((i, j))
                k-=1
            elif j < len(m[i]) - 1 and m[i][j + 1] == k-1:
                i, j = i, j+1
                the_path.append((i, j))
                k -= 1
        if len(the_path) - v >= 0:
            fill(0,116,255)
            ellipse((the_path[len(the_path)-v][1] * sh) + 40,(the_path[len(the_path)-v][0] * d) + 40,d - 60,sh - 60)
            v += 1
