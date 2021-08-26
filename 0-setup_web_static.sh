#!/usr/bin/env bash
# Sets up web servers
sudo apt-get -y update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'
chown -R "$USER:$USER" /var/www/html

directories=(/data/ /data/web_static/ /data/web_static/releases/ /data/web_static/releases/test/)
for i in "${directories[@]}"; do if [[ ! -d "$i" ]]; then mkdir "$i" ; fi; done

echo "Holberton School" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i "42i\ \n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default
service nginx restart
