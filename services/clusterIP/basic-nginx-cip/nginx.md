```yaml
# nginx.yaml

apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deploy
  labels:
    app: nginx-cip 
spec:
  template:
    metadata:
      name: my-nginx-pod
      labels:
        app: nginx-pod
    spec:
      containers:
      - name: nginx-container
        image: nginx
  replicas: 2
  selector:
    matchLabels:
      app: nginx-pod
      
---

apiVersion: v1 
kind: Service
metadata:
  name: my-service
spec:
  type: ClusterIP
  ports:
  - targetPort: 80
    port: 80
  selector:
    app: nginx-pod
```

### Overview:
- This configuration defines a Kubernetes Deployment and a ClusterIP Service for NGINX. 
- The Deployment specifies the creation of two replicas of the NGINX pod, which will use the NGINX image. 
- Each pod is labeled with app: nginx-pod, allowing the service to identify and route traffic to these pods. 
- The ClusterIP Service, named my-service, exposes the NGINX pods internally within the cluster, listening on port 80 and forwarding requests to the pods’ target port 80. 
- This setup allows for internal communication between pods while keeping them inaccessible from outside the cluster.

### Create:
- Create the deployment and service using the above manifest:
```bash
kubectl create -f nginx.yaml
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/services/clusterIP/basic-nginx-cip/images/create.png)

### Check Objects:
- Check the status of the above created objects using:
```bash
kubectl get all

kubectl get deploy

kubectl get pods

kubectl get services
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/services/clusterIP/basic-nginx-cip/images/get-all.png)

### Accessing NGINX:
- Get the pods:
```bash
kubectl get pods -o wide
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/services/clusterIP/basic-nginx-cip/images/pods-wide.png)

- Now, try to access the second pod from the first pod:
```bash
kubectl exec -it <pod-name> -- sh

curl http://<second-pod-IP>
```

- In this case:
```bash
kubectl exec -it nginx-deploy-747df65b64-6w5c6 -- sh

curl http://10.244.0.33
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/services/clusterIP/basic-nginx-cip/images/output.png)