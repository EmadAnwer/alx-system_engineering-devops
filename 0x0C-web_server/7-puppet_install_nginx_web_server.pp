# configure an Nginx

package{ 'nginx':
  ensure => 'installed',
}

service{ 'nginx':
  ensure => 'running',
  enable => 'true',
}

file{'/etc/nginx/sites-available/default':
  ensure => 'file',
  content => 'server {
    listen 80 default_server;
    listen [::]:80 default_server ipv6only=on;

    root /var/www/html;
    index index.html index.htm;

    server_name localhost;
    error_page 404 /404.html;
    location / {
        try_files $uri $uri/ =404;
    }

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }
}',
  require => Package['nginx'],
  notify => Service['nginx'],
  replace => 'true',
}

file {'/var/www/html/index.html':
  ensure => 'file',
  content => 'Hello World!',
  require => Package['nginx'],
  notify => Service['nginx'],
  }

file {'/var/www/html/404.html':
  ensure => 'file',
  content => "Ceci n'est pas une page",
  require => Package['nginx'],
  notify => Service['nginx'],}
