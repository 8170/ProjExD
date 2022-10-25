from random import random
import pygame as pg
import sys
import random

def check_bound(obj_rct,scr_rct):
    """
    こうかとんrctまたは爆弾rctを想定している+スクリーンのrct
    領域内ないなら+1、領域外なら-1
    """
    yoko,tate = 1,1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
      
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
     
    return (yoko,tate)




def main():
    #練習1 3限講義
    pg.display.set_caption("逃げろ！こうかとん")#タイトルバーに表記
    scrn_sfc = pg.display.set_mode((1450,900))#1600x900の画面Surfaceを生成
    scrn_rct = scrn_sfc.get_rect()

    


    #背景画像貼り付け
    bg_sfc = pg.image.load("pg_bg.jpg")
    bg_rect = bg_sfc.get_rect()#Rect


    #練習3　3限講義
    tori_sfc = pg.image.load("fig/3.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc,0,2.0)
    tori_rct = tori_sfc.get_rect() #Rect
    tori_rct.center = 900,400

    tori_out_sfc = pg.image.load("fig/8.png")
    tori_out_sfc = pg.transform.rotozoom(tori_sfc,0,2.0)
    tori_out_rct = tori_out_sfc.get_rect() #Rect

    #練習5　3限講義
    bomb_sfc = pg.Surface((20,20))#描画用(20x20)
    bomb_sfc.set_colorkey((0,0,0))#四隅の部分を透過
    pg.draw.circle(bomb_sfc,(255,0,0),(10,10),10)#円描画(中心10x10)半径10
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = random.randint(0,scrn_rct.width)
    bomb_rct.centery = random.randint(0,scrn_rct.height)

    #追加機能（爆弾の増加）
    bomb_brother_sfc = pg.Surface((100,100))#描画用(20x20)
    bomb_brother_sfc.set_colorkey((0,0,0))#四隅の部分を透過
    pg.draw.circle(bomb_brother_sfc,(255,0,255),(50,50),50)#円描画(中心10x10)半径10
    bomb_brother_rct = bomb_brother_sfc.get_rect()
    bomb_brother_rct.centerx = random.randint(0,scrn_rct.width)
    bomb_brother_rct.centery = random.randint(0,scrn_rct.height)

    bomb_sister_sfc = pg.Surface((50,50))#描画用(20x20)
    bomb_sister_sfc.set_colorkey((0,0,0))#四隅の部分を透過
    pg.draw.circle(bomb_sister_sfc,(0,0,255),(25,25),25)#円描画(中心10x10)半径10
    bomb_sister_rct = bomb_sister_sfc.get_rect()
    bomb_sister_rct.centerx = random.randint(0,scrn_rct.width)
    bomb_sister_rct.centery = random.randint(0,scrn_rct.height)


    #練習6　3限講義
    vx,vy = 1,1
    vx_b,vy_b = 5,5
    vx_c,vy_c = 1.2,1.2


    

    clock = pg.time.Clock()

  

    while True:
        #練習2　3限講義
        scrn_sfc.blit(bg_sfc,bg_rect)#背景貼り付け
        

        for event in pg.event.get():
            if event.type == pg.QUIT: return

        key_stats = pg.key.get_pressed()
        if key_stats[pg.K_UP]: 
            tori_rct.centery -= 3
            if tori_rct.colliderect(bomb_sister_rct):
                tori_rct.centery -= 10
            if tori_rct.colliderect(bomb_brother_rct):
                tori_rct.centery += 10

        if key_stats[pg.K_DOWN]: 
            tori_rct.centery += 3
            if tori_rct.colliderect(bomb_sister_rct):
                tori_rct.centery += 10
            if tori_rct.colliderect(bomb_brother_rct):
                tori_rct.centery -= 10

        if key_stats[pg.K_LEFT]: 
            tori_rct.centerx -= 3
            if tori_rct.colliderect(bomb_sister_rct):
                tori_rct.centerx -= 10
            if tori_rct.colliderect(bomb_brother_rct):
                tori_rct.centerx += 10

        if key_stats[pg.K_RIGHT]: 
            tori_rct.centerx += 3
            if tori_rct.colliderect(bomb_sister_rct):
                tori_rct.centerx += 10
            if tori_rct.colliderect(bomb_brother_rct):
                tori_rct.centerx -= 10

        
        #練習7　3限講義
        yoko,tate = check_bound(tori_rct,scrn_rct)
        if yoko == -1:
            if key_stats[pg.K_LEFT]:
                tori_rct.centerx += 3
            if key_stats[pg.K_RIGHT]:
                tori_rct.centerx -= 3
        if tate == -1:
            if key_stats[pg.K_UP]:
                tori_rct.centery += 3
            if key_stats[pg.K_DOWN]:
                tori_rct.centery -= 3

    
            
        scrn_sfc.blit(tori_sfc,tori_rct)#こうかとん貼り付け


        #練習7　3限講義
        yoko,tate = check_bound(bomb_rct,scrn_rct)#移動判定(爆弾)
        vx *= 1.0005
        vy *= 1.0005
        vx *= yoko 
        vy *= tate 
        bomb_rct.move_ip(vx,vy)

        yoko,tate = check_bound(bomb_brother_rct,scrn_rct)#移動判定(爆弾)
        vx_b *= yoko
        vy_b *= tate
        bomb_brother_rct.move_ip(vx_b,vy_b)
    

        yoko,tate = check_bound(bomb_sister_rct,scrn_rct)#移動判定(爆弾)
        vx_c *= yoko
        vy_c *= tate
        bomb_sister_rct.move_ip(vx_c,vy_c)



        scrn_sfc.blit(bomb_sfc,bomb_rct)#爆弾貼り付け

        scrn_sfc.blit(bomb_brother_sfc,bomb_brother_rct)#爆弾兄弟貼り付け

        scrn_sfc.blit(bomb_sister_sfc,bomb_sister_rct)

        

        #練習8　3限講義
        if tori_rct.colliderect(bomb_rct): 
            tori_sfc = pg.image.load("fig/8.png")
            tori_sfc = pg.transform.rotozoom(tori_sfc,0,2.0)
            scrn_sfc.blit(tori_sfc,tori_rct)
            pg.display.update()
            clock.tick(0.5)
            return

    



        pg.display.update()#ディスプレイ表示のアップデート
        clock.tick(1000)
    

if __name__ == "__main__":
    pg.init()#モジュール初期化
    main()#ゲーム本体
    pg.quit()#初期化の解除
    sys.exit()

