#テンプレート
import sys
def i():return int(sys.stdin.readline().replace("\n",""))
def i2():return map(int,sys.stdin.readline().replace("\n","").split())
def l():return list(sys.stdin.readline().replace("\n",""))
def intl():return [int(k) for k in sys.stdin.readline().replace("\n","").split()]
def lx():return list(map(lambda x:int(x)*-1),sys.stdin.readline().replace("\n","").split())
if __name__ == "__main__":pass
#二分探索
def BinarySerch(n,list,key):#len(list),list,探索するkey #sorted
    r=n
    l=0
    while l<r:
        mid=(r+l)//2
        if list[mid]==key:return True
        elif list[mid]>key:r=mid
        else:l=mid+1
    return False
#優先度付きキュー 
import heapq
heapq.heapify(リスト)でリストを優先度付きキューに変換。
heapq.heappop(優先度付きキュー)で優先度付きキューから最小値を取り出す。
heapq.heappush(優先度付きキュー,要素)で優先度付きキューに要素を挿入。

#深さ優先探索
def dfs(index,tree):
    print(index)
    sa.append(index)
    if tree[index][0] != -1:
        dfs(tree[index][0],tree)
    na.append(index)
    if tree[index][1] != -1:
        dfs(tree[index][1],tree)
    at.append(index)

#約数列挙
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    # divisors.sort()
    return divisors

def dfs(A):
    # 数列の長さが N に達したら打ち切り
    if len(A) == N:
        # 処理
        return
    for v in range(M):
        A.append(v)
        dfs(A)
        A.pop()

dfs([])