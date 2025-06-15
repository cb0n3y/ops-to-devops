# Arch Linux Vagrant Workstation

This repository contains a Vagrantfile to spin up a lightweight Arch Linux virtual machine intended as a DevOps workstation or learning environment.

## 🛠️ Features

- Based on [`terrywang/archlinux`](https://app.vagrantup.com/terrywang/boxes/archlinux) base box (version `4.24.0529`)
- Public IP configured via `public_network`
- Automatically sets hostname and updates `/etc/hosts`
- Performs a full system update on first boot using `pacman -Syyu --noconfirm`
- GUI disabled (`vb.gui = false`) for resource efficiency
- CPU and memory settings customizable via variables at the top of the `Vagrantfile`

## 📦 Prerequisites

- [Vagrant](https://www.vagrantup.com/) installed
- [VirtualBox](https://www.virtualbox.org/) installed

## 🚀 Usage

Clone the repository and run:

```bash
vagrant up
```

⚠️ **IMPORTANT**: During the provisioning phase, Vagrant will prompt you to select a physical network interface to bridge the VM to. Be sure to choose the correct one (e.g., your Wi-Fi or Ethernet interface), or the setup will fail.

Once the VM is up, you can SSH into it:

```bash
vagrant ssh wks
```

## 📋 Notes

- The VM will update all packages during the first boot using pacman -Syyu --noconfirm to avoid manual confirmation prompts. This ensures the system is fully up to date without requiring input.
- The keyboard layout is set to de-latin1.
- The hostname is set to wks and mapped to 192.168.178.106 via /etc/hosts.

## 📂 Project Structure

```bash
.
├── Vagrantfile   # Main Vagrant configuration
└── README.md     # This file
```

## 🔧 Configuration

You can adjust CPU and memory allocations by editing the following variables at the top of the Vagrantfile:

```bash
BOX_CPUS = 4
BOX_RAM  = 8192
```

## 📞 Support

This project is primarily for personal use and experimentation. Issues and suggestions are welcome.
