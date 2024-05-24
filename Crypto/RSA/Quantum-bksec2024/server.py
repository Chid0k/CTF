from Crypto.Util.number import *
import subprocess
import math

FLAG = open('flag.txt','rb').read()

def challenge():

    p = getPrime(512)
    q = getPrime(512)
    n = p*q
    phi = (p-1)*(q-1)
    e = 65537
    m = bytes_to_long(FLAG)
    c = pow(m, e, n)
    print(f'Welcome to my server. Please help me decrypt the secret.\nHere is the public key: {(hex(n), hex(e))}')
    while(True):
        try: 
            print('> 1. Get encrypted secret')
            print('> 2. Use quantum oracle (experimental)\n')
            option = int(input('Enter your options: '))
            
            if(option == 1):
                print(f'Here is the secret (again): {hex(c)}')
            if(option == 2):
                print('WARNING: Server may crash after this.')
                guess = int(input('Make a guess, must be a square number:'))
                if(math.isqrt(guess)**2 != guess):
                    print('Not a square number!')
                    break
                res = subprocess.run(['./quantum-oracle', str(guess), str(phi), str(n)], capture_output=True, text=True)
                print(res.stdout)
                raise ConnectionAbortedError()
        except:
            print('Server crashed :(')
            break



challenge()
