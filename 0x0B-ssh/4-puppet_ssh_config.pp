# set up your client SSH configuration file so that you can connect
# to a server without typing a password.
# * Your SSH client configuration must be configured to use the
# private key ~/.ssh/holberton
# * Your SSH client configuration must be configured to refuse
# to authenticate using a password
file_line { 'puppet_configuration':
  ensure => 'present',
  path   => '~/.ssh/config',
  line   =>  'IdentityFile ~/.ssh/holberton',
  }

file_line { 'puppet_configuration':
  ensure => 'present',
  path   => '~/.ssh/config',
  line   => 'PasswordAuthentication no',
  }
