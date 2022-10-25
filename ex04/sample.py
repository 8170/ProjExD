import pygame as pg
import sys

def main():
    pg.display.set_caption("初めてのPyGame")#タイトルバーに表記
    scrn_sfc = pg.display.set_mode((800,600))#800x600の画面Surfaceを生成
    #Surfaceオブジェクト生成


    tori_sfc = pg.image.load("fig/6.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc,0,2.0)
    tori_rct = tori_sfc.get_rect() #Rect
    tori_rct.center = 700,400
    scrn_sfc.blit(tori_sfc,tori_rct)#スクリーンに貼り付け

    


    pg.display.update()
    clock = pg.time.Clock()
    clock.tick(0.2)
    

if __name__ == "__main__":
    pg.init()#モジュール初期化
    main()#ゲーム本体
    pg.quit()#初期化の解除
    sys.exit()

