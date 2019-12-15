# ------ VARIABLES ------------
DOCKERBUILDCMD=docker build
DOCKERRUNCMD=docker run
DOCKERNAME=atyu/sspro-collector
GOMAINFILE=main
NAME=collector

# ------- MAIN SECTION ---------
help:
	@echo "all    - build go for linux + docker container"
	@echo "run    - start docker container"
	@echo "clean  - remove go binaries + containers"
	@echo "push   - git push commits to git"
	@echo "test-local - test localy the code"

all: install

install: deploy build run 

deploy:
	@echo "Copying files to $(IP)"
	scp -r ./* atyu@$(IP)

#Create a docker container on remote place
build:
	ssh atyu@$(IP) $(DOCKERBUILDCMD) -t atyu1/ssp-collector -f Dockerfile .

run:
	@echo "Starting the container with name: $(NAME)"
	$(DOCKERRUNCMD) --rm -it --name $(NAME)

clean:
	@echo "Clean containers on $(IP)" 
	ssh atyu@$(IP) "docker system prune -f"
	@echo "Clean home dir on $(IP)"
	ssh atyu@$(IP) "rm -rf ~/*"

push:
	git push -u origin master

#------ TESTS ------
test-local: test-local-api

test-local-api:
	curl http://localhost:$(PORT)/test
	

