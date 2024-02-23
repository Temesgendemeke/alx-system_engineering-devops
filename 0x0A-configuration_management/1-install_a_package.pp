# installing flask through puppet

exec { 'flask':
 command => '/usr/bin/apt install python3-flask -v 2.1.0'
}
