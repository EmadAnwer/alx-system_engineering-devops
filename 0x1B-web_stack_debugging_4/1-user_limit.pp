# Increases the amount of file read

exec {"fix-nginx",
	command => 'sed -i "s/15/4096/" /etc/default/nginx ; sudo service nginx restart',
	path    => '/usr/local/bin/:/bin/'
}