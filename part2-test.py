# Part 2 test of the Python Review lab.

import part2

## Test 1. Tests the encode with 2 primes in range
print("Test 1")
if(part2.encode(643,5) == 643*5):
	print("PASSED")
else:
	print("FAILED - should print 3215 for inputs of 643 and 5")
  
## Test 2. Tests the encode with 2 primes, where x is out of range
print("Test 2")
if(part2.encode(3,5) == None):
	print("PASSED")
else:
	print("FAILED - should return None since x of 3 is not in range")
  
 ## Test 3. Tests the encode with 2 non-primes
print("Test 3")
if(part2.encode(501,6) == 3521):
	print("PASSED")
else:
	print("FAILED - should return 3521. Since x of 501 is not prime, should increment to 503, and y of 6 should go to 7")

## Test 4. Tests the decode with product of 2 primes
print("Test 3")
if(part2.decode(66839) in [(751,89),(89,751)]):
	print("PASSED")
else:
	print("FAILED - for the input of 66839, decode should return (751,89) in some order")
 

##Write more test cases here
