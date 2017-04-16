import codecs
from corpus import Corpus
from IBM_Model_1 import IbmModel1
import pickle


corpus = Corpus("./corpus/french.txt", "./corpus/english.txt")

has_lines = True
Mapping_Lines = 100
Iterations = 50
j = 0
skip_files = 6579
while has_lines:
    i = 0
    j += 1
    f_name = "./models/model" + str(j) + ".obj"
    ser_file = open(f_name, "ab")
    sentence_pairs = []
    while corpus.has_more() and i < Mapping_Lines:
        if j > skip_files:
            nel = corpus.next_e_line()
            nfl = corpus.next_f_line()
            sentence_pairs.append({"english": nel, "french": nfl})
        i += 1

    if len(sentence_pairs) > 0:
        print("Creating model" + str(j))
        model = IbmModel1(sentence_pairs, Iterations)
        model.train()
        model.print_params()
        t_p = model.generate_refined_model()
        pickle.dump(t_p, ser_file)
        ser_file.close()
    if i < Mapping_Lines:
        has_lines = False
