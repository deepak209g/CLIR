import cosine
def main():
	print('1. Choose 1 to to translate the sentence.\n2. Choose 2 to compute the cosine similarity')
	n = input()
	if (n == '1'):
		print('Enter the sentence')
		main_str = input()
		trans_str = ""
		print('Enter the correct translated sentence')
		correct_str = input()
		cosine.cosine_driver(trans_str, correct_str)
	else:
		print("Enter Document IDs")
		fname1 = input()
		fname2 = input()
		cosine.cosine_driver(fname1, fname2)
main()