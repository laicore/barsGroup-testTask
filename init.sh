#sudo systemctl start mysql

mysql -uroot -proot -e "create database testBarsdb"
mysql -uroot -proot -e "create user 'boxBars'@'localhost' IDENTIFIED WITH mysql_native_password BY 'boxBars'"
mysql -uroot -proot -e "grant all on testBarsdb.* to 'boxBars'@'localhost'
python3 ~/barsGroup-testTask/siths/manage.py migrate