# Nginx Port 80 Configuration

This project contains a Bash script that configures Nginx to listen on port 80 of all the server's active IPv4 IPs. The script also installs Nginx if it's not already installed.

## Usage

1. Ensure you have the necessary permissions to execute the Bash script.

2. Run the Bash script to configure Nginx:

    ```bash
    ./fix_nginx.sh
    ```

   This script will update the Nginx configuration, install Nginx if needed, and restart Nginx to ensure it listens on port 80. It also checks the status of the Nginx service.

## Bash Script Details

- `fix_nginx.sh`: Bash script to configure Nginx to listen on port 80 and install Nginx if necessary.

## Requirements

- Ubuntu environment (tested on Ubuntu-based Docker container).
- Bash shell.
- Internet connectivity to install Nginx.

## Notes

- The script assumes an Ubuntu-based environment and uses `apt-get` for package management.
- The Nginx configuration file updated is `/etc/nginx/sites-available/default`.
- The script uses the `systemctl` command to restart Nginx and `service` command to check its status.

Feel free to customize the script and adapt it to your specific environment or use case.

