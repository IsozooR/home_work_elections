def elections (citizen_age, citizen_disqualified, citizen_status):
    if citizen_age >= 18 and citizen_status == "y" and citizen_disqualified == "n":
        return "You can vote on the election"
    else:
        return "You can't vote on the election"


try:
    age = int(input("Please enter your age: "))
    disqualified = input("Are you disqualified? (y/n): ")
    citizen = input("Are you a citizen? (n/y): ")

    disqualified = disqualified.lower()
    citizen = citizen.lower()
except ValueError:
    print("Please enter your age again")
    exit()

if disqualified in ("y", "n") and citizen in ("y", "n"):
    print(elections(age, disqualified, citizen))
else:
    print("Mistake. try again")




