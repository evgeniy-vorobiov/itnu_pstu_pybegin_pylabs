import re
from sys import stderr
from random import randint
from itertools import product
from pprint import pprint
from json import load, dump
NOT_FOUND = '$'
MIN_WORD_SIMILARITY = 0
MIN_QUESTION_SIMILARITY = 0.5

class Brain():
    answers = ('да','нет')

    def __init__(self):
        self.memory = {}
        try:
            loaded = load(fp=open('memory.json'))
            for str_key, val in loaded.items():
                tuple_key = tuple(str_key.split())
                self.memory.update({tuple_key:val})
        except FileNotFoundError:
            pass

    def save(self):
        to_save = {}
        for tuple_key, val in self.memory.items():
            str_key = re.sub(r'[()\', ]+',' ',str(tuple_key)).strip()
            to_save.update({str_key:val})
        dump(
            obj=to_save,
            fp=open('memory.json','w'),
            ensure_ascii=0,
            indent=4
        )

    def __fuzzy_key_search(self, words):
        answer = NOT_FOUND
        for key in self.memory:
            rez = []
            for w1, w2 in product(key, words):
                w = self.__compare(w1, w2)
                if w > MIN_WORD_SIMILARITY:
                    rez += [ (w, w1, w2) ]
            if sum((x[0] for x in rez)) / len(rez) > MIN_QUESTION_SIMILARITY:
                answer = self.memory[key]
        assert answer != NOT_FOUND
        return answer

    def __compare(self, s1, s2):
        count = 0
        for ngram in ( s1[i:i+3] for i in range(len(s1)-1) ):
            count += s2.count(ngram)
        return count / max(len(s1), len(s2))

    def think(self, question):
        words = tuple(re.sub(r'[!;:?,.-]',' ', question).split())
        try:
            return "Я уже отвечала, ответ был %s." % self.memory[words]
        except KeyError:
            try:
                answer = self.__fuzzy_key_search(words)
                return "Я, кажется, уже отвечала, ответ был %s." % answer
            except (AssertionError, ZeroDivisionError):
                answer = self.answers[randint(0, len(self.answers)-1)]
                self.memory.update({words:answer})
                return "Мой ответ - %s!" % answer

if __name__ == '__main__':
    brain = Brain()
    print(brain.think('Какой-то вопрос?'))
    print(brain.think('Какой-то вопрос?'))
    print(brain.think('Какой то вопросик?'))
    print(brain.think('Какой то вопросчек?'))
    print(brain.think('Какой то вопросчечечек?'))
    print(brain.think('Сегодня будет дождь?'))
    print(brain.think('Завтра будет дождь?'))
    brain.save()


"""
    Гадалка
"""
#from brain import Brain

brain = Brain()
prompt = "Что Вас интересует?"

question = ""
while question != "хватит":
    print(prompt, end = ' ')
    answer = brain.think(input())
    print(answer)





















