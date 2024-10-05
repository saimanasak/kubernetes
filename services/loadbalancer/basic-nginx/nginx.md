```yaml
# nginx.yaml

apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deploy
  labels:
    app: nginx-lb 
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
  type: LoadBalancer
  ports:
  - targetPort: 80
    port: 80
  selector:
    app: nginx-pod
```

### Overview:
- This configuration defines a Kubernetes Deployment named nginx-deploy, managing two replicas of an NGINX pod to ensure high availability. 
- Each pod runs a single container using the official NGINX image and is labeled as app: nginx-pod. 
- A Kubernetes Service named my-service is created with type LoadBalancer, exposing the NGINX pods to external traffic on port 80. 
- The Service routes traffic to the pods labeled with app: nginx-pod, enabling access to the NGINX web server from outside the cluster via the load balancer’s external IP.

### Explanation:
- The first part is:
    - Creates a Deployment with 2 replicas of an NGINX container, ensuring high availability by running multiple instances of the nginx pod.
    - The Deployment manages the lifecycle of pods, ensuring that the specified number of pods (2) are always running, and they can be updated or scaled easily.
    
- The second part is for the Service.
```yaml
spec:
  type: LoadBalancer
  ports:
  - targetPort: 80
    port: 80
  selector:
    app: nginx-pod
```
- This spec configuration establishes a LoadBalancer service that listens on port 80, forwards traffic to the target port 80 of the NGINX pods, and selects those pods based on the specified label. 
- This setup allows external users to access the NGINX service through the load balancer.

### Create:
- Create the deployment and service using the above manifest:
```bash
kubectl create -f nginx.yaml
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/services/loadbalancer/basic-nginx/images/create.png)

### Check Objects:
- Check the status of the above created objects using:
```bash
kubectl get all

kubectl get deploy

kubectl get pods

kubectl get services
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/services/loadbalancer/basic-nginx/images/get-all.png)

### Accessing NGINX:
- Generally, we can access the nginx with the external IP of the service using the below command:
```bash
http://<external-IP>
```

- Here, If you are running Minikube and have set the service type to LoadBalancer, you need to use minikube tunnel to expose the service properly since Minikube does not support LoadBalancer out of the box.
```bash
minikube tunnel
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/services/loadbalancer/basic-nginx/images/tunnel.png)

- Commands to use, in this case:
```bash
minikube tunnel

http://localhost
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/services/loadbalancer/basic-nginx/images/output-nginx.png)