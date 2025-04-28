def greet(bot_name,birth_year):
    print("hello my name is {0}!".format(bot_name))
    print("I was created in {0}!".format(birth_year))

def remind_name():
    print("please remind me your name: ")
    name=input()
    print("what a great name you have, {0}!".format(name))

def guess_age():
    print("let me guess your age!")
    print("enter remainders after dividing your age by 3, 5 and 7 respectively:")
    rem3=int(input())
    rem5=int(input())
    rem7=int(input())
    age = (rem3*70 + rem5*21 + rem7*15)%105
    print("your age is {0}, that's a good time to start programming!".format(age))

def count():
    print("now i will prove that i can count to any number you want!")
    no=int(input("enter a number: "))
    counter=0
    while counter<=no:
        print("{0}".format(counter))
        counter+=1

def test():
    print("ley us test your programming knowledge!")
    print("why do we use methods?")
    print("1. to repeat a statement multiple times")
    print("2. to decompose a routine into multiple small sub routines")
    print("3. to determine execution time of a program")
    print("4. to interrupt execution of a program")
    print("enter your choice: ")
    ans=2
    choice=int(input())
    while(choice!=ans):
        print("wrong answer!")
        choice=int(input())
    print("correct ans! have a nice day...")
    print(".")
    print(".")
    print(".")
    print(".")

def end():
    print('Congratulations, have a nice day!')
    print('.')
    print('.')
    print('.')
    input()

greet('TE-Chatbot', '2022')
remind_name()
guess_age()
count()
test()
end()
