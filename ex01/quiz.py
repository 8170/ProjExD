import random

a = ["サザエのダンナの名前は？","カツオの妹の名前は？","タラオはカツオから見てどんな関係？"]
b = ["マスオ","ますお","わかめ","ワカメ","おい","甥","甥っ子","おいっこ"]

def shutudai():
    print("問題:")
    print(random.choices(a))
    print("答えるんだ:" )
