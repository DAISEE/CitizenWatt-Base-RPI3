#!/usr/bin/env bash
# Prerequisites install script
# Launch as root

aptitude update

# Install Python
aptitude install -y python3 gcc python3-pip python3-dev

# Install packages
aptitude install -y postgresql supervisor avahi-daemon redis-server iptables-persistent
aptitude install -y postgresql-server-dev-all

# Python modules
aptitude install -y python3-numpy python3-cherrypy3
pip3 install requests sqlalchemy pycrypto psycopg2 redis
