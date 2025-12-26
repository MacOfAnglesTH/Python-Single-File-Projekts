# Ubuntu 24.04 Low-Touch Deployment Pipeline
### This repository contains the orchestration logic for a streamlined, automated deployment pipeline for Ubuntu 24.04 LTS. By integrating PXE booting, Cloud-init, Python-based networking, and Ansible, this project reduces manual technician intervention to a single initial boot.
### 🚀 Workflow Overview
The deployment follows a hands-off, three-stage process:

1. Automated Provisioning: The machine boots via PXE, pulling the Ubuntu 24.04 ISO and applying initial configurations through Cloud-init.

2. Identity & Connectivity: A post-install Python script executes to dynamically assign the computer name (hostname) and establish stable network parameters.

3. Final Orchestration: Once the system is online, the Ansible server pulls the node into its inventory to apply final software packages, security hardening, and custom configurations.

### 🛠 Tech Stack
- OS: Ubuntu 24.04 LTS
- Provisioning: PXE Server (TFTP/DHCP) & Cloud-init
- Scripting: Python 3.6.8
- YMAL
- Configuration Management: Ansible

### 🐍 Python (SUDO needed)
The Python script processes the following user inputs:
1. Hostname
2. IP address
3. Network prefix

After receiving these values, the script performs several steps:

1. Updates the system hostname
2. Detects the active (plugged‑in) network interface
3. Calculates the required network configuration
4. Generates a Netplan YAML file with the new settings
5. Applies the Netplan configuration and restarts the system

These settings are essential for preparing the machine to join the Ansible-managed network environment.

##### #python, #ymal, #linux, #network-programming
##### 🔒 To maintain the confidentiality, some inputs and variable names in these scripts have been modified or anonymized.