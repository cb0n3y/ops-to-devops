
#!/usr/bin/env bash
set -euo pipefail

# DevOps Solutions with Bash
# Author: cb0n3y
# Scriptname: export-keys.sh
# Usage: Run the script and follow the interactive prompts
# Description: Export legacy apt-key entries to /etc/apt/keyrings in dearmored format
# Author: cb0n3y
# Created: 2025-06-25


TARGET_PATH='/etc/apt/keyrings'

log_info() { echo -e "\033[0;32m[+] $1\033[0m"; }
log_warn() { echo -e "\033[0;31m[!] $1\033[0m"; }

print_header() {
    echo "-----------------------------------------"
    log_info "APT Key Management Helper"
    echo "-----------------------------------------"
}

migrate_legacy_key() {
    # Ask user to list legacy keys
    echo -e "\nExisting legacy keys:\n"
    apt-key list
    read -rp "[?] Enter full legacy key ID to export: " KEY_ID
    read -rp "[?] Enter filename to save key as (e.g. trivy.gpg): " KEY_NAME

    local key_path="$TARGET_PATH/$KEY_NAME"

    if [[ -f "$key_path" ]]; then
        log_warn "File $key_path already exists, aborting."
        exit 1
    fi

    log_info "Exporting legacy key $KEY_ID and converting to $key_path"
    sudo mkdir -p "$TARGET_PATH"
    sudo apt-key export "$KEY_ID" | sudo gpg --dearmor -o "$key_path"
    log_info "Legacy key migrated successfully."
}

add_key_from_url() {
    read -rp "[?] Enter URL to key (.gpg or .asc): " KEY_URL
    read -rp "[?] Enter filename to save key as (e.g. trivy-archive-keyring.gpg): " KEY_NAME

    local key_path="$TARGET_PATH/$KEY_NAME"
    if [[ -f "$key_path" ]]; then
        log_warn "File $key_path already exists, aborting."
        exit 1
    fi

    log_info "Downloading and dearmoring key from $KEY_URL"
    sudo mkdir -p "$TARGET_PATH"
    curl -fsSL "$KEY_URL" | sudo gpg --dearmor -o "$key_path"
    log_info "Key added successfully."
}

main() {
    print_header

    echo "Select an option:"
    echo "1) Migrate existing legacy apt-key to new keyring"
    echo "2) Add new key from URL"
    read -rp "[?] Choice (1 or 2): " choice

    case "$choice" in
        1) migrate_legacy_key ;;
        2) add_key_from_url ;;
        *) log_warn "Invalid option selected. Exiting."; exit 2 ;;
    esac
}

main "$@"
