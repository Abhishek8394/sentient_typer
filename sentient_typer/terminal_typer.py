from __future__ import print_function
from time import sleep

def sentient_type(text, pace=0.07, end="\n"):
	for c in text:
		print(c, sep="", end="", flush=True)
		sleep(pace)
	print(end=end)

if __name__ == "__main__":
	sentient_type("Lorem Ipsum dolor\n. I mean hello. We are sentient now.")