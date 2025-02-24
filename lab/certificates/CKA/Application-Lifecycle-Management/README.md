# Application Lifecycle Management

Here are 20 exercises related to Application Lifecycle Management (ALM) in Kubernetes:

---

### Exercise 1: **Create a Kubernetes Application**
1. Deploy a simple application using the `nginx` container image.
2. Expose the application with a service of type `ClusterIP`.
3. Verify the application is running using `kubectl get pods` and `kubectl get services`.

### Exercise 2: **Manage Deployments**
1. Create a deployment for a web application (e.g., `nginx`).
2. Scale the deployment to 4 replicas.
3. Use `kubectl get deployments` to verify that the deployment is running the correct number of replicas.

### Exercise 3: **Rolling Updates**
1. Create a deployment using the `nginx:1.17` image.
2. Update the deployment to use the `nginx:1.18` image.
3. Check the status of the rolling update using `kubectl rollout status`.

### Exercise 4: **Rollback Deployment**
1. Perform a rollback to a previous version of a deployment.
2. Use `kubectl rollout history` to list the previous revisions of the deployment.
3. Rollback the deployment to an earlier version.

### Exercise 5: **Blue-Green Deployment**
1. Create two separate deployments (blue and green) using different versions of an application.
2. Set up a `Service` that routes traffic to the active deployment (e.g., blue).
3. Swap the active deployment by updating the service.

### Exercise 6: **Canary Releases**
1. Create a canary release strategy by creating a deployment with two versions of the application (e.g., 90% to old version, 10% to new version).
2. Use `kubectl rollout status` to monitor the release progress.

### Exercise 7: **Continuous Integration/Continuous Deployment (CI/CD)**
1. Configure a Kubernetes deployment pipeline using GitLab CI or Jenkins.
2. Set up a pipeline that automatically deploys an application when new code is pushed to the repository.

### Exercise 8: **Define Health Checks**
1. Create a deployment for an application with a `livenessProbe` and `readinessProbe` configured.
2. Simulate a failure of the container and verify that Kubernetes restarts the pod based on the liveness probe.

### Exercise 9: **Use Helm for Deployment**
1. Install Helm on your cluster.
2. Deploy an application using a Helm chart (e.g., `nginx` chart).
3. Use `helm list` to verify the release.

### Exercise 10: **Update a Helm Release**
1. Update the deployed application using Helm to a new version.
2. Rollback the update using `helm rollback`.

### Exercise 11: **Application Configuration Management**
1. Use ConfigMaps to store application configuration values.
2. Update the ConfigMap and apply it to a running deployment.
3. Verify that the changes are applied by checking the application logs.

### Exercise 12: **Secret Management**
1. Create a Kubernetes Secret to store sensitive application credentials (e.g., database passwords).
2. Mount the secret as an environment variable in a container.

### Exercise 13: **Application Scaling**
1. Scale a deployment horizontally by increasing the number of replicas to 10.
2. Verify the scaling by using `kubectl get pods` and check the pods' status.

### Exercise 14: **Pod Disruption Budgets**
1. Create a Pod Disruption Budget (PDB) for a deployment to ensure a minimum number of pods are available during voluntary disruptions.
2. Perform a rolling update and check the PDB status.

### Exercise 15: **Pod Affinity and Anti-Affinity**
1. Create a deployment that uses node affinity to ensure it is scheduled on nodes with a specific label.
2. Create another deployment that uses anti-affinity to avoid being scheduled on the same node as the first deployment.

### Exercise 16: **Resource Requests and Limits**
1. Set CPU and memory resource requests and limits for the containers in a deployment.
2. Verify that the containers are constrained by the limits you set using `kubectl describe pod`.

### Exercise 17: **Multi-Container Pods**
1. Create a pod with two containers: one running `nginx` and another running a sidecar container (e.g., a log collector).
2. Verify both containers are running within the same pod and share a volume.

### Exercise 18: **Manage Application Configurations via Environment Variables**
1. Create a deployment with environment variables to store database credentials.
2. Update the deployment to change the environment variable and ensure the container picks up the change.

### Exercise 19: **Custom Resource Definitions (CRDs)**
1. Create a custom resource definition (CRD) to define a custom application resource.
2. Create instances of the custom resource and manage them using Kubernetes resources.

### Exercise 20: **Monitor Application Health**
1. Set up a monitoring solution (e.g., Prometheus, Grafana) to monitor the health of your deployed applications.
2. Create alerts to notify you when a deployment fails or when a resource exceeds its limits.

---

These exercises cover a broad range of topics within the Application Lifecycle Management (ALM) space, progressively increasing in difficulty.