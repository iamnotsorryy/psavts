import secrets
class Password:
    def __init__(self, tuple_of_lists, length):
        self.length = length;
        self.tuple_of_lists = tuple_of_lists
    
    def generate(self):
        lst1 = []
        summa = 0
        for i in range(len(self.tuple_of_lists)):
            lst1.append(1 + secrets.randbelow(self.length))
            summa += lst1[i]
        print(lst1)
        while(summa > self.length):
            summa = 0
            lst1.index(max(lst1)) -= 1
            for i in range(len(self.tuple_of_lists)):
                summa += lst1[i]
            print(lst1)
        print(lst1)
            
def make_letters_list(): #список символов
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    letters += [letter.upper() for letter in letters]
    return letters
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] #список цифр

parol = Password(tuple_of_lists=(make_letters_list(), numbers), length=7)
parol.generate()
