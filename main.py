import string
import os

# ANSI escape codes for text colors
class TextColor:
    MAIN = '\033[37m'
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'

# Password requirements with color
password_requirements = f"""{TextColor.YELLOW}Your password must include the following to meet security standards:{TextColor.RESET}\n
- {TextColor.MAIN}At least one uppercase letter{TextColor.RESET}.
- {TextColor.MAIN}At least one lowercase letter{TextColor.RESET}.
- {TextColor.MAIN}At least one special character{TextColor.RESET}.
- {TextColor.MAIN}At least one digit{TextColor.RESET}.
- {TextColor.MAIN}A minimum length of 8 characters{TextColor.RESET}.\n"""

def change_color_based_on_index(index):

    global password_requirements
    lines = password_requirements.split('\n')
    
    if 0 <= index < len(lines):
        lines[index] = lines[index].replace(TextColor.MAIN, TextColor.RED)
        
    modified_string = '\n'.join(lines)
    password_requirements = modified_string

def resetRequirementColor():
    global password_requirements
    password_requirements = password_requirements.replace(TextColor.RED,TextColor.MAIN)


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def check_password_strength(password: str) -> int:
    score = 0

    # Check if the password contains at least one character from each required character class
    if any(c.isupper() for c in password):
        score += 1
    else:
        change_color_based_on_index(2)
    if any(c.islower() for c in password):
        score += 1
    else:
        change_color_based_on_index(3)
    if any(c in string.punctuation for c in password):
        score += 1
    else:
        change_color_based_on_index(4)
    if any(c.isdigit() for c in password):
        score += 1
    else:
        change_color_based_on_index(5)

    if len(password) >= 8:
        score+= 1
    else:
        change_color_based_on_index(6)
    
    # Check if the password is long enough
    for length_threshold in [10, 12, 14, 16, 18]:
        if len(password) >= length_threshold:
            score += 1
  
    return score

def check_password(password: str) -> string:
    # Check the password strength
    score = check_password_strength(password)

    if score < 4:
         return f"{TextColor.RED}Weak (Do not meet all the requirements){TextColor.RESET}\n"
    elif score <= 8:
        return f"{TextColor.BLUE}Moderate (Meets most(if not all) requirements but not strong){TextColor.RESET}"
    else:
        return f"{TextColor.GREEN}Strong{TextColor.RESET}"

def select_retry():
    while True:
        retry_choice = input("Password does not meet requirements. Retry? (yes/no): ").lower()
        if retry_choice in ['yes', 'no']:
            return retry_choice

clear_console()

while True:
    print(password_requirements)
    password = input(f"{TextColor.YELLOW}Enter password:{TextColor.RESET} ")
    clear_console()


    results = check_password(password)

    print(password_requirements)

    print(f"{TextColor.YELLOW}Enter password:{TextColor.RESET}" + password)

    print("Password strength: " +results)
    

    retry_choice = select_retry()

    if retry_choice != 'yes':
        break
    else:
        resetRequirementColor()
        clear_console()
