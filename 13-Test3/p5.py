class C:
    def __init__(self, numbers):
        self.numbers = numbers
    def __str__(self):
        wyr="+".join(map(str, self.numbers))
        return  f"{wyr}={sum(self.numbers)}"
print(C([5,1]))