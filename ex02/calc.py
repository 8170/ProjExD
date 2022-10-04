print("hello world")


import tkinter as tk#モジュールインポート
import tkinter.messagebox as tkm
root = tk.Tk()#tkモジュールの中のTKのインスタンスを生成



def button_number(event):#練習3
    btn = event.widget
    num = btn["text"]
    #tkm.showinfo(num,f"{num}のボタンが押されました")
    entry.insert(tk.END,num)#末尾に挿入
    #entry.isnert(0,num)#先頭に数字が置かれるので良くない

def click_equal(event):
    eqn = entry.get()
    try:
        res = eval(eqn)
        entry.delete(0,tk.END)
        entry.insert(tk.END,res)
    except ZeroDivisionError as e:
        tkm.showwarning("警告","あなたは計算を知らないですね")
        entry.delete(0,tk.END)
    except SyntaxError as e:
        tkm.showwarning("警告文","あなたは計算が苦手かな?")
        entry.delete(0,tk.END)
    
    

def click_alldel(event):
    entry.delete(0,tk.END)

def click_del(event):
    num = entry.get()
    num_new = num[:-1]
    entry.delete(0,tk.END)
    entry.insert(tk.END,num_new)




root.title("tk")#練習1
root.geometry("400x800")

entry = tk.Entry(root,width=10,font=("Times New Roman",40),justify="right")#練習4
entry.grid(row=0,column=0,columnspan=3)

btn = tk.Button(root,text=f"AC",font=("Times New Roman",30),width=4,height=2)
btn.bind("<1>",click_alldel)
btn.grid(row=1,column=0)

btn = tk.Button(root,text=f"C",font=("Times New Roman",30),width=4,height=2)
btn.bind("<1>",click_del)
btn.grid(row=1,column=1)


r,c = 2,0#練習2
numbers = list(range(9,-1,-1))
others = ["00","."]
for i,num in enumerate(numbers+others,1):
    btn = tk.Button(root,text=f"{num}",font=("Times New Roman",30),width=4,height=2)
    btn.bind("<1>",button_number)
    btn.grid(row=r,column=c)
    c += 1
    if i%3 == 0:
        r += 1
        c = 0


operations = ["+","-","*","/"]
for i,num in enumerate(operations,1):
    btn = tk.Button(root,text=f"{num}",font=("Times New Roman",30),width=4,height=2)
    btn.bind("<1>",button_number)
    btn.grid(row=i,column=4)


btn = tk.Button(root,text=f"=",font=("Times New Roman",30),width=4,height=2)
btn.bind("<1>",click_equal)
btn.grid(row=5,column=4)



        
        




root.mainloop()#rootはインスタンス

# root.geometry("500x200")

# label = tk.Label(root,text="こんにちは",font=("",80))
# label.pack()#インスタンスメソッド

# button = tk.Button(root,text = "stop",font=("",30),bg="red")
# button.pack()

# entry = tk.Entry(root,width=40)
# entry.insert(tk.END,"入力して下さい")
# entry.pack()


# tkm.showwarning("警告","はいやったなお前")

# button = tk.Button(root,text="押すな",font=("",40))
# button.bind("<1>",button_click)
# button.pack()








