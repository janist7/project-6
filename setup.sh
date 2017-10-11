apt-get -qqy update
apt-get -qqy upgrade
locale-gen en_US
locale-gen en_US.UTF-8
update-locale
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
apt-get -qqy install libapache2-mod-wsgi-py3
apt-get -qqy install libpq-dev
apt-get -qqy install nodejs
apt-get -qqy install npm
apt-get -qqy install libffi-dev
apt-get -qqy install libssl-dev
apt-get -qqy install python3
apt-get -qqy install python3-pip
apt-get -qqy install build-essential
apt-add-repository ppa:brightbox/ruby-ng -y
apt-get -qqy update
apt-get -qqy install ruby2.3 ruby2.3-dev libsqlite3-dev
npm install bower -g
gem install -q mailcatcher
pip3 install --upgrade pip
pip3 install virtualenv
ln -s /usr/bin/nodejs /usr/bin/node
ln -s /sites /var/www/html/
cd /sites/*/
virtualenv env
make init
make assets
make clean