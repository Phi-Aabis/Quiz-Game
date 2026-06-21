import sys
import random


SCORE = 0


# question bank of the questions which are of easy difficulty
EasyQuestions = [
    {
        "question": "Q: 3² = ?",
        "options": ["A) 6", "B) 9", "C) 12", "D) 3"],
        "answer": "B"
    },
    {
        "question": "Q: Fastest land animal?",
        "options": ["A) Lion", "B) Tiger", "C) Cheetah", "D) Leopard"],
        "answer": "C"
    },
    {
        "question": "Q: What is the capital of France?",
        "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
        "answer": "C"
    },
    {
        "question": "Q: What planet is known as the Red Planet?",
        "options": ["A) Earth", "B) Mars", "C) Venus", "D) Jupiter"],
        "answer": "B"
    },
    {
        "question": "Q: What is 5 + 7?",
        "options": ["A) 10", "B) 11", "C) 12", "D) 13"],
        "answer": "C"
    },
    {
        "question": "Q: Which ocean is the largest?",
        "options": ["A) Atlantic Ocean", "B) Indian Ocean", "C) Pacific Ocean", "D) Arctic Ocean"],
        "answer": "C"
    },
    {
        "question": "Q: What color do you get by mixing red and white?",
        "options": ["A) Pink", "B) Purple", "C) Orange", "D) Brown"],
        "answer": "A"
    },
    {
        "question": "Q: Who wrote 'Romeo and Juliet'?",
        "options": ["A) Charles Dickens", "B) William Shakespeare", "C) Mark Twain", "D) Jane Austen"],
        "answer": "B"
    },
    {
        "question": "Q: How many continents are there?",
        "options": ["A) 5", "B) 6", "C) 7", "D) 8"],
        "answer": "C"
    },
    {
        "question": "Q: What is H2O commonly known as?",
        "options": ["A) Salt", "B) Oxygen", "C) Water", "D) Hydrogen"],
        "answer": "C"
    },
    {
        "question": "Q: Which animal is known as the king of the jungle?",
        "options": ["A) Tiger", "B) Lion", "C) Elephant", "D) Bear"],
        "answer": "B"
    },
    {
        "question": "Q: What is the largest mammal?",
        "options": ["A) Elephant", "B) Blue whale", "C) Giraffe", "D) Shark"],
        "answer": "B"
    },
    {
        "question": "Q: Which instrument has keys, pedals, and strings?",
        "options": ["A) Guitar", "B) Piano", "C) Drum", "D) Flute"],
        "answer": "B"
    },
    {
        "question": "Q: What do bees produce?",
        "options": ["A) Milk", "B) Silk", "C) Honey", "D) Wax"],
        "answer": "C"
    },
    {
        "question": "Q: Which season comes after spring?",
        "options": ["A) Winter", "B) Autumn", "C) Summer", "D) Monsoon"],
        "answer": "C"
    },
    {
        "question": "Q: How many legs does a spider have?",
        "options": ["A) 6", "B) 8", "C) 10", "D) 12"],
        "answer": "B"
    },
    {
        "question": "Q: What is the currency of the USA?",
        "options": ["A) Euro", "B) Dollar", "C) Pound", "D) Yen"],
        "answer": "B"
    },
    {
        "question": "Q: Which organ pumps blood?",
        "options": ["A) Brain", "B) Liver", "C) Heart", "D) Lung"],
        "answer": "C"
    },
    {
        "question": "Q: What is the square root of 16?",
        "options": ["A) 2", "B) 3", "C) 4", "D) 5"],
        "answer": "C"
    },
    {
        "question": "Q: What is the square root of 16?",
        "options": ["A) 2", "B) 3", "C) 4", "D) 5"],
        "answer": "C"
    },
    {
        "question": "Q: Which bird can mimic human speech?",
        "options": ["A) Sparrow", "B) Crow", "C) Parrot", "D) Eagle"],
        "answer": "C"
    },
    {
        "question": "Q: Which sport uses a bat and ball?",
        "options": ["A) Football", "B) Cricket", "C) Tennis", "D) Hockey"],
        "answer": "B"
    },
    {
        "question": "Q: What is the freezing point of water?",
        "options": ["A) 0°C", "B) 10°C", "C) -10°C", "D) 5°C"],
        "answer": "A"
    },
    {
        "question": "Q: What is the capital of Pakistan?",
        "options": ["A) Lahore", "B) Karachi", "C) Islamabad", "D) Peshawar"],
        "answer": "C"
    },
    {
        "question": "Q: Which direction does the sun rise from?",
        "options": ["A) North", "B) South", "C) East", "D) West"],
        "answer": "C"
    },
    {
        "question": "Q: Which metal is liquid at room temperature?",
        "options": ["A) Iron", "B) Mercury", "C) Copper", "D) Aluminum"],
        "answer": "B"
    },
    {
        "question": "Q: What is the main ingredient in bread?",
        "options": ["A) Rice", "B) Flour", "C) Sugar", "D) Oil"],
        "answer": "B"
    },
    {
        "question": "Q: Which fruit is yellow and curved?",
        "options": ["A) Apple", "B) Banana", "C) Mango", "D) Orange"],
        "answer": "B"
    },
    {
        "question": "Q: Which planet is closest to the Sun?",
        "options": ["A) Venus", "B) Mercury", "C) Earth", "D) Mars"],
        "answer": "B"
    },
    {
        "question": "Q: Which country is known for the Eiffel Tower?",
        "options": ["A) Italy", "B) Spain", "C) France", "D) Germany"],
        "answer": "C"
    },
    {
        "question": "Q: What is the main source of energy for Earth?",
        "options": ["A) Moon", "B) Sun", "C) Wind", "D) Water"],
        "answer": "B"
    },
    {
        "question": "Q: Which part of the plant conducts photosynthesis?",
        "options": ["A) Root", "B) Stem", "C) Leaf", "D) Flower"],
        "answer": "C"
    },
    {
        "question": "Q: Which country is famous for sushi?",
        "options": ["A) China", "B) Japan", "C) Korea", "D) Thailand"],
        "answer": "B"
    },
    {
        "question": "Q: Which number is a multiple of 6?",
        "options": ["A) 14", "B) 18", "C) 20", "D) 22"],
        "answer": "B"
    }
]

