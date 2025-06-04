#!/bin/bash

set e

set_fw_rules() {
    # Use ports from environment variable or fall back to default
    IFS=' ' read -r -a ports <<< "${PORTS: 3000 9100}"

    echo -e "\n[+] Adding required firewall rules for ports: ${ports[*]}"

    # Check if firewalld is running
    if ! systemctl is-active --quiet firewalld; then
        echo "firewalld is not running. Attempting to start..."
        systemctl start firewalld
        systemctl enable firewalld
    fi

    # Add each port to firewalld
    for port in "${ports[@]}"; do
        firewall-cmd --permanent --add-port="$port"/tcp
    done

    echo "[*] Reloading firewalld..."
    firewall-cmd --reload

    echo -e "\n[+] Firewall rules successfully configured."
}

set_fw_rules