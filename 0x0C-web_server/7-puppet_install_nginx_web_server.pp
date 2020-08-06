# Install Nginx web server (w/ Puppet)
package { 'Install Nginx with Puppet':
  ensure => 'installed',
  require   => Package['apache2.2-common'],
  }

file { 'Nginx':
  mode => '0777',
  echo 'Holberton School' > /var/www/html/index.nginx-debian.html,
  }

file_line { 'redirection':
  ensure => 'present',
  line   => 'sudo sed -i "/listen 80 default_server/a rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default',
  }
