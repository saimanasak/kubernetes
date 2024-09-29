```yaml
# nginx-pod.yaml

apiVersion: v1
kind: Pod
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
- The above manifest/definition/configuration file defines a Pod named my-nginx-pod, which runs a single container called nginx-container, using the nginx image. 

### Explanation:

```yaml
apiVersion: v1
```
- This specifies the version of the Kubernetes API you're using to create the object. Here, v1 is the version for core resources like Pods.
- It tells Kubernetes which API version to use when handling this manifest.

```yaml
kind: Pod
```
- The kind field specifies what type of Kubernetes resource you're defining. In this case, it's a Pod, which is the smallest deployable unit in Kubernetes.  
- It defines the object type.

```yaml
metadata:
  name: my-nginx-pod
  labels:
    app: mynginx
```
- **metadata**: This section holds metadata about the Pod, including its name and labels. Metadata provides information to help identify and categorize the Pod.
- **name: my-nginx-pod**: This is the name of the Pod. It's a unique identifier within the Kubernetes namespace. The Pod's name allows you to reference this specific Pod.  
- **labels**: Labels are key-value pairs that can be attached to Kubernetes objects like Pods for easy identification. Labels are used for organizing and selecting subsets of objects like in a service or deployment.
- **app: mynginx**: This is a label key (app) with the value mynginx. This label can be used to identify this Pod as part of an application, which may consist of multiple resources.

```yaml
spec:
  containers:
  - name: nginx-container
    image: nginx
```
- **spec**: This section defines the desired state or specification of the Pod, including the containers it runs. It holds the main configuration of the Pod. 
- **containers**: This section lists the containers that will run inside the Pod. A Pod can have one or more containers. Containers define the application code or services that the Pod will run. 
- **name: nginx-container**: This is the name of the container inside the Pod. It helps identify this specific container within the Pod.  
- **image: nginx**: Specifies the Docker image that will be used for this container. In this case, the container uses the nginx image from a Docker registry. It tells Kubernetes which container image to run. The nginx image is a popular web server.

### Create Pod:
- Syntax to create the pod using the manifest:
```bash
kubectl apply -f manifest_name
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/pods/pod-nginx/screenshots/create_pod.png)

- Below command to create a pod using the above manifest file:
```bash
kubectl apply -f nginx-pod.yaml
```

### Pod Verification:
- Syntax to check the pods:
```bash
# To get pods for a defualt namespace
kubectl get pods

# To get pods for a specific namespace
kubectl get pods -n namespace

# To get all the pods across all namespaces
kubectl get pods -A
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/pods/pod-nginx/screenshots/get_pods.png)

### View Pod Details:
- Syntax to view the pod details:
```bash
kubectl describe pod pod_name -n namespace
```

- To check the above pod details:
```bash
kubectl describe pod my-nginx-pod
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/pods/pod-nginx/screenshots/describe_pod.png)

### Delete Pod:
- Syntax to delete the pod:
```bash
kubectl delete pod pod_name -n namespace
```

- To delete the above pod:
```bash
kubectl delete pod my-nginx-pod
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/pods/pod-nginx/screenshots/delete_pod.png)