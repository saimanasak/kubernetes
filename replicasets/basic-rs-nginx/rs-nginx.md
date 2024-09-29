```yaml
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: my-nginx-rs
  labels:
    app: nginx-rs 
spec:
  template:
    metadata:
      name: my-nginx-pod
      labels:
        app: mynginx
    spec:
      containers:
      - name: nginx-container
        image: nginx
  replicas: 3
  selector: 
    matchLabels:
      app: mynginx
```

### Overview:
- The above YAML defines a Kubernetes ReplicaSet named my-nginx-rs that ensures 3 replicas of an Nginx pod are running.
- The ReplicaSet manages pods with the label app: mynginx and creates new ones if they don't exist.
- Each pod runs a container using the nginx image, defined in the pod template within the ReplicaSet.

### Explanation:
```yaml
apiVersion: apps/v1
```
- Specifies the version of the Kubernetes API to use for creating the object. 
- Here, apps/v1 is used for managing applications, and it's the API version for objects like ReplicaSet, Deployment, etc.

```yaml
kind: ReplicaSet
```
- Specifies the type of Kubernetes resource you're defining. 
- A ReplicaSet, which is responsible for ensuring a specified number of pod replicas are running at all times.

```yaml
metadata:
  name: my-nginx-rs
  labels:
    app: nginx-rs
```
- **metadata**: Contains metadata about the ReplicaSet object such as its name and labels.
- **name: my-nginx-rs**: Unique name given to this ReplicaSet, my-nginx-rs.
- **labels**: Are key-value pairs attached to this ReplicaSet that can be used for organization and identification purposes. Labels are often used for selecting and querying resources.
- **app: nginx-rs**: A label that tags the ReplicaSet with an app label with the value nginx-rs. This is used for grouping and identifying objects (such as this ReplicaSet) under this label.

```yaml
spec:
  template:
    metadata:
      name: my-nginx-pod
      labels:
        app: mynginx
    spec:
      containers:
      - name: nginx-container
        image: nginx
  replicas: 3
  selector: 
    matchLabels:
      app: mynginx
```
- **spec**: Defines the desired behavior of the ReplicaSet, including the pod template, replica count, and how to match pods with labels.
- **template**: Defines the pod specification that will be used to create the replicas. It contains metadata and specification for the pods that will be created.
- **replicas: 3**: The desired number of pod replicas that the ReplicaSet should maintain. In this case, Kubernetes will ensure that 3 pods are running at any time.
- **selector**: Defines how the ReplicaSet knows which pods to manage. It uses label selectors to match pods.
- **matchLabels**: Specifies the key-value pairs the ReplicaSet uses to select the pods it manages. The ReplicaSet will look for pods that have matching labels.
- **app: mynginx**: Indicates that the ReplicaSet should only manage pods that have this label. This must match the app: mynginx label that is defined in the pod template.

### Create ReplicaSet:
- Syntax to create using the manifest:
```bash
kubectl create -f manifest_name
kubectl apply -f manifest_name
```

- Use the below command to create the replicaset from the above manifest:
```bash
kubectl create -f rs-nginx.yaml
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/replicasets/basic-rs-nginx/images/create_rs.png)

### Status of ReplicaSet:
- Syntax to check the replicaset:
```bash
# To get rs for a defualt namespace
kubectl get rs 

# To get rs for a specific namespace
kubectl get rs -n namespace
```

- Use the below command to get the status of replicaset:
```bash
kubectl get rs
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/replicasets/basic-rs-nginx/images/get_rs.png)

- Use the below command to verify the pods:
```bash
kubectl get pods
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/replicasets/basic-rs-nginx/images/initial_get_pods.png)

### View ReplicaSet Details:
- Syntax to view the details of a specific replicaset:
```bash
kubectl describe rs rs_name
```

- Use the below command to describe the created replicaset:
```bash
kubectl describe rs my-nginx-rs
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/replicasets/basic-rs-nginx/images/rs_describe.png)

### Deleting Pod & Verify:
- Use the below command to delete the pod:
```bash
kubectl delete pod 
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/replicasets/basic-rs-nginx/images/delete_pod.png)

- Use the below command to verify the pods that again new pod is created or not:
```bash
kubectl get pods
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/replicasets/basic-rs-nginx/images/get_pods.png)

### Delete ReplicaSet:
- Syntax to delete the replicaset:
```bash
kubectl delete rs rs_name
```

- Use the below command to delete the above created rs:
```bash
kubectl delete rs my-nginx-rs
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/replicasets/basic-rs-nginx/images/delete_rs.png)

### Scaling:
- Various ways to scale:
```bash
kubectl scale --replicas=5 -f replicaset_name

kubectl scale --replicas=5 replicaset replicaset_name
```

> **_NOTE_**:
> 
> Can use both **replicaset** and **rs** in the commands.  