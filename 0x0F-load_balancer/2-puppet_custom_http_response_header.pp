# configure an Nginx

file_line{'custom HTTP header':
  path => '/root/alx/month-0/alx-system_engineering-devops/0x0F-load_balancer/test',
  line => '        add_header X-Served-By \"${::hostname}\";',
  after   => 'server_name _;', 
  match   => '^server_name _;',
  notify  => Service['nginx'],
  }
