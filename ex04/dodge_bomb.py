import pygame as pg
import sys

def main():
    #練習1
    pg.display.set_caption("逃げろ！こうかとん")#タイトルバーに表記
    scrn_sfc = pg.display.set_mode((1450,900))#1600x900の画面Surfaceを生成
    

    


    #背景画像貼り付け
    bg_sfc = pg.image.load("pg_bg.jpg")
    bg_rect = bg_sfc.get_rect()#Rect


    #練習3
    tori_sfc = pg.image.load("fig/3.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc,0,2.0)
    tori_rct = tori_sfc.get_rect() #Rect
    tori_rct.center = 900,400
    

    clock = pg.time.Clock()

  

    while True:
        #練習2
        scrn_sfc.blit(bg_sfc,bg_rect)#背景貼り付け
        

        for event in pg.event.get():
            if event.type == pg.QUIT: return

        key_stats = pg.key.get_pressed()
        if key_stats[pg.K_UP]: tori_rct.centery -= 3
        if key_stats[pg.K_DOWN]: tori_rct.centery += 3
        if key_stats[pg.K_LEFT]: tori_rct.centerx -= 3
        if key_stats[pg.K_RIGHT]: tori_rct.centerx += 3
        
       

        scrn_sfc.blit(tori_sfc,tori_rct)#こうかとん貼り付け


        pg.display.update()#ディスプレイ表示のアップデート
        clock.tick(1000)
    

if __name__ == "__main__":
    pg.init()#モジュール初期化
    main()#ゲーム本体
    pg.quit()#初期化の解除
    sys.exit()

