command to send files across local network (unsafe)
=====

### Sender
tar -cz $file | nc -q 10 -l -p $port

### Receiver
nc -w 10 $SENDER_IP $port | tar -xz
