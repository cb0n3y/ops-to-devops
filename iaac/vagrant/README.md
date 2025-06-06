# Vagrant Environment Setup

This directory defines the infrastructure setup for local VM-based environments using Vagrant.

## Environments

- `dev/`: Developer environment — local, experimental.
- `staging/`: Pre-production testing environment.
- `prod/`: Simulated production environment.

Each environment contains:
- A `Vagrantfile` for provisioning
- Environment-specific provisioning scripts (minimal)
- Monitoring stack: Prometheus + Grafana

## Shared Scripts

Located in `shared-scripts/`, these contain reusable logic like:
- Adding users
- Installing exporters
- Deploying Prometheus config
- Configuring firewall rules

---
