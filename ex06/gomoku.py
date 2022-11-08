# -*- coding:utf-8 -*-

import tkinter
import tkinter.messagebox
import random

#キャンバスの横方向・縦方向サイズ
canvas_size = 400

#ライン数
num_line = 10

#色設定
board_color = "burlywood3" #半面の配色
your_color = "black" #自分の石の色
computer_color = "white" #相手の石の色

#プレイヤー示す値
you = 1
computer = 2


class Gobang():
    def __init__(self,master):
        self.master = master #親ウィジェット
        self.player = you #次に置く石の色
        self.board = None #盤面上の意思を管理する2次元リスト
        self.color = {you:your_color,computer:computer_color} #石の色を保持する辞書
        self.nextDisk = None

        #ウィジェット作成
        self.createWidgets()

        #イベントの設定
        self.setEvents()

        #五目並べゲームの初期化
        self.initGobang()

    def createWidgets(self):
        #ウィジェット作成・配置

        #キャンバスの作成
        self.canvas = tkinter.Canvas(
            self.master,
            bg = board_color,
            width = canvas_size,
            height = canvas_size,
            heiglightthickness = 0
        )
        
        self.canvas.pack(padx=10,pady=10)

    def setEvents(self):
        #イベント設定する

        #キャンバス上のマウスクリックイベントを受付
        self.canvas.bind("<ButtonPress>",self.click)

    def initGobang(self):
        #ゲームの初期化を行う

        #盤面上の石を管理する2次元リストを作成(最初はNone)
        self.board = [[None] * (num_line) for i in range(num_line)]

        #線と線の間隔を計算
        self.interval = canvas_size // (num_line + 1)

        #交点描画位置の左上のオフセット
        self.offset_x = self.interval
        self.offset_y = self.interval

        #縦線を描画
        for x in range(num_line):
            
            #線の開始、終了座標を計算
            xs = x * self.interval + self.offset_x
            ys = self.offset_y
            xe = xs
            ye = (num_line - 1) * self.interval + self.offset_y

            #線の描画
            self.canvas.create_line(
                xs, ys,
                xe, ye,
            )

        #横線を描画
        for y in range(num_line):

            #線の開始・終了座標を計算
            xs = self.offset_x
            ys = y * self.interval + self.offset_y
            xe = (num_line - 1) * self.interval + self.offset_x
            ye = ys

            #線を描画
            self.canvas.create_line(
                xs,ys,
                xe,ye,
            )
        
    def drawDisk(self,x,y,color):
            #(x,y)の公転に色がcolorの石を置く(円の描画)

        #(x,y)の交点の中心座標を計算
        center_x = x * self.interval + self.offset_x
        center_y = y * self.interval + self.offset_y

            #中心座標から円の開始座標と終了座標を計算
        xs = center_x - (self.interval * 0.8) // 2
        ys = center_y - (self.interval * 0.8) // 2
        xe = center_x + (self.interval * 0.8) // 2
        ye = center_y + (self.interval * 0.8) // 2

            #円を描画する
        tag_name = "disk_" + str(x) + "_" + str(y)
        self.canvas.create_oval(
            xs,ys,
            xe,ye,
            fill = color,
        )

        return tag_name

    def getIntersection(self,x,y):
        #キャンバス乗の座標を交点の位置に変換

        ix = (x - self.offset_x + self.interval // 2) // self.interval
        iy = (y - self.offset_y + self.interval // 2) // self.interval

        return ix,iy

    def click(self,event):
        #盤面がクリックされた時の処理

        if self.player != you:
            #computerの操作時は何もしない
            return

        #クリックされた位置がどの交差であるかを計算
        x,y = self.getIntersection(event.x,event.y)

        if x < 0 or x >= num_line or y < 0 or y >= num_line:
            #盤面外の交差の場合は何もしない
            return

        if not self.board[y][x]:
            #石が置かれていない場合はクリックされた位置に石を置く

            #石を置く
            self.place(x,y,self.color[self.player])

    def place(self,x,y,color):
        #(x,y)の交点に色がcolorの石を置く

        #(x,y)に石を置く
        self.drawDisk(x,y,color)

        #描画した円の色を管理リストに記憶
        self.board[y][x] = color

        #5つ並んだかチェック
        if self.count(x,y,color) >= 5:
            self.showResult()
            return
        
        #プレイヤーは交互に変更
        if self.player == computer:
            self.player = you
        else:
            self.player = computer

        if self.player == computer:
            #次のプレイヤーがcomputerの場合は1秒後に石を置く場所を決めさせる
            self.master.after(1000,self.computer)

    def count(self,x,y,color):
        #(x,y)に色がcolorの石を置いた時の石並び数をチェック

        count_dir = [
            (1,0),
            (1,1),
            (0,1),
            (-1,1),
        ]

        max = 0#石の並び数の最大値

        #count_dirの方向に対して石の並び数をチェック
        for i,j in count_dir:
            count_num = 1

            for s in range(1,num_line):
                xi = x + i * s
                yj = y + j * s

                if xi < 0 or xi >= num_line or yj < 0 or yj >= num_line:
                    break

                if self.board[yj][xi] != color:
                    break

                count_num += 1

            for s in range(-1,-(num_line),-1):
                xi = x + i * s
                yi = y + j * s

                if xi < 0 or xi >= num_line or yj < 0 or yj >= num_line:
                    break

                if self.board[yj][xi] != color:
                    break

                count_num += 1

            if max < count_num:
                max = count_num

        return max

    def showResult(self):
        #ゲーム終了時の結果を表示

        #勝利者は先程石を置いたプレイヤー
        win = self.player

        if win == you:
            tkinter.messagebox.showinfo("result","your win")
        else:
            tkinter.messagebox.showinfo("result","your lose")

    def computer(self):
        #コンピューターに石を置かせる

        #相手が石を置いた時に石が最大で連続する交点の座標を取得
        max_list = []
        max = 0
        for y in range(num_line):
            for x in range(num_line):
                if not self.board[y][x]:
                    count_num = self.count(x,y,self.color[you])
                if count_num == max:
                    max_list.append((x,y))
                elif count_num > max:
                    max_list = []
                    max_list.append((x,y))
                    max = count_num

        choice = random.randrange(len(max_list))
        x,y = max_list[choice]

        self.place(x,y,computer_color)

app = tkinter.Tk()
app.title("五目並べ")
gobang = Gobang(app)
app.mainloop()

        


        