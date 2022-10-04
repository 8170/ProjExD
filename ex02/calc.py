print("hello world")


import tkinter as tk#モジュールインポート
import tkinter.messagebox as tkm
root = tk.Tk()#tkモジュールの中のTKのインスタンスを生成

# def button_click(event):
#     btn = event.widget
#     txt = btn["text"]
#     tkm.showinfo(txt,f"[{txt}]ボタンが押されました")

root.title("tk")#練習1
root.geometry("300x500")


r,c = 0,0
for num in range(9,-1,-1):
    btn = tk.Button(root,text=f"{num}",font=("",30),width=4,height=2)
    btn.grid(row=r,column=c)
    c += 1
    if c == 3:
        c = 0
        r += 1
        
        




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








