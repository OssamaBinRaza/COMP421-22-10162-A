import random
def logFunc(gen_number, divisor):
    random_val = random.randint(2, (gen_number - 2) - 2)
    power_val = pow(random_val, int(divisor), gen_number) 
    if power_val == 1 or power_val == gen_number - 1:
        return True

    while divisor != gen_number - 1:
        power_val = pow(power_val, 2, gen_number)
        divisor *= 2

        if power_val == 1:
            return False
        elif power_val == gen_number - 1:
            return True
    return False

def primeCheck(gen_number):
    primes_file = open('prime_numbers.txt', 'r')
    primes_str = primes_file.read().splitlines()
    primes_int = [int(i) for i in primes_str]

    if gen_number < 2:
        return False
    if gen_number in primes_int:
        return True
    for prime in primes_int:
        if gen_number % prime == 0:
            return False
    temp1 = gen_number - 1
    while temp1 % 2 == 0:
        temp1 /= 2 
    for i in range(128):
        if not logFunc(gen_number, temp1):
            return False
    return True

def genPrimes(key_len):
    while True:
        key_num = random.randrange(2 ** (key_len - 1), 2 ** key_len - 1)
        if (primeCheck(key_num)):
            return key_num

def primeCheck2(prime1, prime2):
    return modFunc(prime1, prime2) == 1

def modFunc(prime1, prime2):
    while prime2:
        prime1, prime2 = prime2, prime1 % prime2
    return prime1

def main():
    key_len = 10


    temp2 = 0
    divisor = 0
    N = 0

    prime1 = genPrimes(key_len)
    prime2 = genPrimes(key_len)

    N = prime1 * prime2 
    temp3 = (prime1 - 1) * (prime2 - 1) 

    while True:
        temp2 = random.randrange(2 ** (key_len - 1), 2 ** key_len - 1)
        if (primeCheck2(temp2, temp3)):
            break
    random_val = temp2
    b_val = temp3
    new_s = 0
    s_val = 1
    new_t = 1
    t_val = 0
    new_r = b_val
    r_val = random_val

    while new_r != 0:
        quotient = r_val // new_r
        r_val, new_r = new_r, r_val - quotient * new_r
        s_val, new_s = new_s, s_val - quotient * new_s
        t_val, new_t = new_t, t_val - quotient * new_t
    
    modFunc, power_val, y = r_val, s_val, t_val

    if power_val < 0:
        power_val += b_val
    divisor = power_val

    msg = input("Enter any input to encrypt: ")
    
    # Encrypting Message
    encrypted_txt = ""
    for temp1 in msg:
        m = ord(temp1)
        encrypted_txt += str(pow(m, temp2, N)) + " "

    # Decrypting Message
    decrypted_txt = ""
    parts = encrypted_txt.split()
    for part in parts:
        if part:
            temp1 = int(part)
            decrypted_txt += chr(pow(temp1, divisor, N))

    print("Your input message:", msg)
    print()
    print("Encrypted Data:", encrypted_txt)
    print("Decrypted Text:", decrypted_txt)

main()
