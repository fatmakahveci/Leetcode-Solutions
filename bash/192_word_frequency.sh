cat words.txt | (tr ' ' '\n' ) | tr -s '\n' | sort | uniq -c | sort -hr | awk -c '{print $2" "$1}'
