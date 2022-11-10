# script that takes care of http requests in high volume address to Nginx
exec { 'sed increase ULIMIT number in concerned etc/default/nginx file':
   command => "sed -i 's/15/1024/g' /etc/default/nginx; service nginx restart",
   path => ['/bin', '/usr/bin', '/usr/sbin']
}
