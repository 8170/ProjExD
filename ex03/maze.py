import tkinter as tk
import maze_maker as mm
import tkinter.messagebox as tkm
import random

# 練習5
def key_down(event):
    global key
    key = event.keysym


# 練習6
def key_up(event):
    global key
    key = ""

def key_goal(event):
    key = event.keysym
    tkm.showinfo("おめでとう",f"あなたはごーるしました！！！！！！")
    root.destroy()
    


def main_proc():
    global mx,my
    global cx, cy
    global tori,f_lst
    if key == "Up":
        my -= 1
    if key == "Down":
        my += 1
    if key == "Left":
        mx -= 1
    if key == "Right":
        mx += 1
        #tori = tk.PhotoImage(file=random.choice(f_lst))
    if maze_lst[my][mx] == 0:
        cx,cy = mx*100+50,my*100+50
    else:
        if key == "Up":
            my += 1
        if key == "Down":
            my -= 1
        if key == "Left":
            mx += 1
        if key == "Right":
            mx -= 1
    if my == 7 and mx == 13:
        root.bind("<KeyPress>",key_goal)
    canv.coords("tori", cx, cy)
    root.after(100, main_proc)



if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん") # 練習1

    # 練習2
    canv = tk.Canvas(root, width=1500, height=900, bg="black")
    canv.pack()


    #練習9
    maze_lst = mm.make_maze(15,9)
    f_lst = ["./ex03/fig/9.png""./ex03/fig/0.png""./ex03/fig/1.png""./ex03/fig/2.png""./ex03/fig/3.png""./ex03/fig/4.png""./ex03/fig/5.png""./ex03/fig/6.png""./ex03/fig/7.png","./ex03/fig/8.png"]

    #練習10
    mm.show_maze(canv,maze_lst)

    # 練習3
    tori = tk.PhotoImage(file="./ex03/fig/9.png") #画像を変更しました。
    mx,my = 1,1#マス番号
    cx, cy = mx*100+50,my*100+50#座標
    canv.create_image(cx, cy, image=tori, tag="tori")

    label = tk.Label(root,text="START",font=("",20))
    label.place(x=105,y=140)

    label1 = tk.Label(root,text="GOAL",font=("",20))
    label1.place(x=7*100,y=13*100)

    # 練習4
    key = "" # 現在押されているキーを表す

    # 練習5,6
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)    

    # 練習7
    main_proc()

    



    root.mainloop()