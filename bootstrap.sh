apt-get update
apt-get upgrade
apt-get install memcached
apt-get -qqy install redis-server
apt-get -qqy install make zip unzip postgresql python-psycopg2 libpq-dev
apt-get -qqy install python3 python3-pip
apt-get -qqy install python-dev
apt-get -qqy install nodejs
apt-get -qqy install npm
npm install bower -g
pip3 install --upgrade pip
pip3 install flask packaging oauth2client redis passlib flask-httpauth
pip3 install sqlalchemy flask-sqlalchemy psycopg2 bleach requests
apt-get -qqy install python python-pip
pip2 install --upgrade pip
pip2 install flask packaging oauth2client redis passlib flask-httpauth
pip2 install sqlalchemy flask-sqlalchemy psycopg2 bleach requests
apt-add-repository ppa:brightbox/ruby-ng
apt-get install -y ruby2.3 ruby2.3-dev libsqlite3-dev
gem install mailcatcher
echo 'if [ -n "$BASH_VERSION" ]; then
		if [ -f "/vagrant/*/.env" ]; then
        	. "/vagrant/*/.env"
    	fi
	fi' >> ~/.profile
source /vagrant/*/.env
export $(cut -d= -f1 /vagrant/*/.env)