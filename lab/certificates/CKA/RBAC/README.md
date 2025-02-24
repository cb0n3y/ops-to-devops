# RBAC

Here we just have some exercises related to RBAC

## Exercise 1: Basic RBAC Setup

- Create a namespace called project-x.
- Create a service account called data-viewer in the project-x namespace.
- Create a role called pod-reader that grants permissions to get and list pods in the project-x namespace.
- Create a rolebinding named bind-pod-reader that binds the pod-reader role to the data-viewer service account in the project-x namespace.
- Prove that the data-viewer service account can get and list pods in the project-x namespace but cannot perform these actions on deployments.

### CLI Commands

``` bash

cb0n3y@cka-k8s-master:~/cka_exam_preparation/RBAC$  kubectl create ns project-x -o yaml --dry-run=client [> project-x.yaml] # use only the last part of the command, if you want to save it in a yaml file
cb0n3y@cka-k8s-master:~/cka_exam_preparation/RBAC$ echo "---" >> project-x.yam # optional if you want to put everything in a single file
cb0n3y@cka-k8s-master:~/cka_exam_preparation/RBAC$ kubectl create sa data-viewer -n project-x -o yaml --dry-run=client >> project-x.yaml
cb0n3y@cka-k8s-master:~/cka_exam_preparation/RBAC$ echo "---" >> project-x.yaml
cb0n3y@cka-k8s-master:~/cka_exam_preparation/RBAC$ kubectl kubectl create role pod-reader --resource=pods --verb=get,list -n project-x -oyaml --dry-run=client >> project-x.yaml
cb0n3y@cka-k8s-master:~/cka_exam_preparation/RBAC$ echo "---" >> project-x.yaml
cb0n3y@cka-k8s-master:~/cka_exam_preparation/RBAC$ kubectl create rolebinding bind-pod-reader --role=pod-reader --serviceaccount=project-x:data-viewer --dry-run=client -o yaml >> project-x.yaml

cb0n3y@cka-k8s-master:~/cka_exam_preparation/RBAC$ kubectl --as=system:serviceaccount:project-x:data-viewer auth can-i get pods -n project-x
yes

```

### YAML File

<details>
<summary>Click to view YAML file</summary>

``` yaml

apiVersion: v1
kind: Namespace
metadata:
  creationTimestamp: null
  name: project-x
spec: {}
status: {}
---
apiVersion: v1
kind: ServiceAccount
metadata:
  creationTimestamp: null
  name: data-viewer
  namespace: project-x
---
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  creationTimestamp: null
  name: pod-reader
  namespace: project-x
rules:
- apiGroups:
  - ""
  resources:
  - pods
  verbs:
  - list
  - get
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  creationTimestamp: null
  name: bind-pod-reader
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: Role
  name: pod-reader
subjects:
- kind: ServiceAccount
  name: data-viewer
  namespace: project-x

```

</details>


## Exercise 2: Expanding Permissions

- Create a namespace called dev-environment.
- Create a service account called app-deployer in the dev-environment namespace.
- Create a role called pod-manager with permissions to create, get, list, and delete pods in the dev-environment namespace.
- Create a rolebinding named bind-pod-manager that binds the pod-manager role to the app-deployer service account in the dev-environment namespace.
Prove that the app-deployer service account can delete pods but cannot delete deployments in the dev-environment namespace.


### CLI Commands


``` bash

echo "test"

```

### YAML File

<details>
<sumary>Click to view theYAML file.</sumary>


``` yaml

apiVersion: v1
kind: Namespace
metadata:
  creationTimestamp: null
  name: dev-environment
spec: {}
status: {}
---
apiVersion: v1
kind: ServiceAccount
metadata:
  creationTimestamp: null
  name: app-deployer
  namespace: dev-environment
---
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  creationTimestamp: null
  name: pod-manager
  namespace: dev-environment
rules:
- apiGroups:
  - ""
  resources:
  - pods
  verbs:
  - create
  - get
  - list
  - delete
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  creationTimestamp: null
  name: bind-pod-manager
  namespace: dev-environment
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: Role
  name: pod-manager
subjects:
- kind: ServiceAccount
  name: app-deployer
  namespace: dev-environment

```


</details>


## Exercise 3: Cluster-Wide Permissions

- Create a clusterrole called read-all-namespaces that grants get and list permissions to pods in all namespaces.
- Create a service account called cluster-reader.
- Create a clusterrolebinding named bind-read-all-namespaces that binds the read-all-namespaces ClusterRole to the cluster-reader service account.
- Prove that the cluster-reader service account can get and list pods in all namespaces but cannot perform any action on deployments.


