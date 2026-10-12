print("              king MUTHUVEER ASSISTANT")
print("=" * 50)
print("Hello! I am MUTHU AI.")
print("I can help with Maths, Science and general questions.")
print("Type 'help' to see my commands.")
print("Type 'bye' to exit.") 
print("=" * 50)

name = ""

while True:

    user = input("\nYou: ").strip()
    question = user.lower()

    # EXIT
    if question in ["bye", "exit", "quit"]:
        print("Raj AI: Goodbye! See you again.")
        break

    # GREETING
    elif question in ["hi", "hello", "hey"]:
        replies = [
            "Hello! How can I help you?",
            "Hi! What would you like to learn?",
            "Hey! Ask me a Maths or Science question."
        ]

        print("Raj AI:", random.choice(replies))

    # HELP
    elif question == "help":
        print("""
Raj AI can currently do:

1. Maths calculations
2. Square roots
3. Powers
4. Area of circles
5. Science questions
6. Tell the time
7. Remember your name

Examples:

calculate 25 * 8
sqrt 144
power 2 10
area circle 5

what is gravity
what is photosynthesis
what is an atom
what is dna
what is force
what is speed
""")

    # NAME
    elif question.startswith("my name is "):

        name = user[11:].strip()

        print("Raj AI: Nice to meet you,", name)

    elif question == "what is my name":

        if name:
            print("Raj AI: Your name is", name)
        else:
            print("Raj AI: You haven't told me your name yet.")

    # TIME
    elif question in ["time", "what is the time"]:

        current_time = datetime.now().strftime("%I:%M %p")

        print("Raj AI: The current time is", current_time)

    # CALCULATOR
    elif question.startswith("calculate "):

        expression = question[10:]

        try:
            # Only allow basic mathematical characters
            allowed = "0123456789+-*/().% "

            if all(character in allowed for character in expression):

                answer = eval(
                    expression,
                    {"__builtins__": None},
                    {}
                )

                print("Raj AI:", answer)

            else:
                print("Raj AI: Please enter a valid calculation.")

        except:
            print("Raj AI: I could not calculate that.")

    # SQUARE ROOT
    elif question.startswith("sqrt "):

        try:

            number = float(question[5:])

            if number < 0:
                print("Raj AI: I cannot calculate the real square root of a negative number.")
            else:
                answer = math.sqrt(number)
                print("Raj AI:", answer)

        except ValueError:
            print("Raj AI: Please enter a number.")

    # POWER
    elif question.startswith("power "):

        try:

            values = question.split()

            number = float(values[1])
            power = float(values[2])

            answer = number ** power

            print("Raj AI:", answer)

        except:
            print("Raj AI: Example: power 2 5")

    # CIRCLE AREA
    elif question.startswith("area circle "):

        try:

            radius = float(question[12:])

            area = math.pi * radius ** 2

            print("Raj AI: Area =", round(area, 2))

        except:
            print("Raj AI: Example: area circle 5")

    # SCIENCE KNOWLEDGE

    elif "gravity" in question:

        print("""
Raj AI:
Gravity is a force that attracts objects toward each other.

On Earth, gravity pulls objects toward the centre of the Earth.

Earth's gravitational acceleration is approximately:

9.8 m/s²
""")

    elif "photosynthesis" in question:

        print("""
Raj AI:
Photosynthesis is the process plants use to make food.

Plants use:

Sunlight
Carbon dioxide
Water

They produce:

Glucose
Oxygen

Equation:

Carbon dioxide + Water
        ↓ sunlight
Glucose + Oxygen
""")

    elif "atom" in question:

        print("""
Raj AI:
An atom is one of the basic units of matter.

Atoms contain:

Protons     → Positive charge
Neutrons    → No charge
Electrons   → Negative charge

Protons and neutrons are found in the nucleus.
Electrons exist around the nucleus.
""")

    elif "dna" in question:

        print("""
Raj AI:
DNA stands for Deoxyribonucleic Acid.

DNA contains genetic information that helps determine
how living organisms grow, develop and function.

DNA has a double-helix structure.
""")

    elif "force" in question:

        print("""
Raj AI:
Force is a push or pull acting on an object.

Newton's Second Law:

Force = Mass × Acceleration

F = m × a

Force is measured in Newtons (N).
""")

    elif "speed" in question:

        print("""
Raj AI:

Speed tells us how fast something is moving.

Formula:

Speed = Distance / Time

Example:

Distance = 100 metres
Time = 20 seconds

Speed = 100 / 20

Speed = 5 m/s
""")

    elif "water" in question:

        print("""
Raj AI:
Water is a chemical compound.

Chemical formula:

H₂O

This means one water molecule contains:

2 Hydrogen atoms
1 Oxygen atom
""")

    elif "solar system" in question or "planets" in question:

        print("""
Raj AI:
The eight planets in our Solar System are:

1. Mercury
2. Venus
3. Earth
4. Mars
5. Jupiter
6. Saturn
7. Uranus
8. Neptune
""")

    # UNKNOWN QUESTION
    else:

        print("""
Raj AI: I don't know the answer to that question yet.

I am still a small Python AI.

Try asking me about:
Maths
Gravity
Atoms
DNA
Force
Speed 
Planets
photosynthesis
""")

 