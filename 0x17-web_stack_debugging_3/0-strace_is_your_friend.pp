# Fixes 500 error from wordpress config file
file { '/var/www/html/wp-includes/class-up-locale.phpp':
ensure => present,
source => '/var/www/html/wp-includes/class-wp-locale.php',
}
