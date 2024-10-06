## CLUSTER IP

- The ClusterIP service type is the default and most basic service type in Kubernetes, designed for internal communication within the cluster. 
- It creates a virtual IP address that routes traffic to the associated pods, allowing them to communicate with one another using this internal address. 
- ClusterIP services are not accessible from outside the cluster, making them suitable for microservices architectures where components need to interact securely and privately.
- This service type is particularly useful for applications that do not require external access but still need to interact with other services within the cluster. 
- It simplifies network management by providing a stable endpoint for pods that may be frequently created and destroyed. 
- ClusterIP services are often used in combination with other service types, such as NodePort or LoadBalancer, to facilitate both internal and external communications as part of a broader application architecture.