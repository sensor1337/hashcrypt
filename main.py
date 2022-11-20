from sensorHashcrypt import hashing
import sys
import rsa


# defs
def asym_dec(msg_cr, prkey):
    msg_dec = rsa.decrypt(msg_cr, prkey)
    print("Decrypted message:", msg_dec.decode('utf8'))


def asym_enc():
    (pubkey, prkey) = rsa.newkeys(512)  # Keys generation
    print("Your public key:", pubkey,
          "\nYour private key (don't say it to any1 except your interlocutor):", prkey)
    msg = input("Enter message to encrypt:").encode('utf8')
    msg_cr = rsa.encrypt(msg, pubkey)
    print("Your encrypted message:", msg_cr)

    if input("Do you want to decrypt your message? (y/n):") == 'y' or 'Y':
        asym_dec(msg_cr, prkey)
    else:
        sys.exit(0)


def encrypt():
    msg = input("Enter message to encrypt:")
    alg = int(input("""
    Choose algorythm to hash:
    [1] - md5
    [2] - sha256
    [3] - sha512
    [4] - sha-1
    """))

    # input analysis

    if alg == 1:
        hashing.md5(msg)

    elif alg == 2:
        hashing.sha256(msg)

    elif alg == 3:
        hashing.sha512(msg)

    elif alg == 4:
        hashing.sha_1(msg)

    else:
        print("Incorrect input value.")
        sys.exit(0)


# user communication

mode = int(input("""
    Welcome to HashCrypt! Choose working mode:
    [1] - Hash encryption
    [2] - Asymmetric message encryption
    [3] - Asymmetric message decryption
    """))
if mode == 1:
    encrypt()
elif mode == 2:
    asym_enc()
elif mode == 3:
    msg_cr = input("Enter encrypted message:")
    prkey = input("Enter your private key:")
    asym_dec(msg_cr, prkey)

else:
    print("Invalid mode number")
    sys.exit(1)

# bye

print("Thank you for using Hashcrypt! New functions are going tba soon.\n<3 by https://github.com/sensor1337 <3")
