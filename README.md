# msi_dn3
Image zbuildamo z
```
docker build -t flaskapp:v1 .
```
še prej nastavimo environment variable z "eval $(minikube docker-env)" tako da bo image narejen z dockerjem od minikuba
<br>
na začetku ustvarimo persistent volume za mongo
```
kubectl apply -f volume.yaml
kubectl apply -f volumeclaim.yaml
```
za ustvarit app zaženemo deploymente in service za vse storitve
```
kubectl apply -f deployments_init.yaml
kubectl apply -f services_init.yaml
```
aplikacija lahko dostopamo na naslovu flask service-a

![curl](https://github.com/xao1215/msi_dn3/blob/main/c.PNG)

Če zaženemo ingress je sedaj dostopna tudi preko load-balancerja na 127.0.0.1
```
kubectl apply -f ingress.yaml
```

![curl](https://github.com/xao1215/msi_dn3/blob/main/d.PNG)

<br>

za blue-green deployment update zaženemo nov deployment in service

```
kubectl apply -f deployment_bluegreen.yaml
kubectl apply -f service_v2.yaml
```

![stanje po ukazu](https://github.com/xao1215/msi_dn3/blob/main/a.PNG)
če posodobimo configuracijo za ingress lako takoj dostopamo do nove verzije aplikacije
![ingress2](https://github.com/xao1215/msi_dn3/blob/main/e.PNG)


za rolling update zaženemo nov deployment
```
kubectl apply -f deployment_rolling.yaml
```
![stanje po ukazu](https://github.com/xao1215/msi_dn3/blob/main/b.PNG)

flask aplikacija rabi 5 sekund preden začne delovat, zato liveness in readiness probe počakata 7 sekund preden začneta poizvedovat po stanju poda vsakih 5 sekund.
<br>

