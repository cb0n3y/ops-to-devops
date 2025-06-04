# Grafana VM (Vagrant)

This Vagrant setup provisions a CentOS 9 Stream virtual machine with GRafana installed and configured for local monitoring and testing.

## 📦 Requirements

- VirtualBox
- Vagrant
- Internet connection (for package installation)

## 🚀 Usage

1. Start the VM

```bash
vagrant up
```

2. Stop the VM

```bash
vagrant halt
```

3. Destroy the VM

```bash
vagrant destroy
```

Change to acces Grafana UI at: ttp://<your-grafanas-ip>:3000

## 🔧 Configuration

- **OS**: CentOS 9 Stream  
- **Grafana config path**: /etc/grafana/  
- **Setup script**: scripts/grafana-setup.sh  

## 📁 Folder structure

- **Vagrantfile**: defines VM settings and provisioning  
- **scripts/grafana-setup.sh**: installs and configures Grafana