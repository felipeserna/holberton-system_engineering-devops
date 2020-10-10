# Increase the limit of requests
exec { 'limit':
  command => "sed -i 's/15/2000/g' /etc/default/nginx; service nginx restart",
  path    =>['/bin', '/usr/bin', '/usr/sbin']
  }
