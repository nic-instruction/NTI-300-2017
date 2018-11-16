#!/bin/bash
echo "yaaaaah hoooooooooooo"

yum -y install httpd mod_ssl
systemctl enable httpd
systemctl start httpd
