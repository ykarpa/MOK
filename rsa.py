import random


def is_prime(n):
    """Check if a number is prime"""
    for i in range(2,n):
        if (n % i) == 0:
            return False
    return True


def euler_func(p, q):
    """Count the positive integers (up to p*q) that are relatively prime to p*q"""
    return (p - 1) * (q - 1)


def extended_euclidean_algorithm(a, b):
    """Extended Euclidean algorithm for finding gcd, x, y"""
    if a == 0 :
        return b, 0, 1
    gcd,x1,y1 = extended_euclidean_algorithm(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


def modular_inverse(num, mod):
    return extended_euclidean_algorithm(num, mod)[1] % mod


def generate_keys(bit_length):
    """Generate public and private keys"""
    # Generation of p and q
    half_bit_length = bit_length // 2
    while True:
        p = random.randint(2**(half_bit_length-1), 2**half_bit_length-1)
        if is_prime(p):
            break
    while True:
        q = random.randint(2**(half_bit_length-1), 2**half_bit_length-1)
        if is_prime(q) and p != q:
            break
    # Calculation of the module
    n = p * q
    # Public key creation
    phi = euler_func(p, q)
    while True:
        e = random.randint(3, phi - 1)
        if extended_euclidean_algorithm(e, phi)[0] == 1:
            break
    pub_key = (e, n)
    # Private key creation
    d = modular_inverse(e, phi)
    priv_key = (d, n)
    return pub_key, priv_key


def rsa_encrypt(public_key, plain_text):
    """Encrypt text using input parameters"""
    e, n = public_key
    try:
        encrypted_text = pow(int(plain_text), e, n)
    except ValueError:  # Якщо виняток виникає при спробі конвертації тексту у ціле число
        encrypted_text = [pow(ord(char), e, n) for char in plain_text]
    return encrypted_text


def rsa_decrypt(private_key, encrypted_text):
    """Decrypt text using input parameters"""
    d, n = private_key
    try:
        decrypted_text = str(pow(encrypted_text, d, n))
    except TypeError:  # Якщо виняток виникає при спробі розшифрувати список
        decrypted_text = ''.join([chr(pow(char, d, n)) for char in encrypted_text])
    return decrypted_text


# def rsa_encrypt(public_key, plain_text):
#     """Encrypt text using input parameters"""
#     e, n = public_key
#     return pow(int(plain_text), e, n)


# def rsa_decrypt(private_key, encrypted_text):
#     """Decrypt text using input parameters"""
#     d, n = private_key
#     decrypted_text = str(pow(encrypted_text, d, n))
#     return ''.join(decrypted_text)


keys = generate_keys(12)
key1 = (3, 9173503)
key2 = (6111579, 9173503)
initial_text = "111111"
encrypted_text = rsa_encrypt(key1, initial_text)
decrypted_text = rsa_decrypt(key2, encrypted_text)
print("Ключі - ", keys)
print("Початковий текст - ", initial_text)
print("Зашифрований текст - ", encrypted_text)
print("Розшифрований текст - ", decrypted_text)