#!/bin/bash

qemu-system-x86-64 \
    -enable-kvm \
    -cdrom /path/to/iso \
    -m 1024 \
#      ^^^^
#      1024 bytes of memory 
    -net nic \
#        ^^^
#        enable network card in guest
    -net user 
#        ^^^^
#        set up virtual subnet with a dhcpcd server
