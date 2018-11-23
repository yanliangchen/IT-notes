#!/usr/bin/env bash

## set docker 
function set_docker () {
## install docker
curl -sSL https://get.daocloud.io/docker | sh

## install docker-compose
[ -f /usr/local/bin/docker-compose ] || \
curl -L https://get.daocloud.io/docker/compose/releases/download/1.23.1/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose && \
chmod +x /usr/local/bin/docker-compose


## use daocloud docker registy 
if [ ! -f /etc/docker/daemon.json ]; then
	curl -sSL https://get.daocloud.io/daotools/set_mirror.sh | sh -s http://f1361db2.m.daocloud.io
	/usr/bin/systemctl restart docker
fi
}

function make_compose () {
## local ENV setting
SPHINX_DIR=$(dirname "$PWD")
HTML_DIR=$(find ${SPHINX_DIR} -name index.html -exec dirname {} \;)

## write docker compose
cat << EOF > docker-compose.yml
version: '3'
services: 

  html:
    container_name: sphinx-cicd
    network_mode: "none"
    image: sphinx:1.6.4-apline3.8
    build:
      context: .
      dockerfile: Dockerfile
    volumes:
      - "${SPHINX_DIR}:/usr/src/sphinx"
    
  web:
    container_name: nginx-cicd
    image: nginx:1.14-alpine
    restart: always
    ports:
      - "80:80"
    volumes:
      - "${HTML_DIR}:/usr/share/nginx/html"
EOF

## run container
cd ${SPHINX_DIR}/docker/ && docker-compose -f docker-compose.yaml build
}

case $1 in
	set)
	set_docker
	;;
	make)
	make_compose
	;;
	*)
	echo "Usage: $0 {set|make}"
        exit 1
	;;
esac
