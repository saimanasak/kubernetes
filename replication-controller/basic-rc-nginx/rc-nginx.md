```yaml
# rc-nginx.yaml

apiVersion: v1
kind: ReplicationController
metadata:
  name: my-nginx-rc
  labels:
    app: nginx-rc 
spec:
  replicas: 3
  template:
    metadata:
      name: my-nginx-pod
      labels:
        app: mynginx
    spec:
      containers:
      - name: nginx-container
        image: nginx
```

### Overview:
- The above manifest defines a ReplicationController in Kubernetes, named my-nginx-rc, that ensures 3 pod replicas are always running. 
- Each of these pods will run an NGINX container. 
- If any pod crashes, the ReplicationController will automatically start a new one to maintain 3 running instances. 
- The pods are labeled for easy identification and management (app: mynginx) and these labels can be used later.

### Explanation:

```yaml
apiVersion: v1
```
- This line specifies the API version of the Kubernetes resource being created. v1 means that this YAML file adheres to version 1 of the Kubernetes API.
- It tells Kubernetes which API version to use when handling this manifest.

```yaml
kind: ReplicationController
```
- This defines the type of Kubernetes object you are creating. Here, it's a ReplicationController. 

```yaml
metadata:
  name: my-nginx-rc
  labels:
    app: nginx-rc
```
- **metadata**: This section contains metadata, which is information used to describe or identify the object (ReplicationController). Metadata is important for organizing, searching, and managing resources.  
- **name: my-nginx-rc**: The name field under metadata specifies the name of the ReplicationController. The name is my-nginx-rc, and it must be unique within the Kubernetes namespace. This name helps identify the ReplicationController and can be used when querying or interacting with it.
- **labels**: Labels are key-value pairs that are used to organize and categorize Kubernetes resources. They help identify, filter, and manage resources across the cluster.
- **app: nginx-rc**: This is a label assigned to the ReplicationController itself. It consists of a key (app) and a value (nginx-rc). This label can be used later to select this ReplicationController for management purposes or to group it with other resources that have the same label.

```yaml
spec:
  replicas: 3
  template:
    metadata:
      name: my-nginx-pod
      labels:
        app: mynginx
    spec:
      containers:
      - name: nginx-container
        image: nginx
```
- **spec**: The spec field defines the desired state of the ReplicationController. It contains configuration details about how many pods should be running, and what these pods should look like.
- **replicas: 3**: This line specifies that the ReplicationController should maintain 3 replicas of the pod. In other words, at any given time, there should be 3 running instances (pods) of the application defined in this YAML. If any pod dies, the ReplicationController will create a new one to ensure 3 replicas are always available.
- **template**: The template describes the pods that the ReplicationController will create. Every time a new pod is launched by this ReplicationController, it will follow the configuration provided here. The template section contains both metadata and a specification for the pods.

### Create the Replication Controller:
- Syntax to create the replication controller using the manifest:
```bash
kubectl create -f manifest_name
kubectl apply -f manifest_name
```

- Below command to create a pod using the above manifest file:
```bash
kubectl create -f rc-nginx.yaml
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/replication-controller/rc-nginx/images/create_rc.png)

### RC Verification:
- Syntax to check the replication controller:
```bash
# To get rc for a defualt namespace
kubectl get rc 

# To get rc for a specific namespace
kubectl get rc -n namespace
```

- Below command to get the above created replication controller:
```bash
kubectl get rc
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/replication-controller/rc-nginx/images/get_rc.png)

- Use the below command to verify the pods:
```bash
kubectl get pods
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/replication-controller/rc-nginx/images/initial_get_pods.png)

### View Replication Controller Details:
- Syntax to view the details of a specific replication controller:
```bash
kubectl describe rc rc_name
```

- Use the below command to describe the created replication controller:
```bash
kubectl describe rc my-nginx-rc
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/replication-controller/rc-nginx/images/describe_rc.png)

### Deleting Pod & Verify:
- Use the below command to delete the pod:
```bash
kubectl delete pod 
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/replication-controller/rc-nginx/images/delete_pod.png)

- Use the below command to verify the pods that again new pod is created or not:
```bash
kubectl get pods
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/replication-controller/rc-nginx/images/new_get_pods.png)

### Delete Replication Controller:
- Syntax to delete the replication controller:
```bash
kubectl delete rc rc_name
```

- Use the below command to delete the above created rc:
```bash
kubectl delete rc my-nginx-rc
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/replication-controller/rc-nginx/images/delete_rc.png)

> NOTE:
> 
> Can use both **replicationcontroller** and **rc** in the commands.  