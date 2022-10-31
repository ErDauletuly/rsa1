
sharedPrime = int(input("input P: "))   # p
sharedBase = int(input("input G: "))  # g

aliceSecret = int(input("input a: "))  # a
bobSecret = int(input("input b: "))  # b

A = (sharedBase ** aliceSecret) % sharedPrime
print("\n  A - ", A)

B = (sharedBase ** bobSecret) % sharedPrime
print("  B - ", B)

print("Calculated :")

aliceSharedSecret = (B ** aliceSecret) % sharedPrime
print(" Alice Secret: ", aliceSharedSecret)

bobSharedSecret = (A ** bobSecret) % sharedPrime
print("   BOB"
      " Secret: ", bobSharedSecret)