CUPS attacker to UDP socket
===========================

In this repository it is found a way to take advantage of the UDP socket listening to any message send to port ``631`` which is used by CUPS to find printers.

As well as a way to identify a vulnerable machine and a simple way to block any malicious messages.

Connecting a malicious printer
------------------------------

To start sending UDP messages, ``attack.py`` needs to be executed as:

```
python attack.py <LOCAL_HOST> <TARGET_HOST> <COMMAND>
```

The ``LOCAL_HOST`` is the IP address of the attacker

The ``TARGET_HOST`` would be the victim's local host IP  address

The ``COMMAND`` could be any linux command to be performed in the victim's machine

For example this is how the command would look like:

```
python attack.py 152.138.102.23 143.90.22.223 'echo This machine has been attacked > /tmp/ATTACKED'
```

The port of the printer would always be ``111``. Its location can be found in ``http://localhost:631/printers/Malicious_printer_152_138_102_23``

The print job that the victim starts, the attack will be performed as creating the ``ATTACKED`` file inside ``/tmp/`` with the content ``This machine has been attacked``.


Check if your Linux machine is vulnerable
-----------------------------------------

To check if your current machine is vulnerable, the UDP port ``631`` can be checked if it is listening to any message.
Or run the next command inside the Linux machine presumed to be vulnerable:

```
sudo python3 check_vulnerability.py
```

This script uses ``net-tools`` to check on UDP sockets. This package needs to be installed which it can be done in Ubuntu with:

```
sudo apt install net-tools -y
```

Block UDP listener
------------------

To block every malicious to printer to automatically connect to a linux machine, the UDP port ``631`` needs to be blocked. Run the following script to block it:

```
sudo python3 block_udp.py
```

This script uses Uncomplicated Firewall or ``ufw`` to block any messages. It is installed in any Ubuntu installation but it can be installed with the following command if any problem arises:

```
sudo apt install ufw -y
```
