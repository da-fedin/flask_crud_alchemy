# Contains a set of instructions (targets) to automate tasks related to building, managing, and deploying container.

.PHONY: docker-proj-run
# Make all actions needed for run homework from zero.
docker-proj-run:
	@make init-configs &&\
	make docker-run

.PHONY: docker-proj-purge
# Make all actions needed for purge homework related data.
docker-proj-purge:
	@make docker-purge


.PHONY: init-configs
# Configuration files initialization
init-configs:
	@cp docker-compose.override.dev.yml docker-compose.override.yml


.PHONY: docker-run
# Just run
docker-run:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
		docker compose up --build

.PHONY: docker-stop
# Stop services
docker-stop:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
		docker compose down

.PHONY: docker-purge
# Purge all data related with services
docker-purge:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
		docker compose down --volumes --remove-orphans --rmi local --timeout 0

#.PHONY: init-dev
## Init environment for development
#init-dev:
#	@pip install --upgrade pip && \
#	pip install --requirement requirements.txt && \
#	pre-commit install

.PHONY: run
# Run project.
run:
	@python app.py

.PHONY: purge
# Purge project.
purge:
	@echo Goodbye

.PHONY: build-project-linux
# Build project
build-project-linux:
	@echo '----- Build run -----'
	@chmod +x scripts/build.sh
	@scripts/build.sh
	@echo '----- Build done -----'

.PHONY: pre-commit-run
# Run tools for files from commit.
pre-commit-run:
	@pre-commit run

.PHONY: pre-commit-run-all
# Run tools for all files.
pre-commit-run-all:
	@pre-commit run --all-files
