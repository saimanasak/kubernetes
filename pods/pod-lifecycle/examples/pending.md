## PENDING PHASE

- The Pending phase in Kubernetes is the initial phase of a pod's lifecycle. 
- This phase occurs after a pod is created but before it has started running. 
- A pod enters the Pending state when it cannot be immediately scheduled onto a node, or when it is waiting for some resources to become available. 
- In this phase, Kubernetes is attempting to assign the pod to an appropriate node, but it may face certain constraints or requirements that prevent immediate scheduling.

### Example:
```yaml
# pod-pending.yaml

apiVersion: v1
kind: Pod
metadata:
  name: pending-pod
spec:
  containers:
    - name: busybox
      image: busybox
      command: ["sleep", "30"]
      resources:
        requests:
          memory: "10Gi"
          cpu: "13000m"
```

### Create Pod:
- Command to create the pod using the above manifest:
```bash
kubectl create -f pod-pending.yaml
# or
kubectl apply -f pod-pending.yaml
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/pods/pod-lifecycle/images/pending-create.png)

### Check Pod Status:
- Command to check pod status:
```bash
kubectl get pods
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/pods/pod-lifecycle/images/pending-get-pods.png)

### Pod Details:
- Command to check the pod details:
```bash
kubectl describe pod pod-pending.yaml
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/pods/pod-lifecycle/images/pending-describe.png)

### Check Events:
- You can find the events of the pod at the end of the pod description.

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/pods/pod-lifecycle/images/pending-event.png)

- In this case, the K8s scheduler is unable to find a node with enough resources (CPU and Memory) to satify the request.
- So, the pod remains in the pending state until it finds a node.