import hashlib


# MD5


def md5(msg):
    encrypted = hashlib.md5(msg.encode('utf-8')).hexdigest()
    print("Your MD5-encrypted message:", encrypted)


# SHA256


def sha256(msg):
    encrypted = hashlib.sha256(msg.encode('utf-8')).hexdigest()
    print("Your SHA256-encrypted message:", encrypted)


# SHA512


def sha512(msg):
    encrypted = hashlib.sha512(msg.encode('utf-8')).hexdigest()
    print("Your SHA512-encrypted message:", encrypted)


# SHA-1


def sha_1(msg):
    encrypted = hashlib.sha1(msg.encode('utf-8')).hexdigest()
    print("Your SHA1-encrypted message:", encrypted)