# question bank of the questions which are of medium difficulty
MediumQuestions = [
    {
        "question": "Q: Largest desert?",
        "options": ["A) Sahara", "B) Gobi", "C) Arctic", "D) Kalahari"],
        "answer": "C"
    },
    {
        "question": "Q: Which organ filters blood in humans?",
        "options": ["A) Heart", "B) Kidney", "C) Liver", "D) Lung"],
        "answer": "B"
    },
    {
        "question": "Q: What is the currency of Japan?",
        "options": ["A) Yuan", "B) Won", "C) Yen", "D) Dollar"],
        "answer": "C"
    },
    {
        "question": "Q: What is the capital of Saudi Arabia?",
        "options": ["A) Jeddah", "B) Riyadh", "C) Mecca", "D) Medina"],
        "answer": "B"
    },
    {
        "question": "Q: What is the boiling point of ethanol?",
        "options": ["A) 78°C", "B) 100°C", "C) 90°C", "D) 120°C"],
        "answer": "A"
    },
    {
        "question": "Q: Which vitamin is produced in sunlight?",
        "options": ["A) A", "B) B", "C) C", "D) D"],
        "answer": "D"
    },
    {
        "question": "Q: What is the longest river in the world?",
        "options": ["A) Nile", "B) Amazon", "C) Yangtze", "D) Mississippi"],
        "answer": "A"
    },
    {
        "question": "Q: Which gas is most abundant in Earth's atmosphere?",
        "options": ["A) Oxygen", "B) Nitrogen", "C) Carbon dioxide", "D) Hydrogen"],
        "answer": "B"
    },
    {
        "question": "Q: What is 15 percent of 200?",
        "options": ["A) 20", "B) 25", "C) 30", "D) 35"],
        "answer": "C"
    },
    {
        "question": "Q: What is the main language of Spain?",
        "options": ["A) French", "B) Italian", "C) Spanish", "D) Portuguese"],
        "answer": "C"
    },
    {
        "question": "Q: Which metal is used in electrical wiring?",
        "options": ["A) Gold", "B) Copper", "C) Iron", "D) Zinc"],
        "answer": "B"
    },
    {
        "question": "Q: What is the SI unit of force?",
        "options": ["A) Joule", "B) Newton", "C) Watt", "D) Pascal"],
        "answer": "B"
    },
    {
        "question": "Q: What is 7 squared?",
        "options": ["A) 42", "B) 47", "C) 49", "D) 51"],
        "answer": "C"
    },
    {
        "question": "Q: Which country is known as the Land of the Rising Sun?",
        "options": ["A) China", "B) Japan", "C) Korea", "D) Thailand"],
        "answer": "B"
    },
    {
        "question": "Q: Which organelle is the powerhouse of the cell?",
        "options": ["A) Nucleus", "B) Ribosome", "C) Mitochondria", "D) Golgi body"],
        "answer": "C"
    },
    {
        "question": "Q: Who painted the Mona Lisa?",
        "options": ["A) Van Gogh", "B) Da Vinci", "C) Picasso", "D) Rembrandt"],
        "answer": "B"
    },
    {
        "question": "Q: What is the hardest natural substance?",
        "options": ["A) Gold", "B) Iron", "C) Diamond", "D) Quartz"],
        "answer": "C"
    },
    {
        "question": "Q: Which element has atomic number 1?",
        "options": ["A) Helium", "B) Hydrogen", "C) Oxygen", "D) Carbon"],
        "answer": "B"
    },
    {
        "question": "Q: What is the capital of Canada?",
        "options": ["A) Toronto", "B) Vancouver", "C) Ottawa", "D) Montreal"],
        "answer": "C"
    },
    {
        "question": "Q: Which country hosted the 2016 Olympics?",
        "options": ["A) China", "B) Brazil", "C) UK", "D) Japan"],
        "answer": "B"
    },
    {
        "question": "Q: Who developed the theory of relativity?",
        "options": ["A) Newton", "B) Einstein", "C) Galileo", "D) Tesla"],
        "answer": "B"
    },
    {
        "question": "Q: Who discovered gravity?",
        "options": ["A) Einstein", "B) Newton", "C) Galileo", "D) Kepler"],
        "answer": "B"
    },
    {
        "question": "Q: What is the capital of Turkey?",
        "options": ["A) Istanbul", "B) Ankara", "C) Izmir", "D) Bursa"],
        "answer": "B"
    },
    {
        "question": "Q: Which planet has rings?",
        "options": ["A) Mars", "B) Earth", "C) Saturn", "D) Venus"],
        "answer": "C"
    },
    {
        "question": "Q: Who was the first man to walk on the Moon?",
        "options": ["A) Buzz Aldrin", "B) Yuri Gagarin", "C) Neil Armstrong", "D) Michael Collins"],
        "answer": "C"
    },
    {
        "question": "Q: Which country is both in Europe and Asia?",
        "options": ["A) Egypt", "B) Turkey", "C) Spain", "D) Germany"],
        "answer": "B"
    },
    {
        "question": "Q: What is the boiling point of water in Fahrenheit?",
        "options": ["A) 180°F", "B) 200°F", "C) 212°F", "D) 220°F"],
        "answer": "C"
    },
    {
        "question": "Q: Which gas is used in photosynthesis?",
        "options": ["A) Oxygen", "B) Nitrogen", "C) Carbon dioxide", "D) Hydrogen"],
        "answer": "C"
    },
    {
        "question": "Q: Which country gifted the Statue of Liberty to the USA?",
        "options": ["A) UK", "B) Germany", "C) France", "D) Italy"],
        "answer": "C"
    },
    {
        "question": "Q: Which organ produces insulin?",
        "options": ["A) Liver", "B) Kidney", "C) Pancreas", "D) Heart"],
        "answer": "C"
    },
    {
        "question": "Q: What is 18 × 7?",
        "options": ["A) 112", "B) 126", "C) 132", "D) 140"],
        "answer": "B"
    },
    {
        "question": "Q: What is the currency of the United Kingdom?",
        "options": ["A) Euro", "B) Pound Sterling", "C) Dollar", "D) Franc"],
        "answer": "B"
    },
    {
        "question": "Q: Which ocean is the deepest?",
        "options": ["A) Atlantic", "B) Indian", "C) Arctic", "D) Pacific"],
        "answer": "D"
    }
]

