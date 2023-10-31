def power_mod(base, exponent, modulus):
    if exponent == 0:
        return 1
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent // 2
        base = (base * base) % modulus
    return result

def fermat_little_theorem(a, p):
    if not is_prime(p):
        raise ValueError("p must be a prime number")
    return power_mod(a, p - 1, p)

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Get user input for a and p
a = int(input("Enter the value of 'a': "))
p = int(input("Enter the prime number 'p': "))

# Check if p is prime
if not is_prime(p):
    print("Error: p must be a prime number")
else:
    result = fermat_little_theorem(a, p)
    print(f"{a}^({p}-1) ≡ {result} (mod {p})")
