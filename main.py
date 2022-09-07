from math import sqrt, pow

array_reach = 100000
isPrime = [True for i in range(array_reach + 1)]

# Applying Sieve of Eratosthenes
# This function starts with the smallest numbers and
# Disqualifies the every multiple of the number
# Which gives us the Prime Numbers list
def sieve():
    isPrime[0] = isPrime[1] = False

    for i in range(2, int(sqrt(array_reach)) + 1):
        if isPrime[i]:
            for j in range(i * i, array_reach, i):
                isPrime[j] = False


def findPrimes(digits, starts_with):

    # Range: if 3 then between 99-999
    left = int(pow(10, digits - 1))
    right = int(pow(10, digits) - 1)

    # For every number in range
    for i in range(left, right + 1, 1):

        # Check if requirements met
        if isPrime[i] and str(i)[0] == str(starts_with):
            print(i, end=" ")


if __name__ == "__main__":

    sieve()  # Generate Prime Numbers list
    digits = 3
    starts_with = 5
    findPrimes(digits, starts_with)
