apt-get update
apt-get upgrade
apt-get -qqy install memcached
apt-get -qqy install redis-server
apt-get -qqy install make
apt-get -qqy install zip
apt-get -qqy install git
apt-get -qqy install unzip
apt-get -qqy install postgresql
apt-get -qqy install pgadmin3
apt-get -qqy install python-psycopg2
apt-get -qqy install libpq-dev
apt-get -qqy install python-dev
apt-get -qqy install nodejs
apt-get -qqy install npm
npm install bower -g
#apt-get -qqy install python3
#apt-get -qqy install python3-pip
#pip3 install --upgrade pip
#pip3 install flask packaging oauth2client redis passlib flask-httpauth
#pip3 install sqlalchemy flask-sqlalchemy psycopg2 bleach requests
apt-get -qqy install python
apt-get -qqy install python-pip
pip2 install --upgrade pip
pip2 install flask
pip2 install packaging
pip2 install oauth2client
pip2 install redis
pip2 install passlib
pip2 install flask-httpauth
pip2 install sqlalchemy
pip2 install flask-sqlalchemy
pip2 install psycopg2
pip2 install bleach
pip2 install requests
apt-add-repository ppa:brightbox/ruby-ng
apt-get install -y ruby2.3 ruby2.3-dev libsqlite3-dev
gem install mailcatcher
cd /vagrant/*/
ln -s /usr/bin/nodejs /usr/bin/node
make init
make assets
make clean