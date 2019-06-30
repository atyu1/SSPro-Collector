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

install: deploy build-container 

deploy:
	@echo "Copying files"
	scp -r ./* atyu@$(IP):/tmp

#Create a docker container
build-container:
	ssh atyu@$(IP) $(DOCKERBUILDCMD) -t atyu1/ssp-collector -f /tmp/Dockerfile .
#Run a container
run:
	@echo "Not implemented" 

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
	

