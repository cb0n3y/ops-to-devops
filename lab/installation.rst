Installing and configuring Kubernetes with CRI-O in Ubuntu
==========================================================

i like nmcli, sure i can learn ip but i found out thgat to make an ip static and survive a rebbot take more than i was expected to give.
For that reason i decide to configure nmcl again and here are the steps to follow.

1. Install nmcli


.. code-block:: bash

    apt install network-manager -y


After that you have to edit ntwo diferent files:

1. Under  ``/etc/NetworkManager/NetworkManager.conf`` modify the following line:


.. code-block:: bash

    [ifupdown]
    managed=false   # before
    managed=true    # after


Save the changes

2. We have to tell Netplan that we want to manage our interfaces with NetworkManager. For that edit ``/etc/netplan/<file-name>.yaml

.. code-block:: bash


    network:
    ethernets:
        enp0s3:
            addresses:
            - 192.168.178.60/24     # new ip
            nameservers:
                addresses:
                - 192.168.178.1
                search: []
            routes:
            -   to: default
                via: 192.168.178.1
    version: 2
    renderer: NetworkManager    # new line added


After that just let Netplan get to know NetworkManager:


.. code-block:: bash

    netplan try

Restart also NetworkManager:


.. code-block:: bash

    systemctl restart NetworkManager.service


Install Kubernetes and dependencies
-----------------------------------

Enable iptables Bridged Traffic on all the Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. code-block:: bash


    cat <<EOF | sudo tee /etc/modules-load.d/k8s.conf
    overlay
    br_netfilter
    EOF

    sudo modprobe overlay
    sudo modprobe br_netfilter

    # sysctl params required by setup, params persist across reboots
    cat <<EOF | sudo tee /etc/sysctl.d/k8s.conf
    net.bridge.bridge-nf-call-iptables  = 1
    net.bridge.bridge-nf-call-ip6tables = 1
    net.ipv4.ip_forward                 = 1
    EOF

    # Apply sysctl params without reboot
    sudo sysctl --system

Disable swap on all the Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. code-block:: bash

    sudo swapoff -a
    (crontab -l 2>/dev/null; echo "@reboot /sbin/swapoff -a") | crontab - || true


Install CRI-O Runtime On All The Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash


    sudo apt-get update -y
    sudo apt-get install -y software-properties-common gpg curl apt-transport-https ca-certificates

    curl -fsSL https://pkgs.k8s.io/addons:/cri-o:/prerelease:/main/deb/Release.key |
        gpg --dearmor -o /etc/apt/keyrings/cri-o-apt-keyring.gpg
    echo "deb [signed-by=/etc/apt/keyrings/cri-o-apt-keyring.gpg] https://pkgs.k8s.io/addons:/cri-o:/prerelease:/main/deb/ /" |
        tee /etc/apt/sources.list.d/cri-o.list

    sudo apt-get update -y
    sudo apt-get install -y cri-o

    sudo systemctl daemon-reload
    sudo systemctl enable crio --now
    sudo systemctl start crio.service

Install crictl.

.. code-block:: bash

    VERSION="v1.30.0"
    wget https://github.com/kubernetes-sigs/cri-tools/releases/download/$VERSION/crictl-$VERSION-linux-amd64.tar.gz
    sudo tar zxvf crictl-$VERSION-linux-amd64.tar.gz -C /usr/local/bin
    rm -f crictl-$VERSION-linux-amd64.tar.gz


Install Kubeadm & Kubelet & Kubectl on all Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash


    KUBERNETES_VERSION=1.30

    sudo mkdir -p /etc/apt/keyrings
    curl -fsSL https://pkgs.k8s.io/core:/stable:/v$KUBERNETES_VERSION/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
    echo "deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v$KUBERNETES_VERSION/deb/ /" | sudo tee /etc/apt/sources.list.d/kubernetes.list


Update apt repo


.. code-block:: bash

    sudo apt-get update -y

You can use the following commands to find the latest versions. Install the first version in 1.30 so that you can practice cluster upgrade task.


.. code-block:: bash

    apt-cache madison kubeadm | tac

install the latest version from the repo use the following command without specifying any version.

.. code-block:: bash


    sudo apt-get install -y kubelet kubeadm kubectl


Add hold to the packages to prevent upgrades.


.. code-block:: bash


    sudo apt-mark hold kubelet kubeadm kubectl


Now we have all the required utilities and tools for configuring Kubernetes components using kubeadm.


Add the node IP to KUBELET_EXTRA_ARGS.

.. code-block:: bash

    sudo apt-get install -y jq
    local_ip="$(ip --json addr show eth0 | jq -r '.[0].addr_info[] | select(.family == "inet") | .local')"
    cat > /etc/default/kubelet << EOF
    KUBELET_EXTRA_ARGS=--node-ip=$local_ip
    EOF


Initialize Kubeadm On Master Node To Setup Control Plane
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


- Master Node with Private IP: If you have nodes with only private IP addresses the API server would be accessed over the private IP of the master node.
- Master Node With Public IP: If you are setting up a Kubeadm cluster on Cloud platforms and you need master Api server access over the Public IP of the master node server.


