# Ops to DevOps

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![GitHub Repo Size](https://img.shields.io/github/repo-size/cb0n3y/ops-to-devops)
![Last Commit](https://img.shields.io/github/last-commit/cb0n3y/ops-to-devops)
![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/cb0n3y/ops-to-devops/ci.yml?label=CI%2FCD)

Welcome to the **Ops to DevOps** repository! This project documents my journey transitioning from a System Administrator to a DevOps Engineer, showcasing the skills, tools, and projects I've developed along the way.

---

## 📑 Table of Contents

- [Repository Structure](#repository-structure)
- [Lab](#lab)
- [IaaC](#iaac)
- [Deployment Strategy](#deployment-strategy)
- [Getting Started](#getting-started)
- [Contributing](#contributing)
- [License](#license)

---

## Repository Structure

The repository is organized into two main sections:

- **Lab/**: Hands-on configurations, scripts, and documentation related to various DevOps tools and technologies.
- **IaaC/**: Infrastructure as Code examples, including tools such as Vagrant, Ansible, Terraform, and others. These projects demonstrate infrastructure provisioning, automation, and environment management. 

---

## Lab

This section includes:

- **Ansible**: Playbooks and roles for automation.
- **Bash**: Scripts for various administrative tasks.
- **Python**: Automation and utility scripts.
- **Docker**: Containerization setups.
- **Kubernetes**: Deployment configurations.
- **CI/CD**: Continuous Integration and Deployment pipelines.
- **Monitoring**: Tools and configurations for system monitoring.
- **Security**: Implementations to ensure system integrity.
- **Networking**: Configurations and scripts related to network management.

> Each subfolder contains a `README.md` with detailed information and usage instructions.

---

## IaaC

The IaaC/ directory represents a complete infrastructure setup, structured into different environments:

- **base/**: Shared configurations across all environments.
- **staging/**: Environment for testing and validation.
- **production/**: Live environment configurations.

Each environment includes:

- **applications/**: Deployed applications.
- **configs/**: Configuration files.
- **monitoring/**: Monitoring setups.
- **security/**: Security implementations.

---

## Deployment Strategy

Deployments are managed using Git tags:

- **`vX.Y.Z`**: Deploys to production.
- **`vX.Y.Z-beta`**: Deploys to staging.

Automated pipelines ensure smooth and consistent deployments across environments.

---

## Getting Started

To explore this repository:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/cb0n3y/ops-to-devops.git
   cd ops-to-devops

2. **Navigate through the directories** to explore various tools, configurations, and projects
3. **Refer to individual** README.md files within each folder for detailed instructions and information.

## Contributing
This repository is primarily a personal portfolio, but community contributions and feedback are welcome.
Feel free to open an issue or submit a pull request for improvements or fixes.

## License
This project is licensed under the MIT License.