# 第二回
## 電卓を作成する(ex02/calc.py)
### 追加機能
- クリアボタン:entryに入力されいている数字、数式の1文字を削除する。
- オールクリアボタン:entryに入力されている数字、数式の文字列全てを削除する。
- 四則演算機能追加
- 3限の講義で電卓の機能として追加した+以外の四則演算を追加。
- 私のオリジナリティ追及するために0で割った時の反応と演算子を同時に複数入力した時にtkinterのメッセージボックスで表現している
- 仮に0で割った時、警告文として「あなたは計算を知りませんね」と表示される。
- また、演算子を同時に複数入力したときには、警告文として「計算が苦手ですか？」と表示される。
- 2乗ができるモノを機能を追加

### TODO(実装しようと思ったが時間がなかった)
- 平方根,sin,con,tanへの変換機能
- パーセンテージ表示



### メモ
- 新しくブランチを作るコマンドは [git branch ブランチ名]
- ブランチを切り替えるコマンドは [git switch ブランチ名]
- mainブランチに戻るコマンドは [git switch main]
- ブランチを切り替える前に、全ての変更履歴をコミットした方がいい