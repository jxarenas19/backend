deploy::
	git fetch origin
	git checkout develop
	git pull
	docker-compose up -d --build