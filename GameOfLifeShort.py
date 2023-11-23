import copy as C,random as R,time as T
U,H,W,E,F=0.1,20,20,' ','#'
def v(g,x,y,hx,hy): return 0<=x<H and 0<=y<W and (x,y)!=(hx,hy) and g[x][y]!=E
def n(g,x,y): return sum(v(g,x+i,y+j,x,y) for i in [-1,0,1] for j in [-1,0,1])
g=[[F if R.randint(1,5)==1 else E for _ in range(W)] for _ in range(H)]
while 1:
    print('\n'.join([' '.join(r) for r in g]),f"\nPop:{sum(r.count(F) for r in g)}\n{'--'*W}")
    T.sleep(0.1)
    t=C.deepcopy(g)
    for x in range(H):
        for y in range(W): g[x][y]= E if t[x][y]==F and n(t,x,y) not in [2,3] else F if t[x][y]==E and n(t,x,y)==3 else g[x][y]
