from itertools import product
import string
import sys
import time
import os
def notification(title, message):
	# send notification for macos
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(message, title))

if (len(sys.argv) == 2 or len(sys.argv) == 3):
	chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
	startTime = time.time()

	finalPsw = sys.argv[1]
	maxLength = len(finalPsw) + 2
	print("Max variations: " + str(len(chars)**maxLength))
	count = 0
	for i in range(0, maxLength):
		for length in range(0, i):
			to_attempt = product(chars, repeat=length)
			for attempt in to_attempt:
				password = ''.join(attempt)
				if (password == finalPsw):
					endTime = time.time() - startTime
					notification("Found your password!", "Your password is " + password)
					print("------------")
					print("Found your password after " + str(count) +  " trys (" + str(round(endTime, 4)) + " seconds)")
					print("\nYour password is: " + password)
					print("------------")
					break
				else:
					if ("-v" in sys.argv):
						print("Try " +  str(count) + " --> " + str(password))
				count += 1
	print("\nThis has been executed " + str(count) + " times.")
else:
	print("Usage: " + sys.argv[0] + " <passwordToCheck> <option>")
	print("Available options: \n 	-v: Verbose")

