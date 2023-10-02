# add custom header to the request

file_line{
  'add custom header to the request':
    path  => '/etc/nginx/sites-available/default',
    line  =>  "add_header X-Served-By ${hostname};",
    match => '^server_name',
    after => 'server_name',
    notify => Service['nginx'],
}
