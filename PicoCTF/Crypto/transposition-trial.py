s = """heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_V6E5926A}4"""

for i in range(0,len(s) - len(s) % 3,3):
      print(s[i + 2], s[i], s[i + 1], sep ='', end ='')
      