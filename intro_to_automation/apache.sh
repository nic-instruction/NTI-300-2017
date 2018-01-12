#!/bin/bash
yum -y install httpd mod_ssl                                              # This installs apache with encryption
systemctl enable httpd                                                    # This enables the apache service
systemctl start httpd                                                     # This starts the apache server


sudo sed -i 's/^/#/g' /etc/httpd/conf.d/welcome.conf                                          # Commenting out welcome.conf

sudo echo -e "<html> \n<h1> Welcome, NTI-300 </h1> \n</html>" > /var/www/html/index.html      # Creating our index.html
