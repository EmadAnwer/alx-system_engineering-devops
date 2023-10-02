#configure servers

exec { 'install_nginx':
command  => 'apt -y update; apt -y install nginx',
provider => 'shell'
}

file { '/var/www/html/index.html':
ensure  => 'present',
content => 'Hello World!',
require => Exec['install_nginx'],
}

file { '/var/www/html/404.html':
ensure  => 'present',
content => "Ceci n'est pas une page",
require => Exec['install_nginx'],
}



file_line { 'add header':
path  => '/etc/nginx/sites-enabled/default',
match => 'server_name _;$',
line  => "\tserver_name _;\n\tadd_header X-Served-By ${hostname};",
}

exec { 'run':
command  => 'sudo service nginx restart',
provider => shell,
}
