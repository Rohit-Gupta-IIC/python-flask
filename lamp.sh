#sudo apt update
#sudo apt upgrade -y
#sudo apt install -y apache2 apache2-utils
#systemctl status apache2
#sudo systemctl start apache2
#sudo systemctl enable apache2
#apache2 -v
#sudo iptables -I INPUT -p tcp --dport 80 -j ACCEPT
#sudo ufw allow http
#sudo chown www-data:www-data /var/www/html/ -R
#sudo apt install mariadb-server mariadb-client
#systemctl status mariadb
#sudo systemctl start mariadb
#sudo systemctl enable mariadb
#sudo mysql_secure_installation
#sudo mariadb -u root
#mariadb --version
#sudo apt install -y php7.2 libapache2-mod-php7.2 php7.2-mysql php-common php7.2-cli php7.2-common php7.2-json php7.2-opcache php7.2-readline
#sudo a2enmod php7.2
#sudo systemctl restart apache2
#php --version
#sudo nano /var/www/html/info.php
