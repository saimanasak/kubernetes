```yaml
# deploy-nginx.yaml

apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-nginx-deploy
  labels:
    app: nginx-deploy  
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
  replicas: 3
  selector:
    matchLabels: 
      app: nginx-pod      
```

### Overview:
- The above manifest defines a Deployment named my-nginx-deploy that manages 3 replicas of Pods, each running an NGINX container. 
- It uses labels to identify which Pods it manages and allows for scaling, updating, and self-healing of the NGINX application.

### Explanation:
```yaml
apiVersion: apps/v1
```
- This specifies the API version of the Kubernetes resource. 
- For Deployments, the appropriate version is apps/v1. 
- This ensures compatibility with the Kubernetes cluster.

```yaml
kind: Deployment
```
- This defines the type of Kubernetes resource being created. Here, it is a Deployment.

```yaml
metadata:
  name: my-nginx-deploy
  labels:
    app: nginx-deploy  
```
- **metadata**: This section contains information about the Deployment.
- **name**: Specifies the name of the Deployment. Here, it's named my-nginx-deploy.
- **labels**: Labels are key-value pairs that can be used for identifying and grouping resources. Here, the Deployment is labeled with app: nginx-deploy, which helps in organizing and selecting resources in Kubernetes.

```yaml
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
  replicas: 3
  selector:
    matchLabels: 
      app: nginx-pod 
```
- **spec**: This section outlines the desired state for the Deployment.
- **template**: This defines the Pod template that will be used by the Deployment to create Pods.
- **replicas**: Defines the desired number of identical Pods to be maintained by the Deployment. 3 replicas of the Pod will be created and managed by the Deployment.
- **selector**: This defines how the Deployment finds which Pods to manage.
- **matchLabels**: It specifies that the Deployment should manage Pods with the label app: nginx-pod. This label should match the labels defined in the Pod template. If a Pod does not have this label, it won't be managed by this Deployment.

### Create Deployment:
- Syntax to create using the manifest:
```bash
kubectl create -f manifest_name
kubectl apply -f manifest_name
```

- Use the below command to create the deployment from the above manifest:
```bash
kubectl create -f deploy-nginx.yaml
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/deployments/basic-deploy-nginx/images/create_deploy.png)

### Status of Deployment:
- Syntax to check the deployment:
```bash
# To get deployment for a defualt namespace
kubectl get deployment 

# To get deployment for a specific namespace
kubectl get deployment -n namespace
```

- Use the below command to get the status of deployment:
```bash
kubectl get deployment
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/deployments/basic-deploy-nginx/images/get_deploy.png)

- Use the below command to verify the pods:
```bash
kubectl get pods
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/deployments/basic-deploy-nginx/images/get_initial_pods_deploy.png)

### View Deployment Details:
- Syntax to view the details of a specific deployment:
```bash
kubectl describe deployment deploy_name
```

- Use the below command to describe the created deployment:
```bash
kubectl describe deployment my-nginx-deploy
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/deployments/basic-deploy-nginx/images/describe_deploy.png)

### Deleting Pod & Verify:
- Use the below command to delete the pod:
```bash
kubectl delete pod 
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/deployments/basic-deploy-nginx/images/delete_pod_deploy.png)

- Use the below command to verify the pods that again new pod is created or not:
```bash
kubectl get pods
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/deployments/basic-deploy-nginx/images/after_pods_deploy.png)

### Delete Deployment:
- Syntax to delete the deployment:
```bash
kubectl delete deployment deploy_name
```

- Use the below command to delete the above created deployment:
```bash
kubectl delete deployment my-nginx-deploy
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/deployments/basic-deploy-nginx/images/delete_deploy.png)

> **_NOTE_**:
> 
> Can use both **deployment** and **deploy** in the commands.