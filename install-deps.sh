#!/bin/sh

# Install deps for ordersage
sudo apt update
sudo apt upgrade -y
sudo apt install -y python3-paramiko python3-pandas python3-numpy python3-scp

sudo apt install -y xmlstarlet

# find the name name of the worker node
geni-get portalmanifest | xmlstarlet sel -N x="http://www.geni.net/resources/rspec/3" -t -v "//x:node[@client_id='worker']/@component_id" | cut -d + -f 4 > /tmp/worker-node

# configure ordersage user if necessary
if ! passwd -S -q ordersage; then
    sudo useradd -m -u 13579 -d /home/ordersage ordersage
    sudo mkdir /home/ordersage/.ssh
    sudo sh -c 'geni-get key > /home/ordersage/.ssh/id_rsa'
    sudo chmod 600 /home/ordersage/.ssh/id_rsa
    sudo cp /home/ordersage/.ssh/id_rsa /local/repository/
    sudo chmod 644 /local/repository/id_rsa
    sudo sh -c 'ssh-keygen -e -f /home/ordersage/.ssh/id_rsa > /home/ordersage/.ssh/id_rsa.pub'
    sudo sh -c 'ssh-keygen -i -f /home/ordersage/.ssh/id_rsa.pub > /home/ordersage/.ssh/authorized_keys'
    sudo chown -R ordersage:ordersage /home/ordersage/.ssh
    echo ordersage:$(uuidgen) | sudo chpasswd
fi
