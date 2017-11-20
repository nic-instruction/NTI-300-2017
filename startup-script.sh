#!/bin/bash
echo "yaaaaah hoooooooooooo"

yum -y install httpd
systemctl enable httpd
systemctl start httpd
