echo "source /vagrant/*/.env" >> ~/.profile
echo "export $(cut -d= -f1 /vagrant/*/.env) > /dev/null" >> ~/.profile
sudo echo "source /vagrant/*/.env" >> ~/.profile
sudo echo "export $(cut -d= -f1 /vagrant/*/.env) > /dev/null" >> ~/.profile