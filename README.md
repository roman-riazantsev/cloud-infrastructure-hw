### Instruction how to run Docker:

Build a container:
```
docker build -t romanriazantsev/cloud-infrastructure-hw .
```

Run a container:
```
docker run -p 80:80 romanriazantsev/cloud-infrastructure-hw
```

Site was launched at the localhost:80 . By clicking the button, a notification will be displayed asking you to confirm the launch of the calculation. After the calculation is completed, the "print result" button will appear, which, upon click, will write an array of numbers and the number of iterations.

### Instruction how to run Kubernetes:
#### (You can run bash.sh to skip this part.)

Start minikube:
```
minilube start
```

Create deployment:
(POD, replication)
```
kubectl create -f deployment.yml
```

Create service:
(Gives access to the container.)
```
kubectl create -f service.yml
```

Now our service is available at http://192.168.99.100:30303.



