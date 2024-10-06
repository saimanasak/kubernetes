## NODE PORT

- The NodePort service type in Kubernetes allows users to expose a specific port on each node in the cluster, making it accessible externally. 
- This service type automatically allocates a port from a predefined range (default is 30000-32767) and maps it to the specified port on the pod. 
- This means that users can access the application running in the pod by hitting any node's IP address along with the allocated NodePort. 
- This setup is particularly useful for development and testing environments, as it provides a straightforward way to expose applications without the need for a cloud provider's load balancer.
- NodePort services also facilitate basic load balancing by routing traffic to the pods across all nodes in the cluster. 
- While easy to set up and useful for small-scale applications, NodePort services may not be suitable for production-level deployments, as they expose application ports on all nodes, potentially leading to security concerns. 