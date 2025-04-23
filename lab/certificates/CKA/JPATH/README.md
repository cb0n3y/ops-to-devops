# JSONPATH

## Exercises

### Exercise 1
List the names of all Pods in the `default` namespace using JSONPath.

```bash

k get pod -n default -o=jsonpath='{range .items[*]}{.metadata.name}{"\n"}{end}'

```

### Exercise 2
From the list of all Pods in `kube-system`, extract all container images used.

```bash

k get pod -n kube-system kube-apiserver-dev-k8s-master kube-controller-manager-dev-k8s-master kube-proxy-drsjk kube-proxy-jxkrq kube-proxy-r5nmr kube-proxy-zxb7x kube-scheduler-dev-k8s-master -o=jsonpath='{range .items[*]}{.spec.containers[*].image}{"\n"}{end}'

```

### Exercise 3
List the names of all PersistentVolumeClaims (PVCs) bound to PersistentVolumes.

```bash

k get pvc -A -o=jsonpath='{range .items[?(@.status.phase=="Bound")]}{.metadata.name}{"\n"}{end}'

```

### Exercise 4
From all Pods, print the names of only those that are in `Running` phase.

```bash

k get pod -A -o=jsonpath='{range .items[?(@.status.phase=="Running")]}{.metadata.name}{"\n"}{end}'

```

### Exercise 5
From all Pods in `kube-system`, extract the container names **only if** their `resources.limits.cpu` is set.

```bash

k get pod -n kube-system -o=jsonpath='{range .items[*].spec.containers[*]}{.name}{"\t"}{.resources.limits.cpu}{"\n"}{end}'

```

### Exercise 6
From the list of Deployments, show names of those **with replicas > 1**

```bash

k get deployments.apps -A -o=jsonpath='{range .items[?(@.spec.replicas>1)]}{.metadata.name}{"\n"}{end}'
# or
k get deployments.apps -A -o=jsonpath='{range .items[?(@.spec.replicas>1)]}{.metadata.name}{"\t"}{.spec.replicas}{"\n"}{end}' 

```

### Exercise 7

