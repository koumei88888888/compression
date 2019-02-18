# compression
Study of can_log compression
canのログを圧縮して流す

MP_to_dump: MPのログを圧縮する形式に変換
add0.py: CANアナライザからログ出力した時に勝手に消えるIDの先頭の0を付与
canid.txt: 対象とするcanのIDのリスト（今使ってない）
client.py: socket通信のクライアント側
compression_A.py: 大平方式A
compression_A_plus.py: 大平方式A+
compression_koumei.py: 提案方式
count_id.py: IDごとにログ中に出現したIDの数をカウント
data_ways.py: 指定IDの指定バイト列に出現する値の種類と個数を出力
field_XOR.py: ログ中の同一IDの前後で差分をとる
huffman_hex.py: ハフマン符号化されたIDを1オクテットのサイズになるように0埋めする(使ってない)
huffman_id.py: CANIDをハフマン符号化したリストを生成
huffmaning.py: ハフマン符号化したファイルを生成
id_probability.py: CANID毎に出現頻度を算出
id_to_bin.py: IDをバイナリ化
pickup_ID.c: logフォルダ内のファイルを生成 
run_length.py: ペイロードをランレングス符号化する
xor_Time: 時間の差分をID毎に分けず、行ごとに計算