### CLI Commands

``` bash

echo "test"

```


### YAML File

<details>
<sumary>Click to view the YAML file.</sumary>

``` yaml

apiVersion: v1
kind: ServiceAccount
metadata:
  creationTimestamp: null
  name: cluster-reader
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  creationTimestamp: null
  name: read-all-namespaces
rules:
- apiGroups:
  - ""
  resources:
  - namespaces
  verbs:
  - get
  - list
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  creationTimestamp: null
  name: bind-read-all-namespaces
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: read-all-namespaces
subjects:
- kind: ServiceAccount
  name: cluster-reader
  namespace: '*'

```
</details>


## Exercise 4: More Granular Permissions

- Create a namespace called analytics.
- Create a service account called report-generator in the analytics namespace.
- Create a role called report-viewer that grants get and list permissions on jobs and cronjobs in the analytics namespace.
- Create a rolebinding named bind-report-viewer that binds the report-viewer role to the report-generator service account in the analytics namespace.
- Prove that the report-generator service account can get and list jobs and cronjobs, but cannot interact with pods in the analytics namespace.
^
### CLI Commands

``` bash

echo "test"

```


### YAML File

<details>
<sumary>Click to view the YAML file.</sumary>

``` yaml

apiVersion: v1
kind: Namespace
metadata:
  creationTimestamp: null
  name: analytics
spec: {}
status: {}
---
apiVersion: v1
kind: ServiceAccount
metadata:
  creationTimestamp: null
  name: report-generator
  namespace: analytics
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  creationTimestamp: null
  name: report-viewer
  namespace: analytics
rules:
- apiGroups:
  - batch
  resources:
  - jobs
  - cronjobs
  verbs:
  - get
  - list
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  creationTimestamp: null
  name: bind-reporter-viewer
  namespace: analytics
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: Role
  name: report-viewer
subjects:
- kind: ServiceAccount
  name: report-generator
  namespace: analytics

```

</details>


## Exercise 5: ClusterRole with Elevated Permissions

- Create a clusterrole named cluster-admin-pods that grants create, get, list, delete, and update permissions to pods in all namespaces.
- Create a service account called full-access-admin.
- Bind the cluster-admin-pods ClusterRole to the full-access-admin service account using a clusterrolebinding.
- Prove that the full-access-admin service account can create, get, list, delete, and update pods in all namespaces but cannot do the same for deployments.

### CLI Commands

``` bash

cb0n3y@cka-k8s-master:~/cka_exam_preparation/RBAC$ kubectl create sa full-access-admin --namespace="*" -o yaml --dry-run=client > clusterrole-with-elevated-permissions.yaml
cb0n3y@cka-k8s-master:~/cka_exam_preparation/RBAC$ echo "---" >> clusterrole-with-elevated-permissions.yaml
cb0n3y@cka-k8s-master:~/cka_exam_preparation/RBAC$ kubectl create clusterrole cluster-admin-pods --resource=pods --verb=create,get,list,delete --namespace="*" -o yaml --dry-run=client >> clusterrole-with-elevated-permissions.yaml
cb0n3y@cka-k8s-master:~/cka_exam_preparation/RBAC$ echo "---" >> clusterrole-with-elevated-permissions.yaml
cb0n3y@cka-k8s-master:~/cka_exam_preparation/RBAC$ kubectl create clusterrolebinding bind-full-access-admin --clusterrole=cluster-admin-pods --serviceaccount=*:full-access-admin -o yaml --dry-run=client >> clusterrole-with-elevated-permissions.yaml
cb0n3y@cka-k8s-master:~/cka_exam_preparation/RBAC$ kubectl apply -f clusterrole-with-elevated-permissions.yaml

```


### YAML File

<details>
<sumary>Click to view the YAML file.</sumary>

``` yaml

apiVersion: v1
kind: ServiceAccount
metadata:
  creationTimestamp: null
  name: full-access-admin
  namespace: '*'
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  creationTimestamp: null
  name: cluster-admin-pods
rules:
- apiGroups:
  - ""
  resources:
  - pods
  verbs:
  - create
  - get
  - list
  - delete
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  creationTimestamp: null
  name: bind-full-access-admin
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: cluster-admin-pods
subjects:
- kind: ServiceAccount
  name: full-access-admin
  namespace: '*'

```

</details>


