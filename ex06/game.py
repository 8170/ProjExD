# -*- coding:utf-8 -*-
import tkinter
import tkinter.messagebox
import random

# キャンバスの横方向・縦方向のサイズ（px）
CANVAS_SIZE = 400

# ラインの数
NUM_LINE = 10

# 色の設定
BOARD_COLOR = 'burlywood3' # 盤面の背景色
YOUR_COLOR = 'red' # あなたの石の色
COM_COLOR = 'blue' # 相手の石の色

# プレイヤーを示す値
YOU = 1
aite = 2



class Gobang():
    def __init__(self, master):
        '''コンストラクタ'''

        self.master = master # 親ウィジェット
        self.player = YOU # 次に置く石の色
        self.board = None # 盤面上の石を管理する２次元リスト
        self.color = { # 石の色を保持する辞書
            YOU : YOUR_COLOR,
            aite : COM_COLOR
        }
        self.nextDisk = None

        # ウィジェットの作成
        self.createWidgets()

        # イベントの設定
        self.setEvents()

        # 五目並べゲームの初期化
        self.initGobang()

       

    def createWidgets(self):
        '''ウィジェットを作成・配置する'''

        # キャンバスの作成
        self.canvas = tkinter.Canvas(
            self.master,
            bg=BOARD_COLOR,
            width=CANVAS_SIZE,
            height=CANVAS_SIZE,
            highlightthickness=0
        )
        self.canvas.pack(padx=10, pady=10)

        #画像表示
        self.bg_image = tkinter.PhotoImage(file="gamingtori.PNG")
        self.canvas.create_image(
            CANVAS_SIZE / 2,
            CANVAS_SIZE / 2,
            image=self.bg_image
        )

        
    def setEvents(self):
        '''イベントを設定する'''

        # キャンバス上のマウスクリックイベントを受け付ける
        self.canvas.bind('<ButtonPress>', self.click)


    def initGobang(self):
        '''ゲームの初期化を行う'''

        # 盤面上の石を管理する２次元リストを作成（最初は全てNone）
        self.board = [[None] * (NUM_LINE) for i in range(NUM_LINE)]

        # 線と線の間隔（px）を計算
        self.interval = CANVAS_SIZE // (NUM_LINE + 1)

        # 交点描画位置の左上オフセット
        self.offset_x = self.interval
        self.offset_y = self.interval

        # 縦線を描画
        for x in range(NUM_LINE):
 
            # 線の開始・終了座標を計算
            xs = x * self.interval + self.offset_x
            ys = self.offset_y
            xe = xs
            ye = (NUM_LINE - 1) * self.interval + self.offset_y
                
            # 線を描画
            self.canvas.create_line(
                xs, ys,
                xe, ye,
            )

        # 横線を描画
        for y in range(NUM_LINE):
 
            # 線の開始・終了座標を計算
            xs = self.offset_x
            ys = y * self.interval + self.offset_y
            xe = (NUM_LINE - 1) * self.interval + self.offset_x
            ye = ys
                
            # 線を描画
            self.canvas.create_line(
                xs, ys,
                xe, ye,
            )


    def drawDisk(self, x, y, color):
        '''(x,y)の交点に色がcolorの石を置く（円を描画する）'''

        # (x,y)の交点の中心座標を計算
        center_x = x * self.interval + self.offset_x
        center_y = y * self.interval + self.offset_y

        # 中心座標から円の開始座標と終了座標を計算
        xs = center_x - (self.interval * 0.8) // 2
        ys = center_y - (self.interval * 0.8) // 2
        xe = center_x + (self.interval * 0.8) // 2
        ye = center_y + (self.interval * 0.8) // 2
        
        # 円を描画する
        tag_name = 'disk_' + str(x) + '_' + str(y)
        self.canvas.create_oval(
            xs, ys,
            xe, ye,
            fill=color,
        )

        return tag_name

    def getIntersection(self, x, y):
        '''キャンバス上の座標を交点の位置に変換'''

        ix = (x - self.offset_x + self.interval // 2) // self.interval
        iy = (y - self.offset_y + self.interval // 2) // self.interval

        return ix, iy

    def click(self, event):
        '''盤面がクリックされた時の処理'''
        
        # クリックされた位置がどの交点であるかを計算
        x, y = self.getIntersection(event.x, event.y)

        if x < 0 or x >= NUM_LINE or y < 0 or y >= NUM_LINE:
            # 盤面外の交点の場合は何もしない
            return

        if not self.board[y][x]:
            # 石が置かれていない場合はクリックされた位置に石を置く

            # 石を置く
            self.place(x, y, self.color[self.player])

    def place(self, x, y, color):
        '''(x,y)の交点に色がcolorの石を置く'''

        # (x,y)に石を置く（円を描画する）
        self.drawDisk(x, y, color)

        # 描画した円の色を管理リストに記憶させておく
        self.board[y][x] = color
        
        # ５つ並んだかどうかをチェック
        if self.count(x, y, color) >= 5:
            self.showResult()
            return

        # プレイヤーは交互に変更
        if self.player == aite:
            self.player = YOU
            #message = tkinter.Message(self.master,text="プレイヤー2のターンです")
            #message.pack()
        else:
            self.player = aite
            #message = tkinter.Message(self.master,text="プレイヤー1のターンです")
            #message.pack()

        # if self.player == aite:
        #     # 次のプレイヤーがCOMの場合は1秒後にCOMに石を置く場所を決めさせる
        #     self.master.after(1000, self.com)


    def count(self, x, y, color):
        '''(x,y)に色がcolorの石を置いた時の石の並び数をチェック'''

        # チェックする方向をリストに格納
        count_dir = [
            (1, 0), # 右
            (1, 1), # 右下
            (0, 1), # 上
            (-1, 1), # 左下
        ]

        max = 0 # 石の並び数の最大値

        # count_dirの方向に対して石の並び数をチェック
        for i, j in count_dir:

            # 石の並び数を1に初期化
            count_num = 1

            # (x,y)から現在の方向に対して１交点ずつ遠ざけながら石が連続しているかをチェック
            for s in range(1, NUM_LINE):
                
                xi = x + i * s
                yj = y + j * s

                if xi < 0 or xi >= NUM_LINE or yj < 0 or yj >= NUM_LINE:
                    # 盤面外の交点の場合は石は連続していない
                    break

                if self.board[yj][xi] != color:
                    # 異なる色の石が置かれていれば石は連続していない
                    break

                # 上記以外の場合は石が連続している
                count_num += 1

            # 次は逆方向をチェック
            for s in range(-1, -(NUM_LINE), -1):
                xi = x + i * s
                yj = y + j * s

                if xi < 0 or xi >= NUM_LINE or yj < 0 or yj >= NUM_LINE:
                    break

                if self.board[yj][xi] != color:
                    break

                count_num += 1

            # 最大値の置き換え
            if max < count_num:
                max = count_num
        
        # 石が連続している数の最大値を返却
        return max

    def showResult(self):
        '''ゲーム終了時の結果を表示する'''

        # 勝利者は先ほど石を置いたプレイヤー
        winner = self.player

        # 結果をメッセージボックスで表示する
        if winner == YOU:
            tkinter.messagebox.showinfo('結果', 'プレイヤー1の勝ちです')
        else:
            tkinter.messagebox.showinfo('結果', 'プレイヤー2の勝ちです')

    def com(self):
        '''COMに石を置かせる'''

        # 相手が石を置いた時に石が最大で連続する交点の座標を取得
        max_list = []
        max = 0
        for y in range(NUM_LINE):
            for x in range(NUM_LINE):
                if not self.board[y][x]:
                    # (x,y)座標に相手が石を置いた場合に石が連続する数を取得
                    count_num = self.count(x, y, self.color[YOU])
                    if count_num == max:
                        max_list.append((x, y))
                    elif count_num > max:
                        max_list = []
                        max_list.append((x, y))
                        max = count_num

        # 石が連続する数が最大になる交点の中から１つの座標をランダムに取得
        choice = random.randrange(len(max_list))
        x, y = max_list[choice]

        # 石を置く
        self.place(x, y, COM_COLOR)

# スクリプト処理ここから
app = tkinter.Tk()
app.title('五目並べ')
gobang = Gobang(app)
app.mainloop()