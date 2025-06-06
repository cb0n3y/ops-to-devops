# Grafana Lab Setup

This directory contains the files and scripts to deploy and configure a Grafana instance for monitoring in the lab environment.

## Overview

Grafana is an open-source platform for monitoring and observability.  
In this lab, we deploy Grafana using Vagrant on a CentOS 9 Stream VM and configure it to visualize metrics collected by Prometheus.

## Structure

- `Vagrantfile` — Defines the Grafana VM and its provisioning steps.  
- `scripts/graf-setup.sh` — Installs and configures Grafana inside the VM.  
- `dashboards/` — (Future) Folder to hold JSON dashboard definitions for Grafana.  

## Usage

1. Start the Grafana VM:

   ```bash
   vagrant up grafana
   ```

2. Access Grafana by navigating to:

    ```bash
    http://<grafana-vm-ip>:3000
    ```

3. Default Grafana credentials:

    ```pgsql
    admin / admin
    ```

4. Import dashboards or create your own for monitoring.

## Notes

- The Grafana setup is integrated with Prometheus as the primary data source.
- Firewall rules are set during provisioning to allow necessary ports.
- DNS resolution for Prometheus and Grafana hosts is managed inside the VM