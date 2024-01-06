class RandomizedSet:
    
    def __init__(self):
        self.arrayHashMap = {}
        self.randomSet = []

    def insert(self, val: int) -> bool:
        if val not in self.arrayHashMap:
            self.arrayHashMap[val] = len(self.randomSet)
            self.randomSet.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.arrayHashMap:
            tmpPlaceholder = self.randomSet[len(self.randomSet) -1]
            self.randomSet[len(self.randomSet) -1] = self.randomSet[self.arrayHashMap[val]]
            self.randomSet[self.arrayHashMap[val]] = tmpPlaceholder
            self.arrayHashMap[tmpPlaceholder] = self.arrayHashMap[val]
            self.randomSet.pop(len(self.randomSet) -1)
            del self.arrayHashMap[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        return self.randomSet[random.randrange(0, len(self.randomSet))]