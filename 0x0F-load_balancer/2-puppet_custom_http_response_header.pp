# configure an Nginx

package{ 'nginx':
  ensure => 'installed',
}

service{ 'nginx':
  ensure => 'running',
  enable => 'true',
}
file_line{'custom HTTP header':
  path => '/etc/nginx/sites-available/default',
  line => "        add_header X-Served-By ${hostname};",
  after   => 'server_name _;', 
  match   => '^server_name _;',
  notify  => Service['nginx'],
    require => Package['nginx'],
}
