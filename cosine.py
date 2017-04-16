import math
import codecs
def fillDict(str, dict):
	# f = open(str, "r")
	for line in str:
		for word in line.split():
			# print (word)
			if word not in dict:
				dict[word]=1;
			else:
				dict[word]+=1;

def normalise(dict):
	sq_value = 0

	for key in dict.keys():
		dict[key] = 1 + math.log10(dict[key])
		sq_value += dict[key] * dict[key]

	sq_value = math.sqrt(sq_value)
	# print (sq_value)

	for key in dict.keys():
		dict[key] = dict[key]/sq_value
	
def computeCosine(dict1, dict2):
	cosine = 0.0
	if len(dict1) > len(dict2):
		for key in dict2.keys():
			if key not in dict1:
				continue
			else:
				cosine += dict1[key] * dict2[key]
	else:
		for key in dict1.keys():
			if key not in dict2:
				continue
			else:
				cosine += dict1[key] * dict2[key]
	print ("Cosine Similarity: ", cosine)

def calculateJaccard(dict1, dict2):
	num=0.0
	den=0.0
	ans=0.0
	for key in dict1.keys():
		den += dict1[key]
	for key in dict2.keys():
		den += dict2[key]
	if len(dict1) > len(dict2):
		for key in dict2.keys():
			if key not in dict1:
				continue
			else:
				num += min(dict1[key], dict2[key])
	else:
		for key in dict1.keys():
			if key not in dict2:
				continue
			else:
				num += min(dict1[key], dict2[key])
	# print (num, den)
	ans = num/(den-num)
	print ("Jaccard Coefficient: ", ans)

def cosine_driver(fname1, fname2):
	dict1 = {}
	dict2 = {}
	# fname1 = "test.txt"
	# fname2 = "test2.txt"
	str1 = fname1.split('.')[-1]
	if str1 == 'txt':
		f1 = codecs.open(fname1, "r", encoding="utf8")
		f2 = codecs.open(fname2, "r", encoding="utf8")
		
	else:
		f1 = [fname1]
		f2 = [fname2]

	fillDict(f1, dict1)
	fillDict(f2, dict2)
	# dict1 = {'affection':115, 'jealous':10, 'gossip':2}
	# dict2 = {'affection':20, 'jealous':11, 'gossip':6, 'wuthering':38}
	calculateJaccard(dict1, dict2)
	normalise(dict1)
	normalise(dict2)	
	# print (dict1)
	# print (dict2)
	computeCosine(dict1, dict2)
	

