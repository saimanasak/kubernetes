```yaml
# nginx.yaml

apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deploy
  labels:
    app: nginx-np 
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
  type: NodePort
  ports:
  - targetPort: 80
    port: 80
    nodePort: 30001
  selector:
    app: nginx-pod
```

### Overview:
- The Deployment creates and manages 2 replicas of an NGINX container to ensure high availability.
- Pods are labeled app: nginx-pod, which allows them to be selected by the Service for traffic routing.
- The Service of type NodePort exposes the NGINX pods on port 30001 across all cluster nodes.
- Traffic from outside the cluster on nodePort 30001 is forwarded to port 80 inside the NGINX containers.

### Explanation:
- The first part is:
    - Creates a Deployment with 2 replicas of an NGINX container, ensuring high availability by running multiple instances of the nginx pod.
    - The Deployment manages the lifecycle of pods, ensuring that the specified number of pods (2) are always running, and they can be updated or scaled easily.
    
- The second part is for the Service.
```yaml
spec:
  type: NodePort
  ports:
  - targetPort: 80
    port: 80
    nodePort: 30001
  selector:
    app: nginx-pod
```
- **type: NodePort**: It exposes the service externally on a specific port across each node in the cluster. This allows traffic from outside the cluster to reach the pods. 
- **targetPort: 80**: Inside the pod, the container's port 80 (where NGINX listens) will receive traffic from the service.
- **port: 80**: This is the port on the Service itself that will route traffic to the pods. When other services within the cluster communicate with this service, they use this port.
- **nodePort: 30001**: The port exposed on every node in the cluster (or Minikube's node in your case). You can access the service from outside the cluster by using any node's IP address and this port.
- **selector**: Matches this service to the pods with the label app: nginx-pod. The service will route traffic to all pods that match this label, which are the NGINX pods created by your Deployment.

### Create:
- Create the deployment and service using the above manifest:
```bash
kubectl create -f nginx.yaml
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/services/nodeport/basic-nginx-np/images/create.png)

### Check Objects:
- Check the status of the above created objects using:
```bash
kubectl get all

kubectl get deploy

kubectl get pods

kubectl get services
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/services/nodeport/basic-nginx-np/images/get_all.png)

### Accessing NGINX:
- Generally, we can access the nginx using the below command:
```bash
http://<node-IP>:nodePort
```

- Here, Minikube provides a command to directly route traffic to the service and open it in your browser:
```bash
minikube service service-name

minikube service service-name --url
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/services/nodeport/basic-nginx-np/images/minikube-svc.png)

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/services/nodeport/basic-nginx-np/images/minikube-svc-url.png)

- Commands to use, in this case:
```bash
minikube service my-service

minikube service my-service --url
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/services/nodeport/basic-nginx-np/images/output-nginx.png)