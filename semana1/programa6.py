def is_prime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True

is_prime(2)
# True

is_prime(8)
# False

is_prime(9)
# False

is_prime(11)
# True
