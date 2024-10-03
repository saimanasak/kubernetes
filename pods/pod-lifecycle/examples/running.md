## RUNNING PHASE

- The Running phase indicates that a pod has been successfully scheduled to a node and that at least one container within that pod is actively running. 
- This phase is a key part of the pod lifecycle, as it signifies that the application or service encapsulated within the pod is operational and able to respond to requests.

### Example:
```yaml
# pod-running.yaml

apiVersion: v1
kind: Pod
metadata:
  name: running-pod
spec:
  containers:
  - name: nginx-container
    image: nginx
```

### Create Pod:
- Command to create a pod using the above manifest file:
```bash
kubectl create -f pod-running.yaml

kubectl apply -f pod-running.yaml
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/pods/pod-lifecycle/images/running-create.png)

### Check Pod Status:
- Command to get the status of the pods:
```bash
kubectl get pods
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/pods/pod-lifecycle/images/running-get-pods.png)

### Pod Details:
- Command to check the details of the above pod:
```bash
kubectl describe pod running-pod
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/pods/pod-lifecycle/images/running-describe.png)

- The Running phase is a critical part of the pod lifecycle in Kubernetes, indicating that your application is live and capable of serving requests. 
- Monitoring and managing pods in this state is essential for maintaining the health and availability of applications running in a Kubernetes cluster.