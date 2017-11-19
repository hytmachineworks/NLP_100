UNIXコマンドを用いて確認せよ．
1.コーパス中で頻出する述語と格パターンの組み合わせ
awk -F'[ \t]+' '{for (i = 1; i <= NF; i++) if (i != 1) print($1 " " $i);}' neko_predicate_case.txt | sort | uniq -c | sort -n -r > neko_count.txt

2.「する」「見る」「与える」という動詞の格パターン（コーパス中で出現頻度の高い順に並べよ）
awk -F'[ \t]+' '$1 ~ /^(する|見る|与える)/ {for (i = 1; i <= NF; i++) if (i != 1) print($1 " " $i);}' neko_predicate_case.txt | sort | uniq -c | sort -n -r > neko_verb_count.txt
