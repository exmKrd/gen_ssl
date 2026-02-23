from copy import error
from OpenSSL import crypto
from datetime import datetime
from colorama import Fore


value = 0

while value == 0:
    try :
        key = crypto.PKey()
        key.generate_key(crypto.TYPE_RSA, 2048)
        print ('-----------------------')
        country=input('Country :')
        state= input('State :')
        Locate = input('Locate :')
        Organisation = input('Organisation : ')
        CN = input('CN :')


        cert = crypto.X509()
        cert.get_subject().C = country
        cert.get_subject().ST = state
        cert.get_subject().L = Locate
        cert.get_subject().O = Organisation
        cert.get_subject().CN = CN
        print(f"Here's the informations of your certificat ")
        print(Fore.GREEN + f" Country :{country}\nState :{state}\nLocate :{Locate}\nOrganisation :{Organisation}\nCommon Name :{CN}")
        valid = input(Fore.WHITE + 'are these values correct ? Y/N :').upper()
        if valid == 'Y':
            print('these informations will appear in the certificat')
            value = 1
        else:
            value = 0
        cert.set_serial_number(1000)
        cert.gmtime_adj_notBefore(0)
        cert.gmtime_adj_notAfter(365 * 24 * 60 * 60)
        cert.set_issuer(cert.get_subject())
        cert.set_pubkey(key)

        
        cert.sign(key, 'sha256')


        with open(f"{CN}.key", "wb") as f:
            f.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, key))
        with open(f"{CN}.pem", "wb") as f:
            f.write(crypto.dump_certificate(crypto.FILETYPE_PEM, cert))
        
    except error as e :
        print(Fore.RED + e)    
