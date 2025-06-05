#!/bin/bash

set e

PROM_SRV="xxx.xxx.xxx.xxx"
GRAF_SRV="xxx.xxx.xxx.xxx"
PORTS=(3000 9100)

# create_repository() {
#     echo -e "\n[+] Creating Prometheus repository ..."

#     if [[ -e "$TARGET_FILE" ]]; then
#         echo "The repo file already exists."
#     else
#         cat > "$TARGET_FILE" <<EOF
# [prometheus]
# name=prometheus
# baseurl=https://packagecloud.io/prometheus-rpm/release/el/\$releasever/\$basearch
# repo_gpgcheck=1
# enabled=1
# gpgkey=https://packagecloud.io/prometheus-rpm/release/gpgkey
#         https://raw.githubusercontent.com/lest/prometheus-rpm/master/RPM-GPG-KEY-prometheus-rpm
# gpgcheck=1
# metadata_expire=300
# EOF
#     fi

#     echo -e "\n[+] Repository created"
# }

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

create_hosts_file() {
    echo -e "\n[+] Generating hosts file for DNS resolution..."

    echo "" >> /etc/hosts
    echo "$PROM_SRV     dev-prometheus01.fritz.box  dev-prometheus01" >> /etc/hosts
    echo "$GRAF_SRV     dev-grafana01.fritz.box  dev-grafana01" >> /etc/hosts
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
create_hosts_file
