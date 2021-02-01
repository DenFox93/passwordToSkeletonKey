from sys import argv

password=argv[1]
print("The password inserted is --> " + str(password))
import hashlib,binascii
hash = hashlib.new('md4', password.encode('utf-16le')).digest()
nt= binascii.hexlify(hash)
print("The NTLM calculated is --> " + str(nt))

kiwikey=[]
splits=[nt[i:i+8] for i in range(0, len(nt), 8)]
for j in splits: 
	reverse="".join(reversed([j[i:i+2] for i in range(0, len(j), 2)]));
	kiwikey.append("0x"+reverse)

kiwikey2=str(kiwikey)
kiwikey=kiwikey2.replace("'", "")
kiwikey2=kiwikey.replace("[", "{")
kiwikey= kiwikey2.replace("]", "}")
print("The kiwikey calculated is --> " + str(kiwikey))