Only the Kubeadm initialization command differs for Public and Private IPs.

Execute the commands in this section only on the master node.

If you are using a Private IP for the master Node,

Set the following environment variables. Replace 10.0.0.10 with the IP of your master node.


.. code-block:: bash


    IPADDR="10.0.0.10"
    NODENAME=$(hostname -s)
    POD_CIDR="192.168.0.0/16"



If you want to use the Public IP of the master node,

Set the following environment variables. The IPADDR variable will be automatically set to the server’s public IP using ifconfig.me curl call. You can also replace it with a public IP address


.. code-block:: bash


    IPADDR=$(curl ifconfig.me && echo "")
    NODENAME=$(hostname -s)
    POD_CIDR="192.168.0.0/16"


Now, initialize the master node control plane configurations using the kubeadm command.

For a Private IP address-based setup use the following init command.


.. code-block:: bash


    sudo kubeadm init --apiserver-advertise-address="$IPADDR"  --apiserver-cert-extra-sans="$IPADDR"  --pod-network-cidr="$POD_CIDR" --node-name "$NODENAME"


For Public IP address-based setup use the following init command.

Here instead of --apiserver-advertise-address we use --control-plane-endpoint parameter for the API server endpoint.


.. code-block:: bash


    sudo kubeadm init --control-plane-endpoint=$IPADDR  --apiserver-cert-extra-sans=$IPADDR  --pod-network-cidr=$POD_CIDR --node-name $NODENAME --ignore-preflight-errors Swap


Use the following commands from the output to create the kubeconfig in master so that you can use kubectl to interact with cluster API.


.. code-block:: bash

    mkdir -p $HOME/.kube
    sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
    sudo chown $(id -u):$(id -g) $HOME/.kube/config


Now, verify the kubeconfig by executing the following kubectl command to list all the pods in the kube-system namespace.


.. code-block:: bash


    kubectl get po -n kube-system


You verify all the cluster component health statuses using the following command.



.. code-block:: bash


    kubectl get --raw='/readyz?verbose'

You can get the cluster info using the following command.


.. code-block:: bash


    kubectl cluster-info



Join Worker Nodes To Kubernetes Master Node
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


We have set up cri-o, kubelet, and kubeadm utilities on the worker nodes as well.

Now, let’s join the worker node to the master node using the Kubeadm join command you have got in the output while setting up the master node.

If you missed copying the join command, execute the following command in the master node to recreate the token with the join command.


.. code-block:: bash


    kubeadm token create --print-join-command

Here is what the command looks like. Use sudo if you running as a normal user. This command performs the TLS bootstrapping for the nodes.

.. code-block:: bash


    sudo kubeadm join 192.168.178.60:6443 --token 4xemhv.8kgzflob2qkbw2vx \
    --discovery-token-ca-cert-hash sha256:47132ef8b5782371ca6451540d3622afc63df3b8d40d116707f2acf958c6c6f9


Now execute the kubectl command from the master node to check if the node is added to the master.

.. code-block:: bash

    kubectl get nodes


Install Calico Network Plugin for Pod Networking
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Kubeadm does not configure any network plugin. You need to install a network plugin of your choice for kubernetes pod networking and enable network policy.


.. code-block:: bash


    kubectl apply -f https://docs.projectcalico.org/manifests/calico.yaml


Setup Kubernetes Metrics Server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Kubeadm doesn’t install metrics server component during its initialization. We have to install it separately.

To verify this, if you run the top command, you will see the Metrics API not available error.


.. code-block:: bash


    root@controlplane:~# kubectl top nodes

    error: Metrics API not available



To install the metrics server, execute the following metric server manifest file. It deploys metrics server version v0.7.1


.. code-block:: bash


    kubectl apply -f https://raw.githubusercontent.com/techiescamp/kubeadm-scripts/main/manifests/metrics-server.yaml


Add Kubeadm Config to Workstation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


If you prefer to connect the Kubeadm cluster using kubectl from your workstation, you can merge the kubeadm admin.conf with your existing kubeconfig file.

Follow the steps given below for the configuration.


Step 1: Copy the contents of admin.conf from the control plane node and save it in a file named kubeadm-config.yaml in your workstation.

Step 2: Take a backup of the existing kubeconfig.


.. code-block:: bash


    cp ~/.kube/config ~/.kube/config.bak


Step 3: Merge the default config with kubeadm-config.yaml and export it to KUBECONFIG variable

.. code-block:: bash


    export KUBECONFIG=~/.kube/config:/path/to/kubeadm-config.yaml


Step 4: Merger the configs to a file

.. code-block:: bash


    kubectl config view --flatten > ~/.kube/merged_config.yaml

Step 5: Replace the old config with the new config

.. code-block:: bash

    mv ~/.kube/merged_config.yaml ~/.kube/config


Step 6: List all the contexts


.. code-block:: bash


    kubectl config get-contexts -o name


Step 7: Set the current context to the kubeadm cluster.


.. code-block:: bash

    kubectl config use-context <cluster-name-here>



https://devopscube.com/setup-kubernetes-cluster-kubeadm/




