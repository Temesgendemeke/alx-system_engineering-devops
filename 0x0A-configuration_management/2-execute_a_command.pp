# kills a process named killmenow

exec {'process kill killmenow':
command => '/usr/bin/pkill -f killmenow'
}