## Exercise 6: Deny Specific Permissions

- Create a service account called restricted-deployer in the production namespace.
- Create a role called limited-pod-creator that grants create permissions only to pods in the production namespace.
- Create a rolebinding named bind-limited-pod-creator that binds the limited-pod-creator role to the restricted-deployer service account.
- Create a deny policy using a PodSecurityPolicy that prevents the restricted-deployer from creating pods with privileged access in the production namespace.
- Prove that the restricted-deployer service account cannot create privileged pods in the production namespace but can create non-privileged pods.


### CLI Commands

``` bash

cb0n3y@cka-k8s-master:~/cka_exam_preparation/RBAC$ kubectl create ns production -o yaml --dry-run=client > deny-specific-permissions.yaml 
cb0n3y@cka-k8s-master:~/cka_exam_preparation/RBAC$ echo "---" >> deny-specific-permissions.yaml 
cb0n3y@cka-k8s-master:~/cka_exam_preparation/RBAC$ kubectl create sa restricted-deployer -n production -o yaml --dry-run=client >> deny-specific-permissions.yaml  
cb0n3y@cka-k8s-master:~/cka_exam_preparation/RBAC$ echo "---" >> deny-specific-permissions.yaml
cb0n3y@cka-k8s-master:~/cka_exam_preparation/RBAC$ kubectl create role limited-pod-creator --reosurce=pods --verb=create -n production -o yaml --dry-run=client >> deny-specific-permissions.yaml 
error: unknown flag: --reosurce
See 'kubectl create role --help' for usage.
cb0n3y@cka-k8s-master:~/cka_exam_preparation/RBAC$ kubectl create role limited-pod-creator --resource=pods --verb=create -n production -o yaml --dry-run=client >> deny-specific-permissions.yaml
cb0n3y@cka-k8s-master:~/cka_exam_preparation/RBAC$ echo "---" >> deny-specific-permissions.yaml
cb0n3y@cka-k8s-master:~/cka_exam_preparation/RBAC$ kubectl create rolebinding bind-limited-pod-creator --role=limited-pod-creator --serviceaccount=production:restricted-deployer -n production -o yaml --dry-run=client >> deny-specific-permissions.yaml

cb0n3y@cka-k8s-master:~/cka_exam_preparation/RBAC$ kubectl --as=system:serviceaccount:production:restricted-deployer auth can-i create pods -n production
yes
cb0n3y@cka-k8s-master:~/cka_exam_preparation/RBAC$ kubectl --as=system:serviceaccount:production:restricted-deployer auth can-i list pods -n production
no

```


### YAML File

<details>
<sumary>Click to view the YAML file.</sumary>

``` yaml

apiVersion: v1
kind: Namespace
metadata:
  creationTimestamp: null
  name: production
spec: {}
status: {}
---
apiVersion: v1
kind: ServiceAccount
metadata:
  creationTimestamp: null
  name: restricted-deployer
  namespace: production
---
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  creationTimestamp: null
  name: limited-pod-creator
  namespace: production
rules:
- apiGroups:
  - ""
  resources:
  - pods
  verbs:
  - create
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  creationTimestamp: null
  name: bind-limited-pod-creator
  namespace: production
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: Role
  name: limited-pod-creator
subjects:
- kind: ServiceAccount
  name: restricted-deployer
  namespace: production
 
```

</details>


## Exercise 7: Permissions with Multiple Roles

- Create a namespace called staging-environment.
- Create a service account called web-developer in the staging-environment namespace.
- Create two roles in the staging-environment namespace:

    - pod-viewer with get and list permissions on pods.
    - deployment-manager with get, list, and create permissions on deployments.

- Create two rolebindings:

    - Bind the pod-viewer role to the web-developer service account.
    - Bind the deployment-manager role to the same web-developer service account.

- Prove that the web-developer service account can get, list, and create deployments but cannot delete pods.


### CLI Commands

