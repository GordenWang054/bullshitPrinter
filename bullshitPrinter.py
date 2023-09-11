import random

class bullshitGenerator():
    def __init__(self, sentence):
        self.raw = sentence
        self.seed = len(sentence)
        
    def Seed(self, seed):
        self.seed = seed
    
    def randGenerator(self, sentence, seed = 42):
        random.seed(seed)
        rand_set = [random.randint(0,1) for i in range(len(sentence))]
        return rand_set
    
    def messUpOrder(self):
        rand_set = self.randGenerator(self.raw ,self.seed)
        new_sentence = ""
        for i, word in enumerate(self.raw):
            if rand_set[i] == 1:
                new_sentence = new_sentence + word
        for i, word in enumerate(self.raw):
            if rand_set[i] == 0:
                new_sentence = new_sentence + word
        return new_sentence
    
    def restore(self, sentence, seed):
        random.seed(seed)
        rand_set = [random.randint(0,1) for i in range(len(sentence))]
        index_set_of_one = [i for i, x in enumerate(rand_set) if x == 1]
        num_of_one = len(index_set_of_one)
        raw = ""
        j = 0
        k = 0
        for i in range(len(sentence)):
            if i in index_set_of_one:
                raw = raw + sentence[j]
                j = j + 1
            else:
                raw = raw + sentence[k+num_of_one]
                k = k + 1    
        return raw

    def content(self):
        return self.raw
        
    def show_seed(self):
        return self.seed

def restore(sentence, seed):
    random.seed(seed)
    rand_set = [random.randint(0,1) for i in range(len(sentence))]
    index_set_of_one = [i for i, x in enumerate(rand_set) if x == 1]
    num_of_one = len(index_set_of_one)
    raw = ""
    j = 0
    k = 0
    for i in range(len(sentence)):
        if i in index_set_of_one:
            raw = raw + sentence[j]
            j = j + 1
        else:
            raw = raw + sentence[k+num_of_one]
            k = k + 1    
    return raw

if __name__ == '__main__':
    print("please enter the sentence:")
    sentence = input()
    s1 = bullshitGenerator(sentence)
    seed = 0
    print("want to change the key ? please enter a number but 0:")
    seed = eval(input())
    if seed != 0:
        s1.Seed(seed)
    print(f"{s1.messUpOrder()}")
    print(f"relevent seed: {s1.show_seed()}")

