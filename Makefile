# ------ VARIABLES ------------
DOCKERBUILDCMD=docker build
DOCKERRUNCMD=docker run
DOCKERNAME=atyu/sspro-collector
GOMAINFILE=main
NAME=collector
REMOTE="atyu@$(IP)"
SSHREMOTE=ssh $(REMOTE)
SCPREMOTE="$(REMOTE):~/"

# ------- MAIN SECTION ---------
all: install

install: deploy build run 

deploy:
	@echo "Copying files to $(IP)"
	scp -r ./src/ $(SCPREMOTE)
	scp Dockerfile $(SCPREMOTE)
	scp requirements.txt $(SCPREMOTE)

#Create a docker container on remote place
build:
	ssh $(SSHREMOTE) $(DOCKERBUILDCMD) -t $(DOCKERNAME) -f Dockerfile .

run:
	@echo "Starting the container with name: $(NAME)"
	$(DOCKERRUNCMD) --rm -it --name $(NAME)

clean:
	@echo "Clean containers on $(IP)" 
	$(SSHREMOTE) "docker system prune -f"
	@echo "Clean home dir on $(IP)"
	$(SSHREMOTE) "rm -rf ~/*"

push:
	git push -u origin master
