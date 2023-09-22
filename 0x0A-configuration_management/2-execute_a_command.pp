# kill prosses using exec
exec{'run a command':
        command => 'killall -9 killmenow',
        path    => ['/usr/bin','/usr/sbin','/bin'],
}
