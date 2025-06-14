#!/bin/bash

set -euo pipefail

PORTS=(3000 9100)

# Function to install Grafana repository
create_grafana_repository() {
    echo -e "\n[+] Adding Grafana repository..."

    # Download GPG key and import it
    wget -q -O /etc/pki/rpm-gpg/gpg.key https://rpm.grafana.com/gpg.key
    rpm --import /etc/pki/rpm-gpg/gpg.key

    # Create the Grafana repository file
    cat > /etc/yum.repos.d/grafana.repo <<EOF
[grafana]
name=grafana
baseurl=https://rpm.grafana.com
repo_gpgcheck=1
enabled=1
gpgcheck=1
gpgkey=https://rpm.grafana.com/gpg.key
sslverify=1
sslcacert=/etc/pki/tls/certs/ca-bundle.crt
EOF

    echo -e "\n[+] Grafana repository added."
}

install_packages() {
    echo -e "\n[+] Installing packages..."

    dnf -y update
    dnf -y install grafana
    systemctl enable --now grafana-server.service
}

# create_repository
create_grafana_repository
install_packages
