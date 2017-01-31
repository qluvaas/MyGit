import sys

def main():
	print "Input String: " + sys.argv[1]
	enc = []
	dec = []
	for i in range(0, len(sys.argv[1])):
		enc.append(str(ord(sys.argv[1][i]) + 32))
	print "Encrypted:"
	print "".join(map(str, enc))
	for i in range(0, len(sys.argv[1])):
		dec.append(chr(int(enc[i]) - 32))
	print "Decrypted:"
	print "".join(map(str, dec))
	pass
	
if __name__ == '__main__':
	sys.exit(main())
