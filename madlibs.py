def main():
    adj1 = input("Adjective: ")
    noun = input("Noun: ")
    adj2 = input("Adjective: ")
    noun2 = input("Noun; place: ")
    adj3 = input("Adjective: ")
    adj4 = input("Adjective: ")
    pnoun = input("Plural noun; vehicle: ")
    adj5 = input("Adjective: ")
    adj6 = input("Adjective: ")
    pnoun2 = input("Plural noun: ")
    adj7 = input("Adjective: ")
    pnoun3 = input("Plural noun: ").title()
    pnoun4 = input("Plural noun: ")
    adj8 = input("Adjective: ")
    noun3 = input("Noun: ").title()
    verb = input("Verb: ")
    adj9 = input("Adjective: ")
    verb2 = input("Verb: ")
    pnoun5 = input("Plural noun: ")
    pnoun6 = input("Plural noun; type of job: ")
    adj10 = input("Adjective: ")
    verb3 = input("Verb: ")
    adj11 = input("Adjective: ")

    madlib = f"\nStar Wars Madlib Story\nStar Wars is a {adj1} {noun} of {adj2} versus evil in a {noun2} far, far away.\nThere are {adj3} battles between {adj4} {pnoun} in {adj5} space and {adj6} duels with {pnoun2} called {adj7} sabers.\n{pnoun3} called 'droids' are helpers and {pnoun4} to the heroes. A {adj8} power called The {noun3} {verb}s people to do {adj9} things, like {verb2} {pnoun5}.\nThe Jedi {pnoun6} use The Force for the {adj10} side and the Sith {verb3} it for the {adj11} side."

    print(madlib)


if __name__ == "__main__":
    main()
