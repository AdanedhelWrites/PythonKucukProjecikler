import time

noun = input("Enter noun: ")
plural_noun = input("Enter Plural Noun: ")
verb = input("Enter verb: ")
verb2 = input("Enter verb2: ")
plural = input("Enter Plural: ")
adjective = input("Enter adjective: ")
plural_noun2 = input("Enter Plural Noun: ")
adjective2 = input("Enter adjective: ")



print("Today, every stundet has a computer small enough to fit into his {}.He can solve any math problem by simply pushing the computer's little {}.Computers can add,multiply,divide,and {}.They can also {} better than a human.Some computers are {}.Other have a/an {} screen that shows all kinds of {} and {} figures.".format(noun, plural_noun,verb,verb2,plural,adjective,plural_noun2,adjective2))

time.sleep(15)
dogru_cevaplar = {
    "1.":"bed",
    "2.":"button",
    "3.":"kill",
    "4.":"be",
    "5.":"black",
    "6.":"open",
    "7.":"clothes",
    "8.":"even"}
print("True Answers are:")
print(dogru_cevaplar)


