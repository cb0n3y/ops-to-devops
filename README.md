# Ops to DevOps

Welcome to the **Ops to DevOps** repository! This project documents my journey transitioning from a System Administrator to a DevOps Engineer, showcasing the skills, tools, and projects I've developed along the way.

## Repository Structure

The repository is organized into two main sections:

- **Lab/**: Contains configurations, scripts, and documentation of various tools and technologies I've learned and implemented.
- **HomeLab/**: Features applications and projects I've developed, structured into different environments: `base`, `staging`, and `production`.

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

Each subfolder contains a `README.md` with detailed information and usage instructions.

## HomeLab

The HomeLab is structured as follows:

- **base/**: Shared configurations across all environments.
- **staging/**: Environment for testing and validation.
- **production/**: Live environment configurations.

Within each environment, you'll find:

- **applications/**: Deployed applications.
- **configs/**: Configuration files.
- **monitoring/**: Monitoring setups.
- **security/**: Security implementations.

## Deployment Strategy

Deployments are managed using Git tags:

- **`vX.Y.Z`**: Deploys to production.
- **`vX.Y.Z-beta`**: Deploys to staging.

Automated pipelines ensure smooth and consistent deployments across environments.

## Getting Started

To explore this repository:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/cb0n3y/ops-to-devops.git
   cd ops-to-devops

2. **Navigate through the directories** to explore various tools, configurations, and projects
3. **Refer to individual** README.md files within each folder for detailed instructions and information.

## Contributing
While this repository primarily serves as a personal portfolio, feedback and suggestions are welcome. Feel free to open issues or submit pull requests for improvements.

## License
This project is licensed under the MIT License.