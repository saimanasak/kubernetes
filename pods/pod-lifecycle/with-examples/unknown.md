## UNKNOWN PHASE

- The Unknown phase in Kubernetes occurs when the control plane (the Kubernetes master node) is unable to determine the state of a pod because of a communication issue with the node where the pod is running. 
- This could be due to network issues, node crashes, or problems with the kubelet (the node agent that communicates with the control plane). 
- This phase typically arises in scenarios where there is a failure in communication between the Kubernetes control plane and the node hosting the pod.
- If a node becomes unreachable due to network partitioning, crashes, or other infrastructure problems, Kubernetes may not be able to determine the current state of any pods scheduled on that node.
- The kubelet is responsible for monitoring pods on a node and reporting their status back to the control plane. If the kubelet on the node stops running (e.g., due to a service failure or it being manually stopped), the node cannot send status updates to the Kubernetes API server. As a result, the state of the pods on that node will be marked as Unknown.
- In some cases, even if the node and kubelet are healthy, a temporary network outage or heavy network latency between the control plane and the node can cause the node to be unreachable for status reporting, resulting in the Unknown phase.
- If the node is under extreme resource pressure (e.g., running out of memory or CPU), it may stop responding to the control plane, which can also cause pods to move into the Unknown state.