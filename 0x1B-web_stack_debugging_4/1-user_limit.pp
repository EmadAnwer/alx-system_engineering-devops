# chanhe hard and soft limits for holberton user

exec { 'holberton hard limit':
    command => '/bin/sed -i "s/5/4096/g" /etc/security/limits.conf',
}

exec { 'holberton soft limi':
    command => '/bin/sed -i "s/4/4096/g" /etc/security/limits.conf',
}