# questions bank of the question which are of hard difficulty
HardQuestions = [
    {
        "question": "Q: What is the derivative of sin(x)?",
        "options": ["A) cos(x)", "B) -cos(x)", "C) sin(x)", "D) -sin(x)"],
        "answer": "A"
    },
    {
        "question": "Q: Which particle has no electric charge?",
        "options": ["A) Proton", "B) Electron", "C) Neutron", "D) Positron"],
        "answer": "C"
    },
    {
        "question": "Q: What is the integral of 1/x dx?",
        "options": ["A) x", "B) ln|x|", "C) e^x", "D) 1/x^2"],
        "answer": "B"
    },
    {
        "question": "Q: What is Planck's constant approximately?",
        "options": ["A) 6.63x10^-34", "B) 3x10^8", "C) 9.8", "D) 1.6x10^-19"],
        "answer": "A"
    },
    {
        "question": "Q: Which country has the most time zones?",
        "options": ["A) USA", "B) Russia", "C) France", "D) China"],
        "answer": "C"
    },
    {
        "question": "Q: What is Avogadro's number?",
        "options": ["A) 6.02x10^23", "B) 3x10^8", "C) 9.8", "D) 1.6x10^-19"],
        "answer": "A"
    },
    {
        "question": "Q: Which element has the highest electronegativity?",
        "options": ["A) Oxygen", "B) Fluorine", "C) Chlorine", "D) Nitrogen"],
        "answer": "B"
    },
    {
        "question": "Q: What is the capital of Iceland?",
        "options": ["A) Oslo", "B) Helsinki", "C) Reykjavik", "D) Stockholm"],
        "answer": "C"
    },
    {
        "question": "Q: Which country invented paper?",
        "options": ["A) India", "B) Egypt", "C) China", "D) Greece"],
        "answer": "C"
    },
    {
        "question": "Q: What is the derivative of e^x?",
        "options": ["A) x", "B) e^x", "C) ln(x)", "D) 1/x"],
        "answer": "B"
    },
    {
        "question": "Q: What is 2^10?",
        "options": ["A) 512", "B) 1024", "C) 2048", "D) 4096"],
        "answer": "B"
    },
    {
        "question": "Q: Who developed calculus independently with Newton?",
        "options": ["A) Leibniz", "B) Euler", "C) Gauss", "D) Lagrange"],
        "answer": "A"
    },
    {
        "question": "Q: What is the speed of sound in air?",
        "options": ["A) 343 m/s", "B) 300 m/s", "C) 400 m/s", "D) 500 m/s"],
        "answer": "A"
    },
    {
        "question": "Q: What is the largest internal organ?",
        "options": ["A) Heart", "B) Liver", "C) Kidney", "D) Lung"],
        "answer": "B"
    },
    {
        "question": "Q: What is the unit of electric current?",
        "options": ["A) Volt", "B) Ampere", "C) Ohm", "D) Watt"],
        "answer": "B"
    },
    {
        "question": "Q: What is the formula for kinetic energy?",
        "options": ["A) mv", "B) 1/2 mv^2", "C) mgh", "D) v^2/r"],
        "answer": "B"
    },
    {
        "question": "Q: Which planet has the shortest day?",
        "options": ["A) Earth", "B) Jupiter", "C) Mars", "D) Venus"],
        "answer": "B"
    },
    {
        "question": "Q: What is the binary of 5?",
        "options": ["A) 101", "B) 111", "C) 100", "D) 110"],
        "answer": "A"
    },
    {
        "question": "Q: Which scientist discovered electrons?",
        "options": ["A) Rutherford", "B) Thomson", "C) Bohr", "D) Dalton"],
        "answer": "B"
    },
    {
        "question": "Q: Which law states that entropy of an isolated system always increases?",
        "options": ["A) First Law of Thermodynamics", "B) Second Law of Thermodynamics", "C) Third Law of Thermodynamics", "D) Zeroth Law of Thermodynamics"],
        "answer": "B"
    },
    {
        "question": "Q: Which mathematician proved Fermat's Last Theorem?",
        "options": ["A) Euler", "B) Gauss", "C) Andrew Wiles", "D) Lagrange"],
        "answer": "C"
    },
    {
        "question": "Q: What is the SI unit of electric charge?",
        "options": ["A) Ampere", "B) Coulomb", "C) Volt", "D) Ohm"],
        "answer": "B"
    },
    {
        "question": "Q: What is the sum of the interior angles of a pentagon?",
        "options": ["A) 360°", "B) 540°", "C) 720°", "D) 900°"],
        "answer": "B"
    },
    {
        "question": "Q: What is the value of 0! (zero factorial)?",
        "options": ["A) 0", "B) 1", "C) Undefined", "D) Infinity"],
        "answer": "B"
    },
    {
        "question": "Q: Which country has the longest coastline in the world?",
        "options": ["A) Russia", "B) Canada", "C) Australia", "D) USA"],
        "answer": "B"
    },
    {
        "question": "Q: What is the binary representation of 10?",
        "options": ["A) 1010", "B) 1110", "C) 1001", "D) 1100"],
        "answer": "A"
    },
    {
        "question": "Q: Which gas law states that pressure is inversely proportional to volume?",
        "options": ["A) Charles's Law", "B) Gay-Lussac's Law", "C) Boyle's Law", "D) Avogadro's Law"],
        "answer": "C"
    },
    {
        "question": "Q: What is the derivative of ln(x^2)?",
        "options": ["A) 2/x", "B) 1/x", "C) x", "D) ln(x)"],
        "answer": "A"
    },
    {
        "question": "Q: Which planet has the longest orbital period?",
        "options": ["A) Earth", "B) Mars", "C) Saturn", "D) Neptune"],
        "answer": "D"
    },
    {
        "question": "Q: What is the value of tan(0°)?",
        "options": ["A) 1", "B) 0", "C) Undefined", "D) -1"],
        "answer": "B"
    },
    {
        "question": "Q: Which scientist discovered radioactivity?",
        "options": ["A) Curie", "B) Becquerel", "C) Rutherford", "D) Bohr"],
        "answer": "B"
    },
    {
        "question": "Q: What is the binary representation of 8?",
        "options": ["A) 1000", "B) 1111", "C) 1010", "D) 1100"],
        "answer": "A"
    },
    {
        "question": "Q: What is the sum of the first 10 natural numbers?",
        "options": ["A) 45", "B) 50", "C) 55", "D) 60"],
        "answer": "C"
    }
]


