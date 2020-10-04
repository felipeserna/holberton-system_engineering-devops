# Postmortem   
## Issue Summary   
On August 15, 2020, from 1:00 PM to 2:00 PM PT, around 60% of Amazon Web Services world users could not access to its web server, so they lose a lot of money because their businesses relied on that company. Amazon has many data centers all over the world, and the businesses that were affected were those hosted in a server located in North Virginia, USA. The root cause was that the NGINX web server was not listening on port 80 due to some experiments with port 8080.   
## Timeline   
- At 1:00 PM: A user from Japan tried to access his business web page and he received a 404 error.
- At 1:03 PM: The same user alerted Amazon Web Services of that issue because they did not have a monitoring tool.
- At 1:05 PM: The IT supervisor typed `curl 0:80` and received an error message.
- At 1:20 PM: The IT supervisor typed `service nginx status` and realized that NGINX was not running.
- At 1:30 PM: The IT supervisor found that the server was listening on port 8080.
- At 1:50 PM: The IT supervisor wrote a Bash script to fix the issue by letting the NGINX server for listening on port 80.
- At 2:00 PM: The server was restarted.  
## Root cause and resolution   
The remote server at North Virginia, USA, was listening on port 8080 due to some changes that an engineer did. The IT supervisor used his debugging skills learned when he studied Computer Science and remembered that the default port should be 80 so that a web client can connect to the remote server. He knew that the default file has many lines in which the port must be specified, so he wrote a Bash script for changing all lines of 8080 to 80 by simply typing:  
`sed -i 's/8080/80/g' /etc/nginx/sites-enabled/default`  
Then he restarted the NGINX server writing:  
`service nginx restart`  
Then he typed `service nginx status` and got this message: `nginx is running`   
Finally he typed `curl 0:80` on his terminal and received a message saying that the NGINX web server was successfully installed.   
## Corrective and preventative measures   
Be sure to use a monitoring tool such as Datadog to constantly measure vital signs of your servers. Be sure that your servers are listening on the correct port so that all web clients can connect to them. Every time you make changes to your servers be sure to make some tests such as `curl 0:80` and `service nginx status`. You do not want to have angry users or customers.
