# nifi-docker
Automated nifi container that creates flows from templates.

Once Nifi starts the scripts will locate all of the templates in the 
mounted /app/templates folder and turn them into a running process group.

## Requirements
* docker
* make

## Let's get started (fast version)
```shell script
make make deploy-nifi-templates
```

You can then use your browser to view the running Nifi at ```localhost:8080/nifi```

## Wait, what just happened?

The steps are:
1. Build a docker image that has nifi and python3 (```make nifi-image```)
1. Bring up a docker stack (```make docker-up```)
1. Wait for Nifi to finish starting (```make nifi-ready```)
1. Use a python script to deploy the templates (```make deploy-nifi-templates```)
1. Have a look at it in your browser (no make command for that sorry. Just go to http://localhost:8080/nifi)
1. Tear it all down (```make docker-down```)
