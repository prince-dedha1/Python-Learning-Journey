# KBC-Style Quiz Game
# This program asks multiple-choice questions and rewards the user for correct answers.
# The game stops when the user gives a wrong answer.

import time

# List of all questions
question_lst = [
    "01.What is the color of the sky on a clear day?\n",
    "02.Which animal is known as the “king of the jungle”?\n",
    "03.What is the capital of India?\n",
    "04.In computing, RAM stands for?\n",
    "05.Who wrote Pride and Prejudice?\n",
    "06.Which planet is known as the Red Planet?\n",
    "07.What is H₂O chemically?\n",
    "08.Which country is known as the Land of the Rising Sun?\n",
    "09.Who discovered penicillin?\n",
    "10.In which year did India gain independence?\n",
    "11.What is the square root of 256?\n",
    "12.The Great Barrier Reef is off the coast of which country?\n",
    "13.Who was the first person to set foot on the moon?\n",
    "14.What is the chemical symbol for gold?\n",
    "15.Who wrote the Iliad and the Odyssey?\n",
    "16.Who commanded the 'Hector', the first British trading ship to land at Surat?\n"
]

# List of options for each question
option_lst = [
    ["A) Green", "B) Blue", "C) Purple", "D) Red\n"],
    ["A) Elephant", "B) Tiger", "C) Lion", "D) Cheetah\n"],
    ["A) Mumbai", "B) Bengaluru", "C) New Delhi", "D) Kolkata\n"],
    ["A) Readily Available Memory", "B) Random Access Memory", "C) Rapid Application Management", "D) Run All Modules\n"],
    ["A) Jane Austen", "B) Charlotte Brontë", "C) Mary Shelley", "D) Emily Brontë\n"],
    ["A) Venus", "B) Mars", "C) Jupiter", "D) Mercury\n"],
    ["A) Hydrogen peroxide", "B) Hydrochloric acid", "C) Water", "D) Ozone\n"],
    ["A) China", "B) South Korea", "C) Japan", "D) Thailand\n"],
    ["A) Louis Pasteur", "B) Alexander Fleming", "C) Robert Koch", "D) Jonas Salk\n"],
    ["A) 1945", "B) 1946", "C) 1947", "D) 1948\n"],
    ["A) 12", "B) 14", "C) 16", "D) 18\n"],
    ["A) South Africa", "B) Australia", "C) Brazil", "D) Indonesia\n"],
    ["A) Neil Armstrong", "B) Buzz Aldrin", "C) Yuri Gagarin", "D) Michael Collins\n"],
    ["A) Au", "B) Ag", "C) Fe", "D) Pb\n"],
    ["A) Sophocles", "B) Euripides", "C) Homer", "D) Plato\n"],
    ["A) Paul Canning", "B) William Hawkins", "C) Thomas Rose", "D) James Lancaster\n"]
]

# List of correct answers
correct_optn = ["B", "C", "C", "B", "A", "B", "C", "C", "B", "C", "C", "B", "A", "A", "C", "B"]

# Corresponding prize money for each correct answer
prize_money_lst = [1000, 2000, 5000, 10000, 20000, 40000, 80000, 160000,
                   320000, 640000, 1250000, 2500000, 5000000, 10000000, 30000000, 70000000]

won_money = 0  # Total money won so far
stop = 0       # Control flag to end the game on wrong answer

# Loop through all questions
for qn in range(0, 16):
    if stop == 0:
        # Display the question
        print(question_lst[qn])

        # Display corresponding options
        for opn in range(qn, qn + 1):
            opnlst = option_lst[opn]
            for k in opnlst:
                print(k)

        # Take user's answer
        answer = input("Enter the option (A/B/C/D)--->  ")

        # Check if answer is correct
        for ans in range(qn, qn + 1):
            if answer.upper() == correct_optn[ans]:
                for prize in range(qn, qn + 1):
                    won_money += prize_money_lst[prize]
                    print("✅ Correct!\n")
            else:
                # End the game if answer is wrong
                stop += 1
                print("❌ ❌ ❌ SORRY WRONG ANSWER ❌ ❌ ❌")
    else:
        break

# Display total winnings
print(f"🎉 Congratulations! You Won ₹{won_money}")
