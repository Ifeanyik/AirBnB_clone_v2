#!/usr/bin/env bash
# this script sets up web servers for deployment of web_static
if ! command -v nginx &> /dev/null
then
	sudo apt-get -y update
	sudo apt-get -y install nginx
	sudo service nginx start
fi
if [ ! -d '/data/' ]
then
	sudo mkdir - p '/data/'
fi
if [ ! -d '/data/web_static/' ]
then
	sudo mkdir -p '/data/web_static'
fi
if [ ! -d '/data/web_static/releases/' ]
then
	sudo mkdir -p '/data/web_static/releases/'
fi
if [ ! -d '/data/web_static/shared/' ]
then
	sudo mkdir -p '/data/web_static/shared/'
fi
if [ ! -d '/data/web_static/releases/test/' ]
then
	sudo mkdir -p '/data/web_static/releases/test/'
fi
echo -e '<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHolberton School\n\t</body>\n</html>' | sudo tee /data/web_static/releases/test/index.html > /dev/null
if [ -L ${/data/web_static/current} ]
then
	sudo rm -r /data/web_static/current
	ln -s /data/web_static/releases/test/ /data/web_static/current
else
	ln  -s /data/web_static/releases/test/ /data/web_static/current
fi
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n' /etc/nginx/sites-available/default
exit 0
