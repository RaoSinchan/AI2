problem_dict = {
    "printer not working":"check that it is turned on and connected to the network",
    "cant log in":"make sure you are using the correct username and password",
    "software not installing": "make sure your computer meets system requirements",
    "internet not working":"restart your modem or router",
    "mailbox not updating": "check your internet connection" 
}

def handle_req(user_inp):
    if user_inp.lower() == "exit":
        return ("Goodbye!")
    elif user_inp in problem_dict:
        return (problem_dict[user_inp])
    else:
        return ("sorry! i do not know how to deal with that isue rn 🥲")
    
while True:
    user_inp=input("what's the problem, type 'exit' to quit: ")
    response=handle_req(user_inp)
    print(response)
    if user_inp.lower()=="exit":
        break
