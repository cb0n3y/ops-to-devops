# Multi

Here are **30 exercises** designed to simulate tasks you might encounter in the **CKA (Certified Kubernetes Administrator)** exam. These exercises combine tasks like creating pods, configuring security, setting resource limits, managing network policies, creating roles and bindings, and more. The goal is to practice multiple related tasks in a single exercise to deepen your understanding of Kubernetes concepts.

---

### Exercise 1: **Basic Pod Creation and Resource Limits**
1. Create a pod using the `nginx` image.
2. Set resource limits (`cpu` and `memory`) for the container in the pod.
3. Verify that the resource limits are applied correctly by describing the pod.

### Exercise 2: **Pod with Mount and Persistent Volume**
1. Create a persistent volume (PV) and persistent volume claim (PVC).
2. Create a pod that mounts the PVC to a directory inside the container.
3. Verify that the pod can access the mounted volume.

### Exercise 3: **Pod with Read-Only Filesystem**
1. Create a pod that runs a container with a read-only filesystem.
2. Verify that the container cannot write to the filesystem by attempting to create a file inside the container.

### Exercise 4: **Pod with Security Context (Non-root User)**
1. Create a pod with a container running as a non-root user.
2. Verify that the container runs with the specified user and group by checking the container's UID and GID.

### Exercise 5: **Pod with Seccomp Profile**
1. Create a pod using the `nginx` image.
2. Apply a custom Seccomp profile to the container.
3. Verify that the Seccomp profile is applied by inspecting the container's security context.

### Exercise 6: **Creating and Using Role and RoleBinding**
1. Create a `Role` that allows `get`, `list`, and `create` actions on `pods` in a specific namespace.
2. Create a `RoleBinding` that binds the `Role` to a specific service account.
3. Verify that the service account has the correct permissions by using `kubectl auth can-i`.

### Exercise 7: **Pod with Network Policy**
1. Create a pod that communicates with a second pod in the same namespace.
2. Create a `NetworkPolicy` that restricts ingress and egress traffic to only allow communication between the two pods.
3. Verify that the pods can communicate when allowed, and cannot communicate when restricted.

### Exercise 8: **Pod with AppArmor Profile**
1. Create a pod with a container using an AppArmor profile.
2. Ensure the pod adheres to the security profile by reviewing the pod logs for any violations.

### Exercise 9: **Configuring Image Pull Policy**
1. Create a deployment using the `nginx` image.
2. Set the `imagePullPolicy` to `Always`.
3. Verify that the image is pulled on each pod restart.

### Exercise 10: **Pod with Resource Requests and Limits**
1. Create a pod that runs a container with specified resource requests (`cpu` and `memory`) and limits.
2. Verify that the requests and limits are applied correctly by describing the pod.

### Exercise 11: **Create and Bind ClusterRole**
1. Create a `ClusterRole` that grants `get`, `list`, and `create` permissions on `pods` across the entire cluster.
2. Create a `ClusterRoleBinding` to bind this role to a service account.
3. Verify that the service account has access to perform the specified actions on `pods` in the cluster.

### Exercise 12: **Configure Pod Affinity and Anti-Affinity**
1. Create two pods with labels.
2. Set up pod affinity so that one pod is scheduled on the same node as another pod.
3. Set up pod anti-affinity to ensure that two specific pods are not scheduled on the same node.

### Exercise 13: **Pod with HostNetwork**
1. Create a pod with the `hostNetwork` set to `true`.
2. Ensure that the pod can bind to host ports.
3. Verify that the pod is using the host network by checking the pod's network configuration.

### Exercise 14: **Create and Use ClusterRole for Pod Management**
1. Create a `ClusterRole` that allows management of `pods` across the entire cluster.
2. Create a `ClusterRoleBinding` that binds this role to a service account.
3. Verify that the service account can create and manage pods in any namespace.

### Exercise 15: **Pod with HostPath Volume**
1. Create a pod that uses a `hostPath` volume.
2. Mount the `hostPath` volume to a directory inside the container.
3. Verify that the container can access the files in the `hostPath` volume.

### Exercise 16: **Pod with Multi-Container Setup**
1. Create a pod that runs two containers (`nginx` and `busybox`).
2. Set a shared volume between the two containers.
3. Verify that the containers can communicate and share data via the volume.

