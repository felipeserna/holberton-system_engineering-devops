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

exec { 'command_3':
  command => "sudo sed -i '/listen 80 default_server/a add_header X-Served-By ${hostname};' /etc/nginx/sites-available/default2";

exec { 'command_4':
  'sudo service nginx restart',
  }