``` bash

cb0n3y@cka-k8s-master:~/cka_exam_preparation/RBAC$ kubectl create ns staging-environment -oyaml --dry-run=client > perm-with-multiple-roles.yaml
cb0n3y@cka-k8s-master:~/cka_exam_preparation/RBAC$ echo "---" >> perm-with-multiple-roles.yam
cb0n3y@cka-k8s-master:~/cka_exam_preparation/RBAC$ kubectl create sa web-developer -n staging-environment -oyaml --dry-run=client >> perm-with-multiple-roles.yaml 
cb0n3y@cka-k8s-master:~/cka_exam_preparation/RBAC$ echo "---" >> perm-with-multiple-roles.yaml
cb0n3y@cka-k8s-master:~/cka_exam_preparation/RBAC$ kubectl create role pod-viewer --resource=pods --verb=get,list -n staging-environment -oyaml --dry-run=client >> perm-with-multiple-roles.yaml 
cb0n3y@cka-k8s-master:~/cka_exam_preparation/RBAC$ echo "---" >> perm-with-multiple-roles.yaml
cb0n3y@cka-k8s-master:~/cka_exam_preparation/RBAC$ kubectl create role deployment-manager --resource=deployments --verb=get,list,create -n staging-environment -oyaml --dry-run=client >> perm-with-multiple-roles.yaml
cb0n3y@cka-k8s-master:~/cka_exam_preparation/RBAC$ echo "---" >> perm-with-multiple-roles.yaml
cb0n3y@cka-k8s-master:~/cka_exam_preparation/RBAC$ kubectl create rolebinding bind-pod-viewer --role=pod-viewer --serviceaccount=staging-environment:web-developer -n staging-environment -oyaml --dry-run=client >> perm-with-multiple-roles.yaml
cb0n3y@cka-k8s-master:~/cka_exam_preparation/RBAC$ echo "---" >> perm-with-multiple-roles.yaml
cb0n3y@cka-k8s-master:~/cka_exam_preparation/RBAC$ kubectl create rolebinding bind-deployment-manager --role=deployment-manager --serviceaccount=staging-environment:web-developer -n staging-environment -oyaml --dry-run=client >> perm-with-multiple-roles.yaml

cb0n3y@cka-k8s-master:~/cka_exam_preparation/RBAC$ kubectl --as=system:serviceaccount:staging-environment:web-developer auth can-i list pods -n staging-environment
yes
cb0n3y@cka-k8s-master:~/cka_exam_preparation/RBAC$ kubectl --as=system:serviceaccount:staging-environment:web-developer auth can-i get pods -n staging-environment
yes
cb0n3y@cka-k8s-master:~/cka_exam_preparation/RBAC$ kubectl --as=system:serviceaccount:staging-environment:web-developer auth can-i create pods -n staging-environment
no
cb0n3y@cka-k8s-master:~/cka_exam_preparation/RBAC$ kubectl --as=system:serviceaccount:staging-environment:web-developer auth can-i get deployments -n staging-environment
yes
cb0n3y@cka-k8s-master:~/cka_exam_preparation/RBAC$ kubectl --as=system:serviceaccount:staging-environment:web-developer auth can-i create deployments -n staging-environment
yes
cb0n3y@cka-k8s-master:~/cka_exam_preparation/RBAC$ kubectl --as=system:serviceaccount:staging-environment:web-developer auth can-i list deployments -n staging-environment
yes
cb0n3y@cka-k8s-master:~/cka_exam_preparation/RBAC$ kubectl --as=system:serviceaccount:staging-environment:web-developer auth can-i delete deployments -n staging-environment
no

```


### YAML File

<details>
<sumary>Click to view the YAML file.</sumary>

``` yaml

apiVersion: v1
kind: Namespace
metadata:
  creationTimestamp: null
  name: staging-environment
spec: {}
status: {}
---
apiVersion: v1
kind: ServiceAccount
metadata:
  creationTimestamp: null
  name: web-developer
  namespace: staging-environment
---
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  creationTimestamp: null
  name: pod-viewer
  namespace: staging-environment
rules:
- apiGroups:
  - ""
  resources:
  - pods
  verbs:
  - get
  - list
---
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  creationTimestamp: null
  name: deployment-manager
  namespace: staging-environment
rules:
- apiGroups:
  - apps
  resources:
  - deployments
  verbs:
  - get
  - list
  - create
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  creationTimestamp: null
  name: bind-pod-viewer
  namespace: staging-environment
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: Role
  name: pod-viewer
subjects:
- kind: ServiceAccount
  name: web-developer
  namespace: staging-environment
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  creationTimestamp: null
  name: bind-deployment-manager
  namespace: staging-environment
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: Role
  name: deployment-manager
subjects:
- kind: ServiceAccount
  name: web-developer
  namespace: staging-environment

```

</details>


## Exercise 8: Impersonation and Fine-Grained Access

