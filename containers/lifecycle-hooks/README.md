## CONTAINER LIFECYCLE HOOKS

- Container Lifecycle Hooks in Kubernetes allow us to trigger custom actions when certain lifecycle events occur in a container. 
- These hooks are used to control the behavior of your container during specific phases of its lifecycle, such as when it starts or when it is about to stop.

### Why???

- In a distributed system like Kubernetes, applications are dynamically started, scaled, and stopped based on demand. Hooks provide a way to:
    - Run initialization tasks after the container starts.
    - Gracefully handle shutdown processes, such as closing connections or saving application state.
    - Ensure that resources are properly managed, even during unexpected shutdowns.
    
### Types of Hooks:
- There are two primary types of lifecycle hooks:
    1. PostStart Hook
    2. PreStop Hook
    
### Hook Handlers:
- There are three types of handlers:
    1. exec
    2. HTTP
    3. sleep