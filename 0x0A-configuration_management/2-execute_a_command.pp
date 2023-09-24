# Puppet Manifest to kill the process named 'killmenow' using pkill
exec { 'killmenow':
    command     => 'pkill -f killmenow',
    path        => ['/usr/bin', '/usr/sbin', '/bin', '/sbin'],
    onlyif      => 'pgrep -f killmenow',
    refreshonly => true,
}