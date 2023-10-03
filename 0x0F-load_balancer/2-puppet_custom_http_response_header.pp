# Puppet manifest to configure custom HTTP response header

# Install Nginx package
package { 'nginx':
  ensure => 'installed',
}

# Configure Nginx with the custom HTTP response header
file { '/etc/nginx/sites-available/custom_header':
  ensure  => 'file',
  content => "server {
                listen 80 default_server;
                listen [::]:80 default_server;

                server_name _;

                location / {
                    return 200 '\$host is being served by: \$hostname\n';
                }

                add_header X-Served-By \$hostname;
            }",
}

# Create a symbolic link to enable the configuration
file { '/etc/nginx/sites-enabled/custom_header':
  ensure => 'link',
  target => '/etc/nginx/sites-available/custom_header',
}

# Remove the default Nginx configuration
file { '/etc/nginx/sites-enabled/default':
  ensure => 'absent',
}

# Test the Nginx configuration
exec { 'nginx_test':
  command => 'nginx -t',
}

# Restart Nginx to apply the changes
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => [File['/etc/nginx/sites-enabled/custom_header'], Exec['nginx_test']],
}
