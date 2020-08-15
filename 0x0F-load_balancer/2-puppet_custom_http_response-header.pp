# Create a custom HTTP header response
# * name must be X-Served-By
# * value must be the hostname of the server Nginx is running on
exec { 'apt-get update':
  command => '/usr/bin/apt-get update',
  }

package { 'nginx':
  ensure => 'installed',
  }

file_line { 'command_1':
  path  => '/etc/nginx/sites-available/default',
  line  => "add_header X-Served-By \$HOSTNAME;"
  after => '/listen 80 default_server/a'
  }

exec { 'command_2':
  command => 'sudo service nginx restart',
  }
