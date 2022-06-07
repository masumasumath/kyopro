import time
import random
import copy

#右隣と上とのつながりをチェックして，OKなら繋げる
def do_connect(i,j,tiles,V,N):

    #右隣
    if is_connect_r(i,j,tiles,N):
        V.unite(N*i + j, N*i + j+1)
    #すぐ上
    if is_connect_u(i,j,tiles):
        V.unite(N*(i-1) + j, N*i + j)

def do_connect_all(tiles, V, N):
    for i in range(N):
        for j in range(N):
            do_connect(i,j,tiles, V, N)

#(i,j)にあるタイルが上と繋がっているか
def is_connect_u(i,j,tiles):
    return ( 0 < i ) and  ((tiles[i][j] & 2) | (tiles[i-1][j] & 8) == 10)
        
#(i,j)にあるタイルが下と繋がっているか
def is_connect_d(i,j,tiles,N):
    return ( i < N-1 ) and  ((tiles[i][j] & 8) | (tiles[i+1][j] & 2) == 10)

#(i,j)にあるタイルが右と繋がっているか
def is_connect_r(i,j,tiles,N):
    return ( j < N-1 ) and  ((tiles[i][j] & 4) | (tiles[i][j+1] & 1) == 5)

#(i,j)にあるタイルが左と繋がっているか
def is_connect_l(i,j,tiles):
    return ( 0 < j ) and  ((tiles[i][j] & 1) | (tiles[i][j-1] & 4) == 5)


class UnionFind():

    #初期化
    #n:要素数
    def __init__(self, n):
        self.par = [-1] * n #親の頂点番号
        self.rank = [0] * n #根付き木の高さ
        self.siz = [1] * n #寝付き木に含まれる頂点の個数

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
        
        #yを含むグループをxを含むグループに付け加えるので，サイズが増える
        self.siz[rx] += self.siz[ry] 

        return True
    
    #xを含む寝付き木のサイズ（頂点数）を求める
    def size(self, x):
        return self.siz[self.root(x)]


#最大の木の大きさを求める
def calc_size(tile, N, V):
    res = 0
    for i in range(N*N):
        res = max(res,V.size(i))
    return res

#スコアを求める
def calc_score(tile, V, N, T, K = 0):
    S = calc_size(tile,N,V)
    return S
    # if S < N*N - 1:
    #     return round(500000*S/(N*N-1))
    # else:
    #     round(500000*(2-K/T))


def main():

    #入力の受取
    N, T = map(int,input().split())
    #計測開始
    start = time.perf_counter()

    #初期化（木の管理）
    initV = UnionFind(N*N)

    #入力の受取
    #初期タイル
    init = []
    ori = []
    for i in range(N):
        t = list(input())
        tt = list(map(lambda x:int(x,16),t))
        init.append(tt)
        for j in range(N):
            #0（空きマス）の場所を保持しておく
            if init[i][j] == 0:
                ori.append(i)
                ori.append(j)

    #0（空きマス）以外のとき，つながっていればつなげる
    do_connect_all(init,initV,N)

    tiles = copy.deepcopy(init)

    #初期のスコアを求める
    init_score = calc_score(tiles, initV, N, T)
    #最大スコアを格納する変数
    max_score = init_score

    ANS = []
    TMP = []
    x,y = ori[0], ori[1]
    pre = 0
    ##時間制限ぎりぎりまで移動する
    while time.perf_counter()-start<2.9 and len(TMP) < T:
        direct = random.randint(1,4)
        #空きマスを右へ
        if direct == 1 and pre != 3:
            if y+1 < N:
                tiles[x][y],tiles[x][y+1] = tiles[x][y+1], tiles[x][y]
                y += 1
                TMP.append("R")
            else:
                direct = 2
        #空きマスを上へ
        if direct == 2 and pre != 4:
            if 0 < x-1:
                tiles[x][y],tiles[x-1][y] = tiles[x-1][y], tiles[x][y]
                x -= 1
                TMP.append("U")
            else:
                direct = 3
        #空きマスを左へ
        if direct == 3 and pre != 1:
            if 0 < y-1:
                tiles[x][y],tiles[x][y-1] = tiles[x][y-1], tiles[x][y]
                y -= 1
                TMP.append("L")
            else:
                direct = 4
        #空きマスを下へ
        if direct == 4 and pre != 2:
            if x+1 < N:
                tiles[x][y],tiles[x+1][y] = tiles[x+1][y], tiles[x][y]
                x += 1
                TMP.append("D")
            else:
                direct = 1
        #移動した方向を保存
        pre = direct
        
        #回数制限いっぱい
        if len(TMP) == T:
            V = UnionFind(N*N)
            do_connect_all(tiles,V,N)
            tmp_score = calc_score(tiles,V,N,T,len(TMP))
            if tmp_score > max_score:
                # for ttt in TMP:
                #     print(ttt,end = "")
                # print()
                # print(tmp_score)
                max_score = tmp_score
                ANS = copy.deepcopy(TMP)
            TMP = []
            x,y = ori[0],ori[1]
            pre = 0
            del V

    #答の出力
    for a in ANS:
       print(a, end="")
    # print()
    # print(max_score)

if __name__=="__main__":
    main()

