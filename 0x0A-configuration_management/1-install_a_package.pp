# Puppet Manifest to install Flask version 2.1.0 using pip3

# Ensure pip3 is installed
package { 'python3-pip':
  ensure => installed,
}

# Install Flask version 2.1.0 using pip3
exec { 'install_flask':
  command => '/usr/bin/pip3 install flask==2.1.0',  # Adjust the path based on your system
  path    => '/usr/local/bin',
  creates => '/usr/local/lib/python3.8/dist-packages/flask/__init__.py',  # Adjust the path based on your Python version and installation
}

# Display Flask version after installation
exec { 'display_flask_version':
  command   => '/usr/local/bin/flask --version',  # Adjust the path based on your system
  path      => '/usr/local/bin',
  logoutput => true,
  require   => Exec['install_flask'],
}
