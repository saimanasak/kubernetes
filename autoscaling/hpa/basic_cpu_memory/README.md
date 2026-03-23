## 4 – Horizontal Pod Autoscaler (HPA) using CPU and Memory

### Project Overview

This project demonstrates how to implement **automatic scaling in Kubernetes** using the **Horizontal Pod Autoscaler (HPA)** based on **CPU and memory utilization**.

In real-world applications, traffic is unpredictable — it can increase during peak usage and decrease during off-peak times. Manually scaling applications is inefficient and error-prone. Kubernetes solves this problem using HPA, which automatically adjusts the number of running pods based on resource usage.

In this project, we deploy a simple **Nginx application** using a **Deployment**, expose it internally using a **ClusterIP Service**, and configure an **HPA** to dynamically scale pods based on CPU and memory thresholds. We also use a **load generator pod** to simulate traffic and observe how Kubernetes scales the application in real time.

The goal is to understand how Kubernetes enables **automatic, dynamic scaling** and ensures better performance and resource efficiency.

---

### Concepts Covered

#### 1. Horizontal Pod Autoscaler (HPA)

The **Horizontal Pod Autoscaler (HPA)** automatically scales the number of pod replicas based on observed metrics such as CPU and memory usage.

HPA helps:

- Automatically scale applications based on demand
- Improve application performance during high traffic
- Reduce resource usage during low traffic
- Maintain high availability without manual intervention

In this project, HPA is configured to scale based on:

- `CPU utilization (50%)`
- `Memory utilization (60%)`

---

#### 2. Resource Requests and Limits

For HPA to function correctly, containers must define **resource requests and limits**.

They help:

- Define minimum resources required by a container
- Enable Kubernetes to calculate utilization percentages
- Prevent resource overconsumption

In this project, each container defines:

- `CPU request: 100m`
- `Memory request: 128Mi`

---

#### 3. Deployments

A **Deployment** manages the lifecycle of Pods and ensures the desired number of replicas are running.

It provides:

- Automatic pod creation and management
- Self-healing capabilities
- Easy scaling of application replicas

In this project, the Deployment runs the **Nginx application pods**.

---

#### 4. Services (ClusterIP)

A **Service** provides a stable network endpoint to access Pods.

In this project we use:

**ClusterIP Service**

- Exposes the application **inside the Kubernetes cluster**
- Acts as an internal load balancer
- Distributes traffic across multiple pods
- Allows communication using service name: **http://my-hpa-service**

---

#### 5. Metrics Server

The **Metrics Server** collects resource usage data such as CPU and memory from running pods.

It helps:

- Provide metrics required by HPA
- Enable commands like `kubectl top`
- Allow Kubernetes to make scaling decisions

---

#### 6. Load Generator

A **load generator pod** is used to simulate real-world traffic.

It helps:

- Generate continuous requests to the application
- Increase CPU usage
- Trigger autoscaling

---

### Architecture

![Screenshot](architecture.png)

---

### Solution

- Blog: *Horizontal Pod Autoscaler (HPA) using CPU and Memory in Kubernetes*()
- Manifests: `autoscaling/hpa/`

---

### Expected Outcome

After completing this project:

- The Nginx application should be deployed using a **Kubernetes Deployment**
- Resource requests and limits should be defined for the containers
- The application should be exposed using a **ClusterIP Service**
- Metrics Server should be enabled and collecting resource usage data
- HPA should automatically scale pods based on CPU and memory usage
- Pods should scale up when load increases and scale down when load decreases
- The system should demonstrate **dynamic and automatic scaling in Kubernetes**