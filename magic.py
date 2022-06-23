#Greet user
print("Welcome to the Magic 8-Ball game. Follow the instructions and have fun.\n")

import random

#Make list of auto response
response = ['It is certain.','You may rely on it.','Most likely.','Yes, definitely!','As I see it, yes.','Ask again later.','Concentrate and ask again.','Cannot predict now.','Do not count on it','My sources say no.','Very doubtful']

#Ask for user's name
print('I am the Magic 8-Ball. What is your name?')
name=input()
print('Welcome, '+ name.title())

#Def main to call for user's question
def main():
    print('Ask me a question. ')
    input()

#Return the auto response from list
    print(response[random.randint(0,10)])
    replay()

#Def replay to play again. The user will enter a yes or no answer to the question below:
def replay():

    print('Are you satisfied with your answer? [Yes/No] ')
    reply = input()
    if (reply == 'No' or reply == 'no'):
        print('Concentrate, breathe in, breathe out and try again.')
        main()
    elif (reply == 'Yes' or reply =='yes'):
        print('See you later 👋')
        exit()
    else:
        print('Please enter Yes or No')
        replay()

#Call back main to run the code
main()