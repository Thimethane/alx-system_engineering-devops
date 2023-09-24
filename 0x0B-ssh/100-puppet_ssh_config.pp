# Content of 100-puppet_ssh_config.pp

# Ensure SSH client is configured to use the private key and refuse password authentication
exec { 'echo':
  path    => 'usr/bin:/bin',
  command => 'echo "    IdentityFile ~/.ssh/holberton\n    PasswordAuthentication no" >> /etc/ssh/ssh_config',
  returns => [0,1],
}