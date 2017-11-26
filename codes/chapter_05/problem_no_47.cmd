UNIXコマンドを用いて確認せよ．
1.コーパス中で頻出する述語（サ変接続名詞+を+動詞）
cut -f 1 neko_predicate_mining.txt  | sort | uniq -c | sort -n -r > neko_mining_count.txt


2.コーパス中で頻出する述語と助詞パターン
awk -F'[ \t]+' '{for (i = 1; i <= NF; i++) if (i != 1) print($1 " " $i);}' neko_predicate_mining.txt | sort | uniq -c | sort -n -r > neko_mining_freq.txt