### Exercise 17: **Pod Security Policy (PSP)**
1. Create a `PodSecurityPolicy` that restricts the usage of privileged containers.
2. Create a pod that tries to run with privileged mode enabled and verify that it is denied.
3. Ensure that the policy is applied correctly.

### Exercise 18: **Pod with Init Containers**
1. Create a pod that runs an init container before starting the main application container.
2. Ensure that the init container performs a setup task (e.g., creates a file) before the main container starts.
3. Verify that the init container completes successfully before the main container runs.

### Exercise 19: **Pod with Custom SecurityContext for Containers**
1. Create a pod with two containers, where one runs as a non-root user and the other runs with a specific `capabilities` setting (e.g., adding the `NET_ADMIN` capability).
2. Verify the settings by inspecting the containers' security contexts.

### Exercise 20: **Create and Bind ClusterRole with Network Policies**
1. Create a `ClusterRole` that allows managing `NetworkPolicy` resources across the cluster.
2. Create a `ClusterRoleBinding` to bind this role to a service account.
3. Verify that the service account can create and manage network policies cluster-wide.

### Exercise 21: **Creating and Using Network Policies with Egress and Ingress Rules**
1. Create a pod with no network policies.
2. Create a `NetworkPolicy` that allows ingress traffic from a specific pod but blocks all egress traffic.
3. Verify the restrictions by testing connectivity.

### Exercise 22: **Pod with Memory and CPU Requests/Limit Based on Load**
1. Create a pod that runs an application and set CPU and memory requests and limits.
2. Test the pod with a heavy load and ensure it gets throttled when exceeding the limits.
3. Check the resource usage to verify that the limits are enforced.

### Exercise 23: **Use NetworkPolicy to Allow Only Specific Pods to Communicate**
1. Create two pods in separate namespaces.
2. Create a `NetworkPolicy` in one namespace to allow only one pod to communicate with the other pod.
3. Verify that the pods can communicate as intended.

### Exercise 24: **Pod with CPU and Memory Limits and Multiple Containers**
1. Create a pod with multiple containers, each having its own resource requests and limits.
2. Set a limit for the total pod resources.
3. Verify the resource limits are correctly enforced for each container and the pod.

### Exercise 25: **Create RoleBinding for Pod Creation Permissions**
1. Create a `Role` that allows `create` and `get` actions on `pods` in a namespace.
2. Create a `RoleBinding` that binds this role to a specific service account.
3. Verify the service account can create pods in the specified namespace.

### Exercise 26: **SecurityContext for Pods with Privilege Escalation Disabled**
1. Create a pod that runs a container with privilege escalation disabled.
2. Attempt to run a command that requires privilege escalation and verify that it fails.
3. Ensure that the security context is applied correctly.

### Exercise 27: **Create ClusterRole and ClusterRoleBinding for Managing ConfigMaps**
1. Create a `ClusterRole` that allows managing `ConfigMap` resources across the entire cluster.
2. Create a `ClusterRoleBinding` to bind this role to a service account.
3. Verify that the service account can create and manage `ConfigMaps` across all namespaces.

### Exercise 28: **Pod with Volume Mount and Init Container**
1. Create a pod with an init container that prepares a configuration file.
2. Mount the volume with the configuration file into the main container.
3. Verify that the main container has access to the configuration file.

### Exercise 29: **Create Role and RoleBinding for Managing Secrets**
1. Create a `Role` that grants `get` and `list` permissions on `Secrets` in a specific namespace.
2. Create a `RoleBinding` to bind the `Role` to a service account.
3. Verify that the service account can list and get secrets in that namespace.

### Exercise 30: **Pod with Custom NetworkPolicy and Resource Limits**
1. Create a pod with resource limits (`cpu` and `memory`) set to reasonable values.
2. Set up a `NetworkPolicy` that blocks all ingress traffic except from a specific service.
3. Verify that the pod can receive traffic only from the allowed service.

---

These exercises cover a wide range of topics from pod creation, configuration, and resource management to role and binding creation, as well as security features like network policies and security contexts. Practicing these tasks will help you prepare for both the **CKA** exam and real-world Kubernetes cluster management.