print("hello world")


import tkinter as tk#モジュールインポート
import tkinter.messagebox as tkm
root = tk.Tk()#tkモジュールの中のTKのインスタンスを生成

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    tkm.showinfo(txt,f"[{txt}]ボタンが押されました")

root.title("tk")
root.geometry("300x500")

# root.geometry("500x200")

# label = tk.Label(root,text="こんにちは",font=("",80))
# label.pack()#インスタンスメソッド

# button = tk.Button(root,text = "stop",font=("",30),bg="red")
# button.pack()

# entry = tk.Entry(root,width=40)
# entry.insert(tk.END,"入力して下さい")
# entry.pack()


# tkm.showwarning("警告","はいやったなお前")

button = tk.Button(root,text="押すな",font=("",40))
button.bind("<1>",button_click)
button.pack()





root.mainloop()#rootはインスタンス


