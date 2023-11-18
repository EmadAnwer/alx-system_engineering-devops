# Increases the amount of file read

exec { 'fix-nginx':
    command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
}

# Restart nginx

exec { 'nginx':
  command => '/usr/sbin/service nginx restart',
  require => Exec['fix-nginx'],
}
