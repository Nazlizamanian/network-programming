#Lab10 Nazli Zamanian Gustavsson Regex


#10.2 Introductory experiments
import re
txt = "Hanoror bought 5 portions of orange soil for 13.50 EUR."
re.findall("or", txt)

#10.2.1 Dot means joker
#dot in regex matches all characters. except linebreak.
import re
txt = "Hanoror bought 5 portions of orange soil for 13.50 EUR."
re.findall(".", txt)

import re
txt = "Hanoror bought 5 portions of orange soil for 13.50 EUR."
re.findall("or.", txt) #searches for all strings that start with or and continue charater.
# findall find only non-overlapping strings.

re.findall("..\.",txt) #gives us a real . 

#10.2.3 Other special characters
re.findall(r"\w",txt) #w as in word, matches all words. 
re.findall(r"\W",txt)#!= as w, w as not word. 

re.findall(r"\d",txt) #digit
re.findall(r"\D",txt)# opposite gives word. 

re.findall(r"\s",txt) #spaces 



#Task 1 

def is_valid_email(email):
    # Define the regular expression pattern for a valid email address
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Use re.match() to check if the email matches the pattern
    match = re.match(email_pattern, email)
    
    # If there is a match, print the email address; otherwise, print an error message
    if match:
        print(f"The email address '{email}' is valid.")
    else:
        print(f"The email address '{email}' is not valid.")

# Test the function with examples
is_valid_email('r.nohre@jth.hj.se')
is_valid_email('bjox@se')
is_valid_email('adam@example.com')
is_valid_email('jox@jox@jox.com."')
