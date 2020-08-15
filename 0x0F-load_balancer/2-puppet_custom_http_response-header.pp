# Create a custom HTTP header response
# * name must be X-Served-By
# * value must be the hostname of the server Nginx is running on
exec { 'apt-get update':
  command => '/usr/bin/apt-get update'
  }

package { 'nginx':
  ensure => 'installed'
  }

exec { 'command_1':
  command =>  "sudo chmod '0777' /var/www/html/index.nginx-debian.html",
  }

exec { 'command_2':
  command => 'sudo sed -i \'/listen 80 default_server/a "add_header X-Served-By \$HOSTNAME;" /etc/nginx/sites-available/default;',
  }

exec { 'command_3':
  command => 'sudo service nginx restart',
  }
