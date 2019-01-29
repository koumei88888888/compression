# compression
Study of can_log compression
canのログを圧縮して流す

log: ログファイルからID毎にピックアップしたログファイルを生成
add0.py: CANアナライザからログ出力した時に勝手に消えるIDの先頭の0を付与
canid.txt: 対象とするcanのIDのリスト（今使ってない）
count_id.py: IDごとにログ中に出現したIDの数をカウント
field_XOR.py: ログ中の同一IDの前後で差分をとる
huffman_hex.py: ハフマン符号化されたIDを1オクテットのサイズになるように0埋めする(使ってない)
huffman_hex_id.csv: huffman_hex.pyにより生成
huffman_id.csv: huffman_id.pyにより生成
huffman_id.py: CANIDをハフマン符号化する
id_num.txt: count_id.pyにより生成
id_probability.py: CANID毎に出現頻度を算出
id_probability.txt: id_probability.pyにより生成
pickup_ID.c: logフォルダ内のファイルを生成 
run_length: ペイロードをランレングス符号化する
yuki_1230s_field.csv: 元ログファイル
yuki_1230s_id.csv: ログファイルからIDだけをピックアップしたファイル
yuki_1230s_xor.csv: field_XORにより生成

書いてないの→テスト用に作ったスクリプト
