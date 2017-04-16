from __future__ import division

import re
from collections import defaultdict


class IbmModel1(object):
    """Implement the ibm model 1 for language translation"""
    MIN_PROB = 1e-12

    def __init__(self, sentence_pairs, iterations):
        # sentence_pairs = [{french: "", english: ""}, ....]
        self.sentence_pairs = sentence_pairs
        self.d_e_w, self.d_f_w = self.__get_word_count__()
        self.t_prob = defaultdict(
            lambda: defaultdict(lambda: IbmModel1.MIN_PROB))
        self.iterations = iterations

    def __get_word_count__(self):
        eng_words = set()
        fren_words = set()
        for pair in self.sentence_pairs:
            f_line = re.sub("[\r\n,.()?]", '', pair["french"].lower())
            e_line = re.sub("[\r\n,.()?]", '', pair["english"].lower())
            f_tok = f_line.split(' ')
            e_tok = e_line.split(' ')
            f_tok = [self.__strip__(i) for i in f_tok]
            e_tok = [self.__strip__(i) for i in e_tok]
            pair["french"] = f_tok
            pair["english"] = [None] + e_tok
            for tok in f_tok:
                fren_words.add(tok)
            for tok in e_tok:
                eng_words.add(tok)
        return len(eng_words), len(fren_words)

    def __strip__(self, word):
        word = word.strip('\n\r?.\'')
        return word

    def train(self):
        """train the ibm model 1"""
        for itr in range(0, self.iterations):
            if itr % 10 == 0:
                print("beginning iteration: " + str(itr))
            count = defaultdict(lambda: defaultdict(lambda: 0.0))
            total = defaultdict(lambda: 0.0)
            for pair in self.sentence_pairs:
                f_tokens = pair["french"]
                e_tokens = pair["english"]
                s_total = defaultdict(lambda: 0.0)
                for f_token in f_tokens:
                    if s_total[f_token] == 0.0:
                        for e_token in e_tokens:
                            s_total[f_token] += self.t_prob[f_token][e_token]

                # collect counts
                for f_token in f_tokens:
                    for e_token in e_tokens:
                        add_f = self.t_prob[f_token][e_token] / \
                            s_total[f_token]
                        count[f_token][e_token] += add_f
                        total[e_token] += add_f

            # estimate probabilities

            for f in self.t_prob:
                for e in self.t_prob[f]:
                    factor = count[f][e] / total[e]
                    self.t_prob[f][e] = max(factor, IbmModel1.MIN_PROB)

    def print_params(self):
        for f_tok in self.t_prob:
            for e_tok in self.t_prob[f_tok]:
                print(f_tok, "|", e_tok, " = ", self.t_prob[f_tok][e_tok])

    def generate_refined_model(self):
        t_p = {}
        for f_tok in self.t_prob:
            t_p[f_tok] = {}
            for e_tok in self.t_prob[f_tok]:
                if self.t_prob[f_tok][e_tok] > IbmModel1.MIN_PROB:
                    t_p[f_tok][e_tok] = self.t_prob[f_tok][e_tok]
        return t_p
