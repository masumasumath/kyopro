# 1. matplotlib.patchesモジュールの読み込み
import matplotlib.pyplot as plt
from matplotlib import patches
import random
 
# 2.	Axesオブジェクト生成
fig, ax = plt.subplots(figsize=(4,4))
 
ax.set_xticks([0, 3, 6, 9])
ax.set_yticks([0, 3, 6, 9])
ax.grid()
 
# 3. 図形オブジェクト生成
c1 = patches.Circle( xy=(3,3), radius=3, alpha = 0.3) # 円のオブジェクト
c2 = patches.Circle( xy=(3,7), radius=2, alpha = 0.3) # 円のオブジェクト

cnt = 0
d = []
#10000回の試行でびっしりになる
N = 10000
for _ in range(10000):
    x = random.uniform(0.0,6.0)
    y = random.uniform(0.0,9.0)
    c = patches.Circle( xy=(x,y), radius=0.05, alpha = 0.4,facecolor = 'red') # 円のオブジェクト
    #Axesに図形オブジェクト追加・表示
    ax.add_patch(c)
    #円の内側の点の個数をカウント
    if (x-3)**2 + (y-7)**2 <= 4 or (x-3)**2 + (y-3)**2 <= 9: cnt += 1
print(cnt/N)

#r = patches.Rectangle( xy=(1,1) , width=1, height=1) # 四角形のオブジェクト
 
# 4. Axesに図形オブジェクト追加・表示
ax.add_patch(c1)
ax.add_patch(c2)
 
plt.show()