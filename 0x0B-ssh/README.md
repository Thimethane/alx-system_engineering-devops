SSH Configuration with Puppet

This project demonstrates how to configure the SSH client to use a private key and disable password authentication using Puppet.

Puppet Manifest

The main configuration is defined in the init.pp file within the ssh_config_module Puppet module.

Usage
To apply the configuration using Puppet, run the following command from the project directory:

bash
Copy code
sudo puppet apply --modulepath ./ ssh_config_module/manifests/init.pp
This will configure the SSH client to use the specified private key and disable password authentication.

File Structure
ssh_config_module/manifests/init.pp: Puppet manifest defining the SSH client configuration.
README.md: This file, providing an overview of the project.
Feel free to customize and expand this README to include any additional information or details about your project.