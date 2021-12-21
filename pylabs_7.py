from pprint import pprint

def compare(s1, s2):
    s1, s2 = [ s.lower() for s in [s1, s2] ]
    ngrams = [ s1[i:i + 3] for i in range(len(s1))]
    count = 0
    for ngram in ngrams:
        count += s2.count(ngram)
    return count / max(len(s1), len(s2))

def int_val(s):
    try:
        return int(s)
    except ValueError:
        return 0

if __name__ == '__main__':
    out = []
    for a,b in [
            ('алгоритм', 'алгоритм'),
            ('алгоритм', 'алгоритмы'),
            ('алгоритм', 'алгоритмов'),
            ('стол', 'столик'),
            ('стол', 'стул'),
            ('маша', 'даша'),
            ('ольга', 'олег'),
            ('Ольга', 'Наташа'),
            ('маша', 'машенька'),]:
        out +=  [(a,b,compare(a, b))]
        pprint(out)
        pprint([int_val(s) for s in ['старше', '30', 'но', '101']])


from pprint import pprint
from itertools import product
from utils import compare, int_val

ADDRESS_WORDS = {'дом', 'улица', 'живет'}
NAME_WORDS = {'имя', 'зовут'}
AGE_WORDS = {'старше', 'младше', 'возраст'}

class Person:
    def __init__(self, name, age, address):
        self.name, self.age, self.address = name, age, address
        self.key = (name, address)

    def fuzzy_compare(self, query):
        q = set(query.split())
        score = 0
        for m, f in zip(
            [ADDRESS_WORDS, NAME_WORDS, AGE_WORDS],
            [self.by_address, self.by_name, self.by_age]
        ):
            if m & q:
                score += f(q)

        return score > 0.51

    def by_address(self, Q):
        Q = Q-ADDRESS_WORDS
        W = set(self.address.split())
        rez = []
        for a,b in product(Q, W):
            rez += [(compare(a,b),a,b)]

        return max(rez)[0]

    def by_age(self, Q):
        q_age = max([int_val(q) for q in Q])
        if 'старше' in Q:
            return q_age < self.age
        if 'младше' in Q:
            return q_age > self.age

        return q_age+5 >= self.age >=q_age-5

    def by_name(self, Q):
        Q = Q - NAME_WORDS
        W = set(self.name.split())
        rez = []
        for a, b in product(Q, W):
            rez += [(compare(a,b),a,b)]

        return max(rez)[0]

    def __eq__(self, obj):
        if type(obj) == Person:
            return
        elif type(obj) == str:
            return self.fuzzy_compare(obj)
        else:
            return false

    def __repr__(self):
        return "Person('%s',%s,'%s')" % (self.name, self.age, self.address)

if __name__ == '__main__':
    lena = Person("Лена", 19, "Пушкина, 14, 115")
    oleg = Person("Олег", 34, "Ленского, 10, 11")
    olga = Person("Ольга", 28, "Онегина, 11, 12")
    nata = Person("Наташа", 17, "Ростова, 16, 15")

    quares = [
            'имя Ольга',
            'возраст 30',
            'старше 20',
            'младше 20',
            'живет на Пушкина',
            'дом 10',
            'фамилия Ростова',
            'зовут нташа',]

    people = {
            lena.key: lena,
            oleg.key: oleg,
            olga.key: olga,
            nata.key: nata
    }

    for query, person in product(quares, people.values()):
        if person == query:
            print(query, person)

