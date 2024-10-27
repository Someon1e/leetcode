# https://leetcode.com/problems/design-hashmap/description/


class MyHashMap:
    def __init__(self):
        self.array = [[] for _ in range(197)]

    def put(self, key: int, value: int) -> None:
        hashed = key % len(self.array)
        self.remove(key)
        self.array[hashed].append((key, value))

    def get(self, key: int) -> int:
        hashed = key % len(self.array)
        for other_key, value in self.array[hashed]:
            if key == other_key:
                return value
        return -1

    def remove(self, key: int) -> None:
        hashed = key % len(self.array)
        for index, (other_key, value) in enumerate(self.array[hashed]):
            if key == other_key:
                del self.array[hashed][index]


# TODO: tests
