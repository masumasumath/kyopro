class UnionFind():

    #初期化
    #n:要素数
    def __init__(self, n):
        self.par = [-1] * n #親の頂点番号
        self.rank = [0] * n #根付き木の高さ
        self.size = [1] * n #寝付き木に含まれる頂点の個数

    #根を求める
    def root(self, x):
        #根の場合は自分自身を返す
        if self.par[x] == -1: return x
        else:
            self.par[x] = self.root(self.par[x]) #経路圧縮
            return self.par[x]

    #xとyが同じグループに属するか（根が一致するか）
    def issame(self, x, y):
        return self.root(x) == self.root(y)

    #xを含むグループとyを含むグループを併合（Unite）する
    def unite(self,x,y):

        #x側の根とy側の根を取得する
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry: return False #すでに同じグループのときは何もしない
        # union by rank
        # ry側のrankが小さくなるようにする
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        # ryの親をrxにする
        self.par[ry] = rx

        #rxの子としてyを含むグループを付け加えるので，rank[ry]が小さいときは
        #rank[rx]は増えない
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        
        #yを含むのグループをxを含むグループに付け加えるので，サイズが増える
        self.size[rx] += self.size[ry] 

        return True
    
    #xを含む寝付き木のサイズ（頂点数）を求める
    def siz(self, x):
        return self.size[x]

N, M = map(int,input().split())
V = UnionFind(N)
for _ in range(M):
    a,b = map(int,input().split())
    V.unite(a-1,b-1)
ans = 0
for i in range(N):
    if V.root(i) == i:
        ans = max(ans,V.siz(i))
print(ans)