# main function where execution of game is done.
def main():
    global EasyQuestions
    global MediumQuestions
    global HardQuestions
    global SCORE
    selection(sys.argv)
    print("Only give the letter of the answer, nothing else. ")
    questioning()
    print(totalScore())


# gaurdrail to stop users from not using the command line arguments properly
def selection(args):
    global EasyQuestions
    global MediumQuestions
    global HardQuestions
    global SCORE
    try:
        if args[1] == "-d":
            difficulty = args[2]
            if not difficulty in ["Easy", "Medium", "Hard"]:
                raise ValueError("Error: the difficulty can only be set to 'Easy', 'Medium', or 'Hard'")

            if args[3] == "-n":
                totalQs = args[4]
                if not 1 <= int(totalQs) <= 33:
                    raise ValueError("Error: the total number of questions asked in the program (totalQs) can only be from 1 to 33 (inclusive)")

        elif args[1] == "-n":
            totalQs = int(args[2])
            if not 1 <= totalQs <= 33:
                raise ValueError("Error: the total number of questions asked in the program (totalQs) can only be from 1 to 33 (inclusive)")

            if args[3] == "-d":
                difficulty = args[4]
                if not difficulty in ["Easy", "Medium", "Hard"]:
                    raise ValueError("Error: the difficulty can only be set to 'Easy', 'Medium', or 'Hard'")

        else:
            raise ValueError("Error: you must select either the difficulty or total number of questions asked first and then the other. You can do this by typing '-d (Easy, Medium, or Hard)' or '-n k' where k is an acceptable integer")
    except ValueError:
        sys.exit("Error: you must write an integer after '-n'")


# actual prompting of questions
def questioning():
    global SCORE
    args = sys.argv

    if args[1] == "-d":
        difficulty = args[2]
        num = int(args[4])
    elif args[1] == "-n":
        num = int(args[2])
        difficulty = args[4]
    else:
        sys.exit("Invalid arguments")

    if difficulty == "Easy":
        questions = EasyQuestions
    elif difficulty == "Medium":
        questions = MediumQuestions
    elif difficulty == "Hard":
        questions = HardQuestions
    else:
        sys.exit("Invalid difficulty")

    if num > len(questions):
        sys.exit("Not enough questions in the bank.")

    selected_questions = random.sample(questions, num)

    for question in selected_questions:
        print(question["question"])
        for opt in question["options"]:
            print(opt)

        user_answer = input("Your answer: ")
        print()

        if user_answer == question["answer"]:
            SCORE += 1

# the function which allows the user to see their total score
def totalScore():
    print("\n")
    if sys.argv[1] == "-d":
        return f"You scored {SCORE} out of {sys.argv[4]}. "
    if sys.argv[1] == "-n":
        return f"You scored {SCORE} out of {sys.argv[2]}. "
    print("\n")


if __name__ == "__main__":
    main()


#### Meow :3
