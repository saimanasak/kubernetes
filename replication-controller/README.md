## REPLICATION CONTROLLER

- It is a component that ensures a specified number of identical pod replicas are running at all times. 
- It continuously monitors the state of the cluster and takes action to either start or stop pods to match the desired number, providing fault tolerance and ensuring that application workloads remain available even in the face of individual pod failures or crashes.
- If a pod dies, the ReplicationController will create a new one to replace it. 
- While ReplicationController is used less nowadays (favoring ReplicaSets and Deployments), it still works for simple scenarios.