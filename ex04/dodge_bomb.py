import pygame as pg
import sys

def main():
    #練習1
    pg.display.set_caption("逃げろ！こうかとん")#タイトルバーに表記
    scrn_sfc = pg.display.set_mode((1450,900))#1600x900の画面Surfaceを生成
    

    


    #背景画像貼り付け
    bg_sfc = pg.image.load("pg_bg.jpg")
    bg_rect = bg_sfc.get_rect()#Rect

    clock = pg.time.Clock()

    while True:
        #練習2
        scrn_sfc.blit(bg_sfc,bg_rect)
        pg.display.update()

        for event in pg.event.get():
            if event.type == pg.QUIT: return

        clock.tick(1000)
    

if __name__ == "__main__":
    pg.init()#モジュール初期化
    main()#ゲーム本体
    pg.quit()#初期化の解除
    sys.exit()

