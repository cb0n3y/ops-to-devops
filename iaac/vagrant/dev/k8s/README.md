# Kubernetes Dev Lab with Vagrant and CentOS 9 Stream

This Vagrant project provisions a local multi-node Kubernetes lab using VirtualBox and CentOS 9 Stream. It includes one master node and three worker nodes, each with static IP addresses and preconfigured `/etc/hosts` for seamless name resolution.

---

## 📦 Included VMs

| Role   | Hostname           | IP Address       |
|--------|--------------------|------------------|
| Master | `dev-k8s-master`   | `192.168.178.102`|
| Node 1 | `dev-k8s-node01`   | `192.168.178.103`|
| Node 2 | `dev-k8s-node02`   | `192.168.178.104`|
| Node 3 | `dev-k8s-node03`   | `192.168.178.105`|

---

## ⚙️ System Requirements

- [Vagrant](https://www.vagrantup.com/) ≥ 2.2
- [VirtualBox](https://www.virtualbox.org/) ≥ 6.1
- At least 16 GB RAM and 4 CPUs available for VMs
- Internet access for the base box download

---

## 🚀 Getting Started

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/dev-k8s-lab.git
   cd dev-k8s-lab
    ```

2. Start the Environment

    ```bash
    vagrant up
    ```

3. Access Machines

    ```bash
    vagrant ssh master
    vagrant ssh node-1
    vagrant ssh node-2
    vagrant ssh node-3
    ```

## 🛠 Provisioning Details

- All VMs use the generic/centos9s Vagrant box.
- Mirrors are optimized with fastestmirror=True and parallel downloads.
- Static /etc/hosts entries are configured on each VM for internal name resolution.
- Each VM is assigned:
    - 2 CPUs
    - 4 GB RAM
    - VirtualBox group: /DevOps-Lab/K8S

## 🧪 Use Cases

- CKA preparation & practice
- Manual Kubernetes bootstrapping with kubeadm
- Local testing of Helm charts, CNI plugins, etc.
- DevOps automation experiments

## 🧹 Cleanup

To destroy the environment and free resources:

    ```bash
    vagrant destroy -f
    ```

## 📁 Directory Structure

    ```bash
    .
    ├── Vagrantfile
    └── README.md
    ```

## 📌 Notes

- This lab uses bridged networking (public_network) and assumes you're in a private network (like a home LAN).
- Modify IPs in the Vagrantfile if they conflict with your network.
- If Docker fails to start, ensure necessary kernel modules (e.g., nf_tables, iptable_nat) are present and your system matches the correct kernel version.

