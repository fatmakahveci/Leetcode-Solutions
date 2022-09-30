# Read from the file file.txt and output the tenth line to stdout.

lineNo=$(cat file.txt | wc -l)

if [ $lineNo -gt 9 ]; then head -10 file.txt | tail -1; fi
