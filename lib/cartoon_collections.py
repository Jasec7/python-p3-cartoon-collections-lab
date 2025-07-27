def roll_call_dwarves(line):
    numbered_names = [f'{index}. {name}'for index, name in enumerate(line, start = 1)]
    for names in numbered_names:
        print(names)

def summon_captain_planet(line):
    capital_letter =  [ n.title() + "!"  for n in line ]
    return capital_letter

def long_planeteer_calls(line):
    for word in line:
        if len(word) > 4:
            return True
    return False

def find_the_cheese(line):
    for cheese in line:
        if cheese == "gouda":
           return "gouda"
        elif cheese == "cheddar":
            return "cheddar"
        elif cheese == "camembert":
            return "camembert"
        else:
            None

    
