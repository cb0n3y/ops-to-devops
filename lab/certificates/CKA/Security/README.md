# Security


Exercise 1: Image Security

    Deploy an application using a nginx image pulled from a public registry.
    Restrict the deployment to only allow images from a specific trusted registry (e.g., nginx.com).
    Verify that the image is pulled from the trusted registry.

Exercise 2: Image Vulnerability Scanning

    Set up a Kubernetes cluster with an image vulnerability scanning tool (e.g., Trivy or Clair).
    Scan a public Docker image for vulnerabilities and review the findings.

Exercise 3: Use ImagePullPolicy

    Create a deployment with the nginx image and set the imagePullPolicy to Always.
    Update the deployment with a new version of the image.
    Verify that the image is pulled again when the pod is restarted.

Exercise 4: Run Containers as Non-Root

    Deploy an application using a Docker image (nginx or custom).
    Configure the security context for the container to run as a non-root user.
    Ensure the pod is running with the correct user by inspecting the pod's security context.

Exercise 5: Set Up Container User and Group

    Create a deployment for a web application.
    Define a securityContext in the pod spec that ensures the container runs as a user and group ID other than root.
    Verify that the user is not root in the pod by running a simple id command inside the container.

Exercise 6: Use Seccomp Profiles

    Create a deployment that uses nginx as the container image.
    Configure the deployment to use a default Seccomp profile (runtime/default).
    Verify that the security context is properly set by inspecting the container's security settings.

Exercise 7: Use PodSecurityPolicy (PSP)

    Create a PodSecurityPolicy that restricts the usage of privileged containers.
    Deploy a pod that attempts to run as privileged and ensure the pod fails with the correct error message.
    Apply the policy and validate its effect.

Exercise 8: Use Host Network and Port Binding

    Create a deployment that runs an application with the hostNetwork set to true.
    Verify that the application is able to bind to host ports (e.g., 80 or 443) by checking the pod's networking configuration.

Exercise 9: Use Read-Only File System

    Create a pod that runs a container with the filesystem mounted as readOnly.
    Verify that the container cannot write to the filesystem by attempting to create a file inside the container.

Exercise 10: Security Context for Pod

    Create a pod spec that runs a container with the securityContext configured to prevent privilege escalation.
    Verify the pod does not allow privilege escalation by attempting to run a command that would elevate privileges.

Exercise 11: Apply Network Policies

    Create a NetworkPolicy to block all ingress and egress traffic to a specific pod.
    Create a second NetworkPolicy that allows ingress traffic only from a specific pod or service.
    Test connectivity between pods to verify the policies work as intended.

Exercise 12: Network Policy to Allow Traffic from a Namespace

    Create a NetworkPolicy that allows traffic from pods only in the dev namespace.
    Deploy a pod in the dev namespace and verify it can communicate with the target pod.
    Ensure that pods in other namespaces are blocked from accessing the target pod.

Exercise 13: Limit Egress Traffic

    Define a NetworkPolicy that restricts egress traffic from a pod to specific external services (e.g., blocking external HTTP access).
    Test the egress restrictions by attempting to reach a blocked external service.

Exercise 14: Network Policies with IP Block

    Create a NetworkPolicy that allows communication from a specific IP block (e.g., 192.168.0.0/24) while denying all other IP ranges.
    Test by deploying a pod with an external IP outside the allowed range and ensuring it cannot communicate with the target pod.

Exercise 15: Using ImagePullSecrets

    Create a deployment that pulls an image from a private registry.
    Use an ImagePullSecret to authenticate against the registry.
    Verify that the application pod pulls the image successfully using the provided secret.

Exercise 16: Control Access to Sensitive Files

    Create a deployment that mounts a secret as a volume in the pod.
    Use securityContext to control the access permissions (e.g., set readOnly access for the secret).
    Verify that the secret is correctly mounted and protected as specified.

Exercise 17: Container Resource Constraints

    Create a deployment and set resource limits (cpu and memory) for the container.
    Ensure that the pod is killed and restarted if it exceeds its resource limits.
    Use kubectl describe pod to check the resource usage and status.

Exercise 18: Use PodSecurityAdmission (PSA)

    Enable PodSecurityAdmission in the cluster to enforce security standards such as "restricted", "baseline", or "privileged".
    Create a pod that violates the "restricted" policy (e.g., running as root).
    Ensure the pod is blocked and review the security error message.

Exercise 19: Configure AppArmor

    Create a deployment that runs a container with an AppArmor profile.
    Configure the container to use a custom AppArmor profile for additional security restrictions.
    Verify the AppArmor profile is applied by checking the container's logs for violations.

Exercise 20: Network Policies with Namespaced Rules

    Create a NetworkPolicy that allows traffic from pods within the same namespace.
    Deploy two pods in the same namespace and verify they can communicate with each other.
    Deploy a pod in a different namespace and ensure it cannot communicate with the pods in the original namespace.

