# ------ VARIABLES ------------
DOCKERBUILDCMD=docker build
DOCKERRUNCMD=docker run
DOCKERNAME=atyu/sspro-collector
GOMAINFILE=main

# ------- MAIN SECTION ---------
help:
	@echo "all    - build go for linux + docker container"
	@echo "run    - start docker container"
	@echo "clean  - remove go binaries + containers"
	@echo "push   - git push commits to git"
	@echo "test-local - test localy the code"

install: build-linux build-container 

#Build go package for linux platform
build-linux:
	@echo "Not implemented" 

#Create a docker container
build-container:
	@echo "Not implemented" 

#Run a container
run:
	@echo "Not implemented" 
#ToDo: Add deploy 

#Clean binaries + conatiners
clean:
	@echo "Not implemented" 
	docker system prune -f

push:
	git push -u origin master

#------ TESTS ------
test-local: test-local-api

test-local-api:
	curl http://localhost:$(PORT)/test
	

