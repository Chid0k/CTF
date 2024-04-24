# for i in range(ord('A'), ord('Z')+1):
#       print(f'{chr(i)}\n',end = '')
a = "ZGSOCXPQUYHMILERVTBWNAFJDK"
b = "IWCYNM?D?TLG?BSEKFPVUH?ARO"
f = {'' : ''}
for i in range(0,len(a)):
      f[a[i]] = b[i]

s = """SYTe (eakdy tkd sjbyndr yar thjm) jdr j yobr kt skxbnyrd ersndzyo skxbryzyzkc. 
Skcyreyjcye jdr bdrercyrq gzya j ery kt sajhhrcmre gazsa yrey yarzd sdrjyzwzyo, 
yrsaczsjh (jcq mkkmhzcm) evzhhe, jcq bdklhrx-ekhwzcm jlzhzyo. 
Sajhhrcmre nenjhho skwrd j cnxlrd kt sjyrmkdzre, 
jcq garc ekhwrq, rjsa ozrhqe j eydzcm (sjhhrq j thjm) gazsa ze enlxzyyrq yk jc kchzcr eskdzcm erdwzsr. 
SYTe jdr j mdrjy gjo yk hrjdc j gzqr jddjo kt skxbnyrd ersndzyo evzhhe zc j ejtr, 
hrmjh rcwzdkcxrcy, 
jcq jdr akeyrq jcq bhjorq lo xjco ersndzyo mdknbe jdkncq yar gkdhq tkd tnc jcq bdjsyzsr. 
Tkd yaze bdklhrx, yar thjm ze: bzskSYT{TD3UN3CSO_4774SV5_4D3_S001_7JJ384LS}"""
s = s.upper()

for i in range(0,len(s)):
      if ord(s[i]) in range(65, ord('Z') + 1):
            print(f[s[i]],end ='')
      else:
            print(s[i], end ='')
