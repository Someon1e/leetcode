# https://leetcode.com/problems/design-hashset/description/


class MyHashSet:
    def __init__(self):
        self.array = [[] for _ in range(197)]

    def add(self, key: int) -> None:
        hashed = key % len(self.array)
        self.remove(key)
        self.array[hashed].append(key)

    def remove(self, key: int) -> None:
        hashed = key % len(self.array)
        if key in self.array[hashed]:
            self.array[hashed].remove(key)

    def contains(self, key: int) -> bool:
        hashed = key % len(self.array)
        return key in self.array[hashed]


# TODO: tests
