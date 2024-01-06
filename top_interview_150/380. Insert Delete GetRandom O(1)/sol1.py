class RandomizedSet:
    
    def __init__(self):
        self.arrayHashMap = {}
    def insert(self, val: int) -> bool:
        if val not in self.arrayHashMap:
            self.arrayHashMap[val] = 1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.arrayHashMap:
            del self.arrayHashMap[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(list(self.arrayHashMap.items()))[0]
    