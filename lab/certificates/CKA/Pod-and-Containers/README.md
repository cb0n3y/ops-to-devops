# Pods and Containers

Here are 20 exercises based on the "Configure Pods and Containers" section of the Kubernetes documentation:

### Exercise 1: Configure a simple pod
- Create a pod named `nginx-pod` with an NGINX container.
  
### Exercise 2: Set resource requests and limits
- Create a pod that requests 500m CPU and 256Mi memory for an NGINX container and sets a limit of 1 CPU and 512Mi memory.

### Exercise 3: Configure environment variables
- Create a pod that runs a container with the environment variable `APP_NAME` set to "MyApp".

### Exercise 4: Set a command and args
- Create a pod running the `sleep` command with an argument to sleep for 3600 seconds.

### Exercise 5: Use a ConfigMap in a pod
- Create a ConfigMap with a key-value pair (`APP_MODE=production`), then reference it in a pod as an environment variable.

### Exercise 6: Use a Secret in a pod
- Create a Secret with a username and password, then mount it as an environment variable in a pod.

### Exercise 7: Set up volume mounting
- Create a pod that uses an emptyDir volume and mounts it at `/data` in the container.

### Exercise 8: Use an existing PVC (Persistent Volume Claim)
- Create a pod that mounts a pre-existing Persistent Volume Claim at `/mnt/data`.

### Exercise 9: Enable multi-container pods
- Create a pod with two containers: one running NGINX and the other running Redis.

### Exercise 10: Define liveness and readiness probes
- Create a pod with a container that has both liveness and readiness probes to check the health of the container.

### Exercise 11: Use init containers
- Create a pod with one init container that runs a script before the main container starts.

### Exercise 12: Configure resource limits in a Deployment
- Create a Deployment that uses a pod template with CPU and memory limits for its container.

### Exercise 13: Set an image pull policy
- Create a pod that uses a `Always` image pull policy to pull the image every time the pod starts.

### Exercise 14: Use a sidecar container
- Create a pod with a sidecar container that logs data from the main container.

### Exercise 15: Configure a pod with a service account
- Create a pod that uses a service account named `pod-service-account`.

### Exercise 16: Configure a pod with affinity rules
- Create a pod with node affinity rules to schedule it on nodes with `zone=us-west`.

### Exercise 17: Configure pod tolerations
- Create a pod with a toleration for a taint with key `app` and value `critical`.

### Exercise 18: Use resource quotas with pods
- Create a namespace with a resource quota that limits the number of CPU cores, memory, and pods.

### Exercise 19: Set pod priority
- Create a pod with a priority class of `high-priority` to ensure it is scheduled before other pods.

### Exercise 20: Configure a pod to use a hostNetwork
- Create a pod with the `hostNetwork` set to true, allowing it to use the node's network stack.