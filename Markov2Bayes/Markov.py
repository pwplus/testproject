__author__ = 'Travis Salas Cox'

from random import randint, choice


class MarkovChain:
    def __init__(self, seed_file):
        self.db = {}
        self.seed_file = seed_file
        self.words = self.make_words()
        self.number_of_words = len(self.words)
        self.to_db()

    def __repr__(self):
        return "your own person markov generator " + str(__name__)

    def __str__(self):
        return str((self.words, self.db))

    def make_words(self):
        self.seed_file.seek(0)
        words = self.seed_file.read().split()
        return words

    def markov_triples(self):
        if self.number_of_words >= 3:
            for i in range(self.number_of_words - 2):
                yield (self.words[i], self.words[i + 1], self.words[i + 2])

    def to_db(self):
        for word_one, word_two, word_three in self.markov_triples():
            key_pair = (word_one, word_two)
            if key_pair in self.db.keys():
                self.db[key_pair].append(word_three)
            else:
                self.db[key_pair] = [word_three]

    def gen_pseudo_random_text(self, text_length=None):
        length = 30 if text_length is None else text_length
        seed_int = randint(0, self.number_of_words - 3)
        first_word, second_word = self.words[seed_int], self.words[seed_int + 1]
        done = False
        generated_words = []
        while not done:
            try:
                for i in xrange(length-1):
                    generated_words.append(first_word)
                    first_word, second_word = second_word, choice(self.db[(first_word, second_word)])
                generated_words.append(second_word)
                done = True
            except KeyError:
                seed_int = randint(0, self.number_of_words - 3)
                first_word, second_word = self.words[seed_int], self.words[seed_int + 1]
                generated_words = []

        return ' '.join(generated_words)


if __name__ == "__main__":
    random_int = randint(0, 101)
    file = open('C:\Users\Travis Salas Cox\PycharmProjects\Markov2Bayes\dummy-text.txt')
    markov = MarkovChain(file)
    print markov.gen_pseudo_random_text(text_length=random_int)
