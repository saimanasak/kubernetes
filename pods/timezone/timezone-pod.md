```yaml
apiVersion: v1
kind: Pod
metadata:
  name: timezone-pod
spec:
  containers:
  - name: nginx-container
    image: nginx
    volumeMounts:
    - name: timezone
      mountPath: /etc/localtime  
      subPath: Asia/Kolkata
  volumes:
  - name: timezone
    hostPath:
      path: /usr/share/zoneinfo
```

### Overview:

- The above manifest defines a pod named timezone-pod that runs a single NGINX container. 
- The pod is configured to mount the local timezone file for Asia/Kolkata from the host system into the container at /etc/localtime.
- This setup ensures that the application inside the pod operates with the correct timezone settings, allowing for accurate time management and logging based on the specified timezone.

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
  name: timezone-pod
```
- **metadata**: This section holds metadata about the Pod, including its name and labels. Metadata provides information to help identify and categorize the Pod.
- **name: timezone-pod**: This is the name of the Pod. It's a unique identifier within the Kubernetes namespace. The Pod's name allows you to reference this specific Pod.  

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

```yaml
    volumeMounts:
    - name: timezone
      mountPath: /etc/localtime  
      subPath: Asia/Kolkata
  volumes:
  - name: timezone
    hostPath:
      path: /usr/share/zoneinfo
```
- **volumeMounts**: This section defines the volumes to mount inside the container.
- **name: timezone**: Refers to the name of the volume being mounted (defined later in the manifest).
- **mountPath: /etc/localtime**: Specifies the path inside the container where the volume will be mounted. In this case, it mounts to /etc/localtime, which is the standard location for timezone information in Linux systems.
- **subPath: Asia/Kolkata**:  Indicates a specific file or directory to mount from the volume. Here, it mounts the Asia/Kolkata timezone file from the host's timezone data.
- **volumes**: This section defines the volumes that can be mounted by containers in the pod.
- **name: timezone**: Names the volume timezone, which will be referenced in the volumeMounts section.
- **hostPath**: Specifies that this volume type refers to a directory on the host machine.
- **path: /usr/share/zoneinfo**: Points to the directory on the host filesystem that contains timezone files. In this case, it points to /usr/share/zoneinfo, which is where Linux systems typically store timezone data.

> **_NOTE_**:
> 
> Everything is done in the **default** namespace.

### Create Pod:
- Using the below command create a pod:
```bash
kubectl apply -f basic-example.yaml
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/pods/timezone/images/timezone-pod-create.png)

### Check Pod Status:
- Check the status of the pod using the below command:
```bash
kubectl get pods
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/pods/timezone/images/timezone-pod-get-pods.png)

### Verify Timezone:
- Command to check the timezone of the pod:
```bash
kubectl exec timezone-pod -- date

# General Command:
kubectl exec <pod-name> -- date
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/pods/timezone/images/timezone-pod-verify.png)