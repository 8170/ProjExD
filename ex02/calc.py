print("hello world")


import tkinter as tk#モジュールインポート
import tkinter.messagebox as tkm
root = tk.Tk()#tkモジュールの中のTKのインスタンスを生成



def button_number(event):#練習3
    btn = event.widget
    num = int(btn["text"])
    tkm.showinfo(num,f"{num}のボタンが押されました")

root.title("tk")#練習1
root.geometry("300x500")

entry = tk.Entry(root,width=10,font=("Times New Roman",40),justify="right")#練習4
entry.grid(row=0,column=0,columnspan=3)

r,c = 1,0#練習2
for i,num in enumerate(range(9,-1,-1),1):
    btn = tk.Button(root,text=f"{num}",font=("Times New Roman",30),width=4,height=2)
    btn.bind("<1>",button_number)
    btn.grid(row=r,column=c)
    c += 1
    if i%3 == 0:
        r += 1
        c = 0



        
        




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








