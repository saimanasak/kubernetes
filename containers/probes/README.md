## PROBE

- In general, a probe is a tool or mechanism used to inspect, monitor, or measure the status or condition of something. 
- It is typically used to gather information without making changes to the subject being examined.
- In Kubernetes, a probe is a diagnostic mechanism that checks the health and status of a container within a pod. 
- Probes are performed periodically by the kubelet to determine the current state of a container. 
- Based on the result of the probe, Kubernetes can decide whether to restart a container, keep it running, or route traffic to it.
- They are of three types:
    1. Liveness Probe
    2. Readiness Probe
    3. Startup Probe