import hashlib
from cryptography.fernet import Fernet
import base64
username_trial = "GOUGH"
bUsername_trial = b"GOUGH"

user_key = input("\nEnter your license key: ")
user_key = user_key.strip()

print(user_key)

key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = "xxxxxxxx"
key_part_static2_trial = "}"
key_full_template_trial = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial

print(len(key_full_template_trial))

# len key = 32
# key = picoCTF{1n_7h3_|<3y_of_xxxxxxxx}

a = [4, 5, 3, 6, 2, 7, 1, 8]
key_part_dynamic1_trial = ""
for i in a:
    key_part_dynamic1_trial += hashlib.sha256(bUsername_trial).hexdigest()[i]
print(key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial)