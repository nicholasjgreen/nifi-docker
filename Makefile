.PHONY: nifi-image
nifi-image:
	docker build -t nick/nifi:latest .

.PHONY: docker-up
docker-up: nifi-image
	docker-compose up -d

.PHONY: nifi-ready
nifi-ready: docker-up
	docker-compose exec nifi python3 /app/scripts/wait_for_nifi.py >/dev/null

.PHONY: deploy-nifi-templates
deploy-nifi-templates: nifi-ready
	docker-compose exec nifi python3 /app/scripts/deploy_all_templates.py

.PHONY: docker-down
docker-down:
	docker-compose down

all: nifi-image docker-up nifi-ready
