#!/usr/bin/env bash

# File: nginx_config.pp

# Install Nginx package
package { 'nginx':
  ensure => 'installed',
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure => 'running',
  enable => true,
}

# Configure Nginx default site to listen on port 80
file { '/etc/nginx/sites-available/default':
  ensure  => 'file',
  content => "
    server {
        listen 80 default_server;
        listen [::]:80 default_server;

        server_name _;

        location / {
            echo 'Hello World!';
        }

        location /redirect_me {
            return 301 https://github.com/Thimethane;
        }
    }
  ",
  notify  => Service['nginx'],
}
