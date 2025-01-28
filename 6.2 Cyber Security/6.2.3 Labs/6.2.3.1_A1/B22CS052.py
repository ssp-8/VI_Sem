import math
from smtplib import SMTP
import numpy as np
import string

def mail_OTP(mailID: str):
    # Using SMTP
    s = SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login(
        user="sumeetpatil20004@gmail.com",
        password="zpyf tsfo gzfu elnx",
    )
    OTP = np.random.randint(1e5,1e6-1)
    message = f"Subject: Your OTP Code  \n\nBody: Welcome to the Password Checker\nYour OTP is {OTP}"
    s.sendmail("b22cs052@iitj.ac.in",mailID,message)

    return OTP


def password_strength_checker(password : str):

    def get_entropy(password: str):

        #size = lower_case + upper_case + numeric_digit + punctuation
        size = 26 + 26 + 10 + len(string.punctuation)

        # reference for entropy : https://www.geeksforgeeks.org/password-entropy-in-cryptography/
        entropy = len(password) * math.log2(size)
    
        if entropy < 28:
            print("Your password is Weak")
        elif entropy >= 28 and entropy <= 36:
            print("Your password is Moderate")
        else:
            print("Your password is Strong")
    

    def password_met_complexity(password: str):
        
        # common passwords taken from : https://github.com/Sharma-IT/password-strength-checker
        passwords = [
            "123456", "password", "12345678", "qwerty", "12345", "123456789", "1234567", "111111", 
            "1234569", "iloveyou", "adobe123", "123123", "admin", "1234567890", "letmein", "photoshop", 
            "1234", "monkey", "shadow", "sunshine", "1234567", "password1", "princess", "azerty", 
            "trustno1", "000000", "1234556", "dragon", "baseball", "football", "welcome", "jesus", 
            "password12", "654321", "qwertyuiop", "solo", "cookie", "starwars", "passw0rd", "michael", 
            "pokemon", "ninja", "zaq12wsx", "metallica", "charlie", "superman", "batman", "naruto", 
            "access", "anthony", "pepper", "daniel", "12345678910", "iloveyou!", "freedom", "whatever", 
            "scooter", "purple", "orange", "snoopy", "lovely", "marina", "success", "blue", "magic", 
            "winner", "peanut", "fantasia", "edward", "8888888", "01234", "pepper01", "aaron431", 
            "password01", "thomas", "cocacola", "qazwsx", "7777777", "myspace1", "password1", "computer", 
            "michelle", "corvette", "Hello123", "youtube", "secret", "abcd1234", "summer", "internet", 
            "asshole", "ginger", "princess1", "george", "cookie1", "cheese", "mickey", "tigger", "robert", 
            "soccer", "boomer", "nfvgbh", "compaq", "gateway", "asa123", "batman1", "nanook", "slipknot", 
            "frodo", "0987654321", "q1w2e3r4", "peaches", "badboy", "power", "samantha", "misty", "jasmine", 
            "mercedes", "steven", "dallas", "jessica", "guitar", "chelsea", "dexter", "amber", "danielle", 
            "blink182", "mike", "toyota", "blowme", "asdfghjkl", "samsung", "dolphins", "elephant", 
            "marlboro", "aaaaa1", "monica", "jimmy", "birdie", "crystal", "maverick", "catdog", "banana", 
            "pookie", "kitty", "superfly", "amanda", "muffin", "redsox", "winter", "barbie", "william", 
            "jonathan", "ginger01", "taylor", "pokemon1", "titanic", "angels", "jordan23", "michell1", 
            "4815162342", "drowssap", "samson", "jackson", "anime", "123qwe", "fucking", "dakota", 
            "fender1", "ncc1701d", "slayer", "cloud", "porn", "softball", "camaro", "mattie", "morgan", 
            "harley", "ranger1", "987654321", "phoenix", "jennifer", "ireland", "hockey", "corolla", 
            "simpsons", "monster", "dave", "victoria", "red123", "11111111111", "gunner", "helpme", 
            "asswordp", "hottie", "money", "123abc", "lovers", "098765", "green", "98765432", "maverick1", 
            "braves", "welcome1", "4444444", "liverpool", "poopoo", "shitty", "asdfgh", "happy123", 
            "creative", "drowssap123", "admin123", "drive", "banana1", "testing", "legend", "jason1", 
            "melissa", "brooklyn", "therock", "princessa", "coffee", "booboo", "kitten", "satan666", 
            "mitchell", "lucky", "wildcard", "fucker", "dilbert1", "island", "butthead", "isabelle", 
            "winnie", "casper", "richard", "bitches", "magnum", "chance", "bubbles", "testing12", "sexy", 
            "maxwell", "killer", "maria123", "school", "pepper123", "xbox360", "galore", "maggie123", 
            "sexsex", "bigdog", "beautiful", "minniemouse", "family", "hottie1", "trebor", "secret1", 
            "penguin", "merlin", "veronica", "yankees1", "987654321a", "matthew1", "ashley", "hello123", 
            "elizabet", "school123", "captain", "shadow1", "master1", "123456a", "qwertyu", "charlie1", 
            "loveme", "football1", "loveyou", "696969696", "explorer1", "christin", "q1w2e3", "sweet", 
            "pokemon123", "qwerty123", "cocacola1", "compaq123", "tennis", "9876543210", "midnight", 
            "martin", "mickeymouse", "nintendo", "babygirl", "asd123", "college", "party", "love123", 
            "lovely1", "789456", "xxxxxx", "serenity", "passw0rd", "0000"
        ]

        has_lower_case = False
        has_upper_case = False
        has_digit = False
        has_special_character = False
        # checking for the parameters mentioned in the lab key requirements
        for char in password:

            char_ascii = ord(char)
            # upper case
            if char_ascii >= 65 and char_ascii <= 90:
                has_upper_case = True
            # lower case
            elif char_ascii >= 97 and char_ascii <= 122:
                has_lower_case = True
            # numeric digit
            elif char_ascii >= 48 and char_ascii <= 57:
                has_digit = True
            # special characters
            elif (char_ascii >= 33 and char_ascii <= 47) or (char_ascii >= 58 and char_ascii <= 64):
                has_special_character = True
            
            if(has_special_character and has_upper_case and has_lower_case and has_digit):
                break
        
        # length of password and common check is done and returned as tuple
        return (len(password) >= 8,has_lower_case,has_upper_case,has_digit,has_special_character,password not in passwords)
    
    
    password_params = password_met_complexity(password)

    # to print error messages in case a requirement is not met
    error_messages = [
        "Please have minimum 8 characters",
        "Please have atleast one lower case character in your password",
        "Please have atleast one upper case character in your password",
        "Please have atleast one numeric digit in your password",
        "Please have atleast special character in your password",
        "Your password is too common"
    ]

    # checking whether requirements are met
    for i,param in enumerate(password_params):
        if param == False:
            print(error_messages[i])
            return False
    
    # looking for strength
    get_entropy(password)
    return True
    
    


pass_req = "● Minimum 8 characters\n"+"● Contains both uppercase and lowercase letters\n"+"● Includes at least one numeric digit\n"+"● Has at least one special character (e.g., !, @, #, etc)\n"+"● No commonly used passwords (e.g., 'password123', '123456')"
mailID = input("Please Enter mail ID: ")
password = input("Password must:\n"+pass_req+"\nPlease enter Password: ")


is_password_valid = password_strength_checker(password)

# is password is meeting requirements, then mailing the OTP
if is_password_valid:

    OTP = mail_OTP(mailID)
    i = 0

    # giving the user 5 chances to enter otp
    while i < 5:

        OTP_entered = input(f"Please enter the OTP sent to you on your mail {mailID}: ")
        try:
            if int(OTP_entered) == OTP:
                print("User Verified")
                break
            else:
                print("Invalid OTP")
                i+=1
        except:
            print("Invalid OTP")
            i+=1
        
    if i == 5:
        print("You have entered wrong OTP 5 times. Please try again later")
    
    


