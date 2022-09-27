from ast import Break
import random
import datetime

a = []
for i in range(26):
    a.append(chr(65+i))


b = 10
c = 2

def shutudai():
    print("対象文字")
    d = random.sample(a,b)
    for i in d:
        print(i,end=" ")
    print("表示文字")
    a1 = random.sample(d,c)
    a2 = set(a1)
    #ad = set(d)
    #a22 = ad - a2
    a22 = set(d) - a2
    a23 = list(a22)
    for i in a23:
        print(i,end=" ")
    
    d = 2
    st = datetime.datetime.now()
    while d > 0:
        ans = input("欠損文字はいくつあるでしょうか？：")
        if ans in a2:
            print("正解!!")
            d -= 1
        elif ans not in a2:
            print("不正解")
    else:
        print("ゲームは終了です！クリアおめでとうございます!")
        Break
    ed = datetime.datetime.now()
    print(f"クリアタイムは{(ed-st).seconds}秒です")


    



if __name__ == "__main__":
    shutudai()
 
