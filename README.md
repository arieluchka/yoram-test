# ez-joy

## Manual build procedure

1. build the Dockerfile   
```
docker build -t ez-easy-easy/ez-joy:<version> .
```      

2. run the unit-test(s)   
```
pytest ...
```      

3. build the HELM chart   
```
helm package ...
```      
      
4. deploy the Docker-image and HELM-chart to DockerHub
```
docker login
docker push ez-easy-easy/ez-joy:<version>
helm push ....
```
