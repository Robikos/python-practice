from collections import Counter
from collections import defaultdict

from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement
from itertools import chain


def incrementor():
    index = 0
    while True:
        yield index
        index += 1


x = Counter([1, 2, 3, 4, 5, 4, 3, 1, 1])
y = Counter([1, 2, 4, 4])


class MyCounter:
    def __init__(self, collection: list):
        self.collection = collection
        self.result = {}
        self.count()

    def count(self):
        for key in self.collection:
            self.result[key] = self.result.get(key, 0) + 1

    def most_common(self, size=-1):
        return list(self.result.items())[0:size] if size != -1 else list(self.result.items())

    def __str__(self):
        return f"MyCounter({self.result})"

    def __repr__(self):
        return self.__str__()


x = defaultdict(lambda: 10)


class MyDefaultDict:
    def __init__(self, callable_fun):
        self.callable_fun = callable_fun
        self.dictionary = {}

    def __getitem__(self, item):
        return self.dictionary[item] if item in self.dictionary.keys() else self.missing_key(item)

    def __setitem__(self, key, value):
        self.dictionary[key] = value

    def missing_key(self, item):
        self.dictionary[item] = self.callable_fun()
        return self.dictionary[item]

    def __str__(self):
        return f"MyDefaultDict({self.dictionary})"

    def __repr__(self):
        return self.__str__()


x = MyDefaultDict(lambda: 10)


class MyContainer:
    pass


def tree():
    return defaultdict(tree)


root = tree()
x = permutations([1, 2, 3, 4])


def my_permutations(collection: list):
    if len(collection) == 1:
        yield collection

    for element in collection:
        collection_left = collection.copy()
        collection_left.remove(element)

        for subpermutation in my_permutations(collection_left):
            yield [element] + subpermutation


x = combinations([1, 2, 3, 4], 2)


def my_combinations(collection: list, size: int):
    if size == 1:
        for element in collection:
            yield [element]

    for element in collection:
        collection_left = collection.copy()
        collection_left.remove(element)

        for subcombination in my_combinations(collection_left, size - 1):
            yield [element] + subcombination


x = combinations_with_replacement([1, 2, 3, 4], 2)


def my_combinations_with_replacement(collection: list, size: int):
    if size == 1:
        for element in collection:
            yield [element]

    for element in collection:

        for subcombination in my_combinations_with_replacement(collection, size - 1):
            yield [element] + subcombination


x = combinations([1, 2, 3], 2)
y = combinations(['a', 'b', 'c'], 2)
z = chain(x, y)


def my_chain(*iterables):
    for iterable in iterables:
        for element in iterable:
            yield element


