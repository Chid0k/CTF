buffer = "a" * 64
modified = "\x0a\x0d\x0a\x0d"       # Litte endian

print(buffer + modified)