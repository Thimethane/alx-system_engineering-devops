# Puppet Manifest to create a file in /tmp
# Ensure the directory exists
file { '/tmp':
    ensure => 'directory',
}
# Create the file with specified content, permissions, owner, and group
file { '/tmp/school':
    ensure  => 'file',
    content => 'I love Puppet',
    mode    => '0744',
    owner   => 'www-data',
    group   => 'www-data',
}