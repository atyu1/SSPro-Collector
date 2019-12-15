# ------ VARIABLES ------------
DOCKERBUILDCMD=docker build
DOCKERRUNCMD=docker run
DOCKERNAME=atyu/sspro-collector
GOMAINFILE=main
NAME=collector
REMOTE=atyu@$(IP)
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
	$(SSHREMOTE) $(DOCKERBUILDCMD) -t $(DOCKERNAME) -f Dockerfile .

run:
	@echo "Starting the container with name: $(NAME)"
	$(SSHREMOTE) "$(DOCKERRUNCMD) -d --name $(NAME) $(DOCKERNAME)"
	$(SSHREMOTE) "docker logs $(NAME)"
	$(SSHREMOTE) "docker rm -f $(NAME)"

clean:
	@echo "Clean containers on $(IP)" 
	$(SSHREMOTE) "docker system prune -f"
	@echo "Clean home dir on $(IP)"
	$(SSHREMOTE) "rm -rf ~/*"

push:
	git push -u origin master
