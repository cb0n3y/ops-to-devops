# Run Applications

Here are 20 exercises related to running applications in Kubernetes, based on the official documentation:

---

### Exercise 1: 
1. Create a deployment called `nginx-deployment` with 3 replicas of the Nginx container.
2. Expose the deployment with a service of type `ClusterIP`.
3. Verify the deployment and service are running.

### Exercise 2: 
1. Create a deployment named `mysql-deployment` using the MySQL 5.7 image.
2. Set environment variables `MYSQL_ROOT_PASSWORD=rootpassword`.
3. Expose the deployment with a `ClusterIP` service.

### Exercise 3:
1. Scale the `nginx-deployment` to 5 replicas.
2. Check the status of the pods and ensure 5 pods are running.

### Exercise 4:
1. Create a `nginx-deployment` with a rolling update strategy.
2. Update the deployment to use a new Nginx image (`nginx:1.18`).

### Exercise 5:
1. Create a CronJob to run a `nginx` container every 5 minutes.
2. Check if the CronJob runs as expected.

### Exercise 6:
1. Create a DaemonSet that runs `nginx` on every node.
2. Verify the pods are running on all nodes.

### Exercise 7:
1. Deploy a StatefulSet using `mysql` and persistent storage.
2. Verify the StatefulSet pods have persistent storage attached.

### Exercise 8:
1. Create a ReplicaSet with 3 replicas for the `nginx` container.
2. Scale the ReplicaSet to 4 replicas.

### Exercise 9:
1. Create a deployment with 2 containers: a sidecar and a main app.
2. Verify both containers are running in the same pod.

### Exercise 10:
1. Create a deployment that uses `nginx` as the container image.
2. Apply resource limits and requests for CPU and memory to the deployment.

### Exercise 11:
1. Create a Kubernetes Deployment and expose it using a `LoadBalancer`.
2. Verify you can access the deployment using an external IP.

### Exercise 12:
1. Create a deployment with a `livenessProbe` that checks the health of the container.
2. Ensure that the container is restarted if the probe fails.

### Exercise 13:
1. Update a deployment with an environment variable and verify the pod is restarted.
2. Use the `kubectl rollout status` command to check the status.

### Exercise 14:
1. Create a deployment with a container running the `redis` image.
2. Expose the Redis service as a `ClusterIP`.

### Exercise 15:
1. Create a deployment using a custom container image.
2. Set up a resource request and limit for the deployment.

### Exercise 16:
1. Use the `kubectl apply` command to update the deployment and change the container's image version.
2. Use `kubectl rollout undo` to revert the changes.

### Exercise 17:
1. Create a Pod that runs an Nginx container.
2. Verify the pod is running and accessible on the cluster.

### Exercise 18:
1. Create a deployment with a `readinessProbe`.
2. Simulate failure and ensure the pod is not available to the service until healthy.

### Exercise 19:
1. Create a deployment using `nginx` and set a custom label for the pods.
2. Use `kubectl get pods -l <label>` to list pods with that label.

### Exercise 20:
1. Create a deployment with a `replicaset` and then scale down the replicas to 0.
2. Ensure no pods are running when the ReplicaSet is scaled down to 0.