apt-get -qqy update
apt-get -qqy upgrade
apt-get -qqy install memcached
apt-get -qqy install redis-server
apt-get -qqy install make
apt-get -qqy install zip
apt-get -qqy install git
apt-get -qqy install unzip
apt-get -qqy install postgresql
apt-get -qqy install pgadmin3
apt-get -qqy install python-psycopg2
apt-get -qqy install apache2
apt-get -qqy install libapache2-mod-wsgi
apt-get -qqy install libpq-dev
apt-get -qqy install python-dev
apt-get -qqy install nodejs
apt-get -qqy install npm
sudo apt-get install libffi-dev
sudo apt-get install libssl-dev
sudo apt-get install python3
sudo apt-get install python3-pip
apt-get -qqy  install build-essential
apt-add-repository ppa:brightbox/ruby-ng -y
apt-get -qqy update
apt-get -qqy install ruby2.3 ruby2.3-dev libsqlite3-dev
apt-get -qqy install python
apt-get -qqy install python-pip
npm install bower -g
gem install -q mailcatcher
pip2 install --upgrade pip
cd /vagrant/*/
apt-get -qqy install language-pack-UTF-8
locale-gen UTF-8
ln -s /usr/bin/nodejs /usr/bin/node
make init
make assets
make clean
