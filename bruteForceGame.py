# -*- coding: utf-8 -*-
from itertools import product
import string, sys, time, os



def notification(title, message):
	# send notification for macos
    os.system("""
    			 osascript -e 'display notification "{}" with title "{}"'
    		  """.format(message, title))

def printProgressBar (current, total, length=100, prefix="", suffix="", filler="#", space=" ", oncomp="Done!", border="[]"):
    if len(border) != 2:
        print("parameter 'border' must include exactly 2 symbols!")
        return None

    print(prefix + border[0] + (filler * int(current / total * length) +
                                      (space * (length - int(current / total * length)))) + border[1], suffix, "\r", end="")
    if total == current:
        if oncomp:
            print(prefix + border[0] + space * int(((length - len(oncomp)) / 2)) +
                  oncomp + space * int(((length - len(oncomp)) / 2)) + border[1], suffix)
        if not oncomp:
            print(prefix + border[0] + (filler * int(current / total * length) +
                                        (space * (length - int(current / total * length)))) + border[1], suffix)

if (len(sys.argv) == 2 or len(sys.argv) == 3):
	chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
	startTime = time.time()

	finalPsw = sys.argv[1]
	maxLength = len(finalPsw)
	maxVariations = len(chars)**len(finalPsw)

	print("Max variations: " + str(maxVariations))

	count = 0

	for length in range(maxLength+1):
		to_attempt = product(chars, repeat=length)
		for attempt in to_attempt:
			password = ''.join(attempt)
			
			if (password == finalPsw):
				endTime = time.time() - startTime
				notification("Found your password!", "Your password is '" + password +  "' (" + str(round(endTime, 4)) + " seconds)")
				print("\n------------")
				print("Found your password after " + str(count) +  " trys (" + str(round(endTime, 4)) + " seconds)")
				print("\nYour password is: " + password)
				print("------------")
				break
			else:
				if ("-v" in sys.argv):
					printProgressBar(count, maxVariations, 100, "", "Trying " + password)
				else:
					pass
				count += 1
	print("\nThis has been executed " + str(count) + " times.")
else:
	print("Usage: " + sys.argv[0] + " <passwordToCheck> <option>")
	print("Available options: \n 	-v: Verbose")

