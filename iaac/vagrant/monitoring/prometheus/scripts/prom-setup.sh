#!/bin/bash

set e

TARGET_FILE='/etc/yum.repos.d/prometheus.repo'
PROM_SRV="xxx.xxx.xxx.xxx"
GRAF_SRV="xxx.xxx.xxx.xxx"
PORTS=(9090 9100)

create_repository() {
    echo -e "\n[+] Creating Prometheus repository ..."

    if [[ -e "$TARGET_FILE" ]]; then
        echo "The repo file already exists."
    else
        cat > "$TARGET_FILE" <<EOF
[prometheus]
name=prometheus
baseurl=https://packagecloud.io/prometheus-rpm/release/el/\$releasever/\$basearch
repo_gpgcheck=1
enabled=1
gpgkey=https://packagecloud.io/prometheus-rpm/release/gpgkey
        https://raw.githubusercontent.com/lest/prometheus-rpm/master/RPM-GPG-KEY-prometheus-rpm
gpgcheck=1
metadata_expire=300
EOF
    fi

    echo -e "\n[+] Repository created"
}

create_hosts_file() {
    echo -e "\n[+] Generating hosts file for DNS resolution..."

    # Change the host names as required
    echo "" >> /etc/hosts
    echo "$PROM_SRV     dev-prometheus01.fritz.box  dev-prometheus01" >> /etc/hosts
    echo "$GRAF_SRV     dev-grafana01.fritz.box  dev-grafana01" >> /etc/hosts
}

install_prometheus() {
    echo -e "\n[+] Installing prometheus..."

    dnf -y update
    dnf -y install prometheus node_exporter
    systemctl enable --now prometheus node_exporter.service
}

create_repository
install_prometheus
create_hosts_file
