# Quiz Game Final Draft

INSTRUCTIONS = """
    Instructions:
    1) Each question has 10 points.
    2) Each has 4 options to choose from.
    3) You can see the results at the end.
    4) Can exit the game anytime.
"""

# List of all of the questions, options, and answer. 
game_dict = [ { "question": 'What is fear of spiders called?', 'options': ['Arachnophobia','Claustrophobia','Acrophobia','Aerophobia'], 'answer': 'Arachnophobia'} ,
{"question": 'What is the capital city of Australia?','options': ['Melbourne','Sydney','Adelaide','Perth'],'answer': 'Sydney'},
{"question": 'What continent is Czech Republic in?','options': ['Asia','America','Africa','Europe'],'answer': 'Europe'},
{"question": 'What is the official language of China?','options': ['Mandarin','Cantonese','Hunanese','Kejia'],'answer': 'Mandarin'},
{"question": 'How many ounces are in a cup?','options': ['16','6','4','8'],'answer': '8'},
{"question": 'What is the name of the biggest desert in the world?','options': ['Kaveer','Gobi','Arabian','Sahara'],'answer': 'Sahara'},
{"question": 'Who was the first man on the moon?','options': ['Neil Armstrong','Yuri Gagarin','Sunita Williams','Jack Swigert'],'answer': 'Neil Armstrong'},
{"question": 'What is the capital of Illinois?','options': ['Chicago','Seattle','Carson City','Springfield'],'answer': 'Springfield'},
{"question": 'When was the U.S. national anthem written?','options': ['1880','1814','1910','1790'],'answer': '1814'},
{"question": 'What is California motto?','options': ['In God We Trust','Excelsior','Eureka','Friendship'],'answer': 'Eureka'}
]

# List of prizes
prizes = ['a head massager.','a set of shampoo and conditioner.','a BOSE mini speaker.','a pack of 4 hand sanitizers.','a set of 2 custom-made face masks.']

# Function to print the questions and list the options 
def print_question(num):

    question_answers = game_dict[num]
    question = question_answers['question']
    option_list = question_answers['options']
    print(f"\n{num+1}. {question}")
    print(f"\na. {option_list[0]}    b. {option_list[1]}     c. {option_list[2]}     d. {option_list[3]}\n")


# Function to get and evaluate the answer  
def check_the_answer(n):
    
        user_answer = input(">: ").lower().strip()
       
        if n == 0 and (user_answer == 'a' or user_answer == 'arachnophobia'):
            return True
        elif n == 1 and (user_answer == 'b' or user_answer == 'sydney'):
            return True
        elif n == 2 and (user_answer == 'd' or user_answer == 'europe'):
            return True
        elif n == 3 and (user_answer == 'a' or user_answer == 'mandarin'):
            return True
        elif n == 4 and (user_answer == 'd' or user_answer == '8'):
            return True
        elif n == 5 and (user_answer == 'd' or user_answer == 'sahara'):
            return True
        elif n == 6 and (user_answer == 'a' or user_answer == 'neil armstrong'):
            return True
        elif n == 7 and (user_answer == 'd' or user_answer == 'springfield'):
            return True
        elif n == 8 and (user_answer == 'b' or user_answer == '1814'):
            return True
        elif n == 9 and (user_answer == 'c' or user_answer == 'eureka'):
            return True
        else:
            return False
 
# Function to match score with prize
def match_score(scr):
    
    if  (scr != 0) and (scr <= 20):
        prize = prizes[0]
    elif 20 < scr <= 40:
        prize = prizes[1]
    elif 40 < scr <= 60:
        prize = prizes[2]
    elif 60 < scr <= 80:
        prize = prizes[3]
    elif 80 < scr <= 100:
        prize = prizes[4]
    else:
        prize = "nothing 😐"
    return prize

# Main function of the game
def play_game():
    score = 0
    correct_answers = 0
    incorrect_answers = 0
    q_num = 0
    # Ask for player's name 
    print("Hi there, What is your name?")
    user_name = input("> ").title().strip()
    # Greet the player
    # Show welcome message 
    print(f"\nWelcome {user_name}!")
    # Explain the rules
    print(INSTRUCTIONS)
    # Start the loop
    # looping 10 times for 10 questions 
    while q_num < 10:
        # Ask user to continue or Exit 
        choice = input("\nPress ENTER to continue  or   E: to exit> ").lower().strip()
        if choice == '':
            # Ask question #x and list the options  
            print_question(q_num)
            # verify the answer
            player_answer = check_the_answer(q_num)
            # Checking the answer
            if player_answer == True:
                # Print correct
                print("\nCorrect! 👍")
                # Add 10 points
                score = score + 10
                # Add 1 to the variable correct_answers
                correct_answers += 1
                # show score
                print("Score:",score)
            else:
                # Print incorrect
                print(f'\nIncorrect! 👎 the answer is {game_dict[q_num]["answer"]}')
                incorrect_answers += 1
                print("Score:",score)

            q_num += 1
        elif choice == 'e':
            # Stop the loop 
            break
        else:
            print("Not a valid answer!")
    # printing scores and prize(if any)    
    gift = match_score(score)
    print(f"\nResults:\nScore: {score}\nCorrect Answers: {correct_answers}\nIncorrect Answers: {incorrect_answers}\nYou won {gift}")

play_game()