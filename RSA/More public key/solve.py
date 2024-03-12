from Crypto.Util.number import *
from Crypto import Random
import Crypto.Util.number
import re
from binascii import unhexlify
import libnum
import sys

def is_hex(s): 
    if (s.startswith("0x")): return(True)
    else: return(False)
def hex_to_long(c):
    c=unhexlify(c.replace("0x",""))
    return(bytes_to_long(c))
    
def attack(c1, c2, e1, e2, N):    
    if libnum.gcd(e1, e2) != 1:
        print ("Exponents e1 and e2 cannot be coprime")
        sys.exit(0)
    x,y,_=libnum.xgcd(e1,e2)
    val = (pow(c1,x,N) * pow(c2,y,N)) % N
    return (val)


n = 19654774472335850429240954210004569637126970177465189327608530669740298019540424708045813438277185971702712657381586032044929392696229206921203305494729555195622222922626346931171799503526212048603029758022670691410979393909529256139167908525210956106664077878607866858146208047085152181254674688046414400151173331625835576511827619592572144402998602220852063845022305731383706005470731146230435548020364211733212100727953337032368963390857144244205841719260252078412762721255863011659687112608465214870691525656783824871275319712749158617842718707588695784680351406407900996775950836524058352985176661331291066585077
e1 = 8501826870733
e2 = 5640153282749
c1 = 11129419808202552232019237097046017064405093013478164625343874810302201472875886710416318433667060838733667331223546189547321176686622838296265326542994624563842958938051487905021203681753582105832219196432785263262478499381313915102596063423254872208958521529409723269843595201959611277966570225742328102517915644488458556231678454498692661466745218693796650699377269129909853124730190461301695201658143060040499632400621838322314248435647182156030111321582707250565954290691092007476064791924433638664913702323038382629518184457473599053582201146645474464748309393708528012196919441914382849925896885938548807597323
c2 = 4244474492772498801505364331870318432215933967225075356158491236496315501122945810421993542277752204870446481332428304112339038080767660474332480800815589820700756086096624221234127838373725952983708837562175240065780315560428606141309231489674117793290954647705615490423821570350080593543540182572323187935376989793573441433725040192218504193253665632406007039993628676604456037730409408880957341487327276885427162791618501022053197157789338985603348329743009851861278653439772124237172083914055859585744691318414689373280204196127735481717929943363210989179274181811515477754859078579932771348612838011586401367869
# len(FLAG) = 35

m = attack(c1, c2,e1, e2, n)
print(long_to_bytes(m))

    