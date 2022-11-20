from sensorHashcrypt import hashing


# user-communication


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

# bye

print("Thank you for using Hashcrypt! New functions are going tba soon.\n<3 by https://github.com/sensor1337 <3")



