# This Python generate the remmina profiles, for new installation slax servers.
Still in developing... final version will be publish soon 26.12.2025 Mac

### 🐍 Python
Slax Server is a lightweight Linux system designed for easy OS deployment—typically just copy, paste, and run a command.

However, both the network configuration and the Remmina remote‑client profiles are unique to each machine and cannot be pre‑injected into the operating system image.

Because the OS is frequently reinstalled after failures, the network settings and Remmina profiles must be manually recreated each time.
Remmina supports two connection protocols: VNC and RDP.

This Python script is intended to automate that setup process. It will:
1. Request the hostname from the user
2. Request the network interface name, or automatically detect the active interface
3. Read a list of Remmina profiles and their configuration values
4. Apply the configuration values to the profile templates
5. Write the generated Remmina profile files to the local system

##### #python, #linux, #network-programming
##### 🔒 To maintain the confidentiality, some inputs and variable names in these scripts have been modified or anonymized.