- Create a service account called report-viewer in the finance namespace.
- Create a role called financial-reports with get and list permissions on configmaps in the finance namespace.
- Bind the financial-reports role to the report-viewer service account using a rolebinding.
- Use the --as flag to impersonate the report-viewer service account and try to access a configmap in the finance namespace.
- Prove that the impersonated report-viewer can read configmaps but cannot perform any modifications (e.g., create, delete) to them.


### CLI Commands

``` bash

cb0n3y@cka-k8s-master:~/cka_exam_preparation/RBAC$ kubectl create ns finance -oyaml --dry-run=client > impersonation-and-fine-grained-access.yaml 
cb0n3y@cka-k8s-master:~/cka_exam_preparation/RBAC$ echo "---" >> impersonation-and-fine-grained-access.yaml 
cb0n3y@cka-k8s-master:~/cka_exam_preparation/RBAC$ kubectl create sa report-viewer -n finance -oyaml --dry-run=client >> impersonation-and-fine-grained-access.yaml 
cb0n3y@cka-k8s-master:~/cka_exam_preparation/RBAC$ echo "---" >> impersonation-and-fine-grained-access.yaml
cb0n3y@cka-k8s-master:~/cka_exam_preparation/RBAC$ kubectl create role financial-reports --resource=configmaps --verb=get,list -n finance -oyaml --dry-run=client >> impersonation-and-fine-grained-access.yaml 
cb0n3y@cka-k8s-master:~/cka_exam_preparation/RBAC$ echo "---" >> impersonation-and-fine-grained-access.yaml
cb0n3y@cka-k8s-master:~/cka_exam_preparation/RBAC$ kubectl create rolebinding bind-financial-reports --role=financial-reports --serviceaccount=finance:report-viewer -n finance -oyaml --dry-run=client >> impersonation-and-fine-grained-access.yaml

cb0n3y@cka-k8s-master:~/cka_exam_preparation/RBAC$ kubectl --as=system:serviceaccount:finance:report-viewer auth can-i list configmaps -n finance
yes
cb0n3y@cka-k8s-master:~/cka_exam_preparation/RBAC$ kubectl --as=system:serviceaccount:finance:report-viewer auth can-i get configmaps -n finance
yes
cb0n3y@cka-k8s-master:~/cka_exam_preparation/RBAC$ kubectl --as=system:serviceaccount:finance:report-viewer auth can-i create configmaps -n finance
no
cb0n3y@cka-k8s-master:~/cka_exam_preparation/RBAC$ kubectl --as=system:serviceaccount:finance:report-viewer auth can-i delete configmaps -n finance
no

```


### YAML File

<details>
<sumary>Click to view the YAML file.</sumary>

``` yaml

apiVersion: v1
kind: Namespace
metadata:
  creationTimestamp: null
  name: finance
spec: {}
status: {}
---
apiVersion: v1
kind: ServiceAccount
metadata:
  creationTimestamp: null
  name: report-viewer
  namespace: finance
---
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  creationTimestamp: null
  name: financial-reports
  namespace: finance
rules:
- apiGroups:
  - ""
  resources:
  - configmaps
  verbs:
  - get
  - list
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  creationTimestamp: null
  name: bind-financial-reports
  namespace: finance
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: Role
  name: financial-reports
subjects:
- kind: ServiceAccount
  name: report-viewer
  namespace: finance

```

</details>


## Exercise 9: Use of ServiceAccount with External Access

- Create a service account named external-agent in the operations namespace.
- Create a role called pod-monitor that grants the get, list, and watch permissions on pods in the operations namespace.
- Bind the pod-monitor role to the external-agent service account.
- Generate a kubeconfig file for the external-agent service account and use it to access pods from an external machine or environment.
- Prove that the external-agent service account can watch pods in the operations namespace, even from an external machine.


### CLI Commands

``` bash

echo ""

```


### YAML File

<details>
<sumary>Click to view the YAML file.</sumary>

``` yaml
---
- name: test

```
</details>


## Exercise 10: Advanced Role with Multiple Resources and APIGroup

- Create a namespace called security.
- Create a service account called sec-auditor in the security namespace.
- Create a role called sec-audit that grants get and list permissions for the following resources across different APIGroups:

    - secrets in the core API group.
    - auditlogs in the audit.k8s.io API group.

- Bind the sec-audit role to the sec-auditor service account.
- Prove that the sec-auditor service account can get and list secrets and auditlogs but cannot modify or create any of these resources.

### CLI Commands

``` bash

echo "test"

```


### YAML File

<details>
<sumary>Click to view the YAML file.</sumary>

``` yaml

---
- name: test

```
</details>

