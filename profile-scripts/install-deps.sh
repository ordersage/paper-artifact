#!/bin/sh

# Install deps for ordersage
sudo apt update
sudo apt upgrade -y
sudo apt install -y python3-paramiko python3-pandas python3-numpy python3-scp

sudo apt install -y xmlstarlet

# find the name name of the worker node
geni-get portalmanifest | xmlstarlet sel -N x="http://www.geni.net/resources/rspec/3" -t -v "//x:node[@client_id='worker']/@component_id" | cut -d + -f 4 > /tmp/worker-node
