# fix wordpress config file

exec { 'fix_wp_config':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => ['/usr/local/bin/', '/bin/'],
}
