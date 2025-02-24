# Storage

Exercise 1: Create a Persistent Volume (PV) and Persistent Volume Claim (PVC)

    Task: Create a Persistent Volume (PV) named data-volume of size 5Gi in the /mnt/data directory of a node. Then, create a Persistent Volume Claim (PVC) named data-claim that requests 3Gi of storage.
    Objective: Learn how to manually create and bind PVs and PVCs.

Exercise 2: Bind PVC to PV

    Task: Bind the data-claim PVC from the previous exercise to the data-volume PV by ensuring the storageClassName in the PVC matches that of the PV. Confirm the binding is successful by checking kubectl get pvc.
    Objective: Learn how PVCs are bound to PVs and the importance of storageClassName.

Exercise 3: Use Storage Class to Create Dynamic PV

    Task: Create a Storage Class named fast-storage that uses the provisioner kubernetes.io/aws-ebs (or an equivalent for your environment). Then, create a PVC using this storage class and request 10Gi of storage. Ensure the dynamic volume is provisioned automatically.
    Objective: Understand how Storage Classes are used for dynamic provisioning of Persistent Volumes.

Exercise 4: Create a Pod Using PVC

    Task: Create a Pod that mounts the data-claim PVC (from Exercise 2) to /data inside the container. The Pod should use the nginx image and be created in the default namespace.
    Objective: Learn how to mount persistent volumes inside pods.

Exercise 5: Modify PVC Request Size

    Task: Modify the data-claim PVC from Exercise 2 to request 10Gi instead of 3Gi, and apply the changes. Verify that the PVC is updated and the volume is resized if applicable.
    Objective: Understand how to modify PVCs and the behavior of resizing volumes.

Exercise 6: Troubleshoot PVC Not Binding to PV

    Task: Create a new PVC that requests 8Gi of storage but doesn't match any available PVs. Use kubectl describe pvc to troubleshoot why the PVC is not binding, and then adjust the PV or PVC to resolve the issue.
    Objective: Gain troubleshooting skills related to PVC-PV binding issues.

Exercise 7: Create a StatefulSet with Persistent Storage

    Task: Deploy a StatefulSet for a nginx application that uses a PVC to store data. The StatefulSet should have 3 replicas, and each replica should have its own persistent volume.
    Objective: Learn how to create a StatefulSet and ensure each replica gets its own Persistent Volume.

Exercise 8: Set Reclaim Policy for PV

    Task: Create a Persistent Volume (PV) with a ReclaimPolicy set to Retain. Then, create a PVC and bind it to the PV. Delete the PVC and observe that the PV is retained. Test the behavior by creating a new PVC with the same name and binding it to the retained PV.
    Objective: Understand the different reclaim policies (Delete, Retain, Recycle) and how they affect PVs after PVC deletion.

Exercise 9: Create a Shared Volume Using ReadWriteMany

    Task: Create a Persistent Volume that supports ReadWriteMany access mode. Then, create a PVC and mount it in two different Pods, ensuring that both Pods can read and write to the same volume.
    Objective: Learn how to work with volumes that support ReadWriteMany access mode and share storage between Pods.

Exercise 10: Backup and Restore a PVC

    Task: Use a third-party tool like Velero (or any other backup tool) to back up the persistent volume data from the data-claim PVC created in earlier exercises. Then, restore it to a new PVC and verify the data is intact by checking the contents inside a Pod that mounts the restored PVC.
    Objective: Understand how to back up and restore persistent volumes using a third-party tool.

Summary of the Exercises

    Create a Persistent Volume (PV) and Persistent Volume Claim (PVC)
    Learn basic creation of PVs and PVCs.

    Bind PVC to PV
    Understand the process of binding PVCs to PVs.

    Use Storage Class to Create Dynamic PV
    Learn how to provision dynamic volumes using Storage Classes.

    Create a Pod Using PVC
    Mount a PVC inside a pod.

    Modify PVC Request Size
    Learn how to resize PVCs and how volumes behave during resizing.

    Troubleshoot PVC Not Binding to PV
    Troubleshoot issues when PVCs don't bind to available PVs.

    Create a StatefulSet with Persistent Storage
    Learn how StatefulSets use persistent storage for each replica.

    Set Reclaim Policy for PV
    Understand reclaim policies and how they impact volume lifecycle.

    Create a Shared Volume Using ReadWriteMany
    Learn how to create and manage shared volumes with ReadWriteMany.

    Backup and Restore a PVC
    Learn how to back up and restore persistent data in Kubernetes.

