Configuration Management Project

This repository contains Puppet manifests and related files for configuring and managing various aspects of a system. The Puppet manifests are designed to meet specific requirements, install packages, and execute commands.

Puppet Manifests

1. Install a Package (1-install_a_package.pp)
This Puppet manifest installs Flask version 2.1.0 using pip3.

Usage:

bash
Copy code
sudo puppet apply 1-install_a_package.pp
2. Execute a Command (2-execute_a_command.pp)
This Puppet manifest kills a process named "killmenow" using the pkill command.

Usage:

bash
Copy code
sudo puppet apply 2-execute_a_command.pp
Requirements
Ensure you have the following requirements met to successfully use the provided Puppet manifests:

Puppet installed on the target system.

How to Use

Clone this repository to your local machine.
Navigate to the project directory.
Choose the desired Puppet manifest and apply it using the puppet apply command as shown in the individual manifest descriptions.
Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or create a pull request.