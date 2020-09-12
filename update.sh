echo removing the old script
sleep 1s

rm -r yousseftool.py
sleep 1s
echo updating

pkg install wget 

wget https://raw.githubusercontent.com/youhacker55/yousseftermux/master/yousseftool.py
sleep 1s
echo updated

figlet enjoy
