# 第5回
## 負けるな！こうかとん(ex05/fight_koukaton.py)
### ゲーム概要
- ex05/fight_koukaton.pyを実行すると、1600x900のスクリーンに草原が描画され、こうかとんを移動させ飛び回る爆弾から逃げるゲーム
-こうかとんがばくだんと接触するとゲームオーバーで終了する
### 操作方法
- 矢印キーでこうかとんを上下左右に移動する
### 追加機能
- chimpクラス　ゲームエリア内にチンパンジーの画像が表示 ぶつかったらゲームオーバー
- チンパンジー(敵)　攻撃の妨げを行う
- 腕(見方) 見方の手伝い
- こうかとんが腕の画像に触れたら拡大する。ある一定の拡大までいくとゲームクリア!!!!
- しかし、チンパンジーは腕の拡大率を下げる効果があるのでチンパンジーを避けながら腕を成長させていく必要がある。
- 腕の成長は運ゲーかと思われるが、運も実力の内！己の力で勝ちきれ！！！！１！！
### 追加したかった機能
- こうかとんから球が発射する
### メモ
クラス内の関数を自由に使用するにはself.が必要である。