def check_voter_eligibility():
    citizenship = input("Are you a Kenyan citizen? (yes/no): ").strip().lower()
    age= int(input("Enter your age: ").strip())

    if citizenship == "yes" and age >= 18:
        print("You are eligible to vote in Kenya. PROCEED")
    else:
        print("You are not eligible to vote.  WAIT UNTIL YOU TURN 18 MY FRIEND")

check_voter_eligibility()