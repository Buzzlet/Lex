# Lex
This is a program written for my Concepts of Programming Languages class intended to demonstrate how lexical analysis is used in parsing. The Lex program must be portable and generic enough that it can run given any language description.

## Usage

### Command Line Usage
- Standard usage: prompt> python lex.py /path/to/config_file /path/to/test_file
- If the configuration file or test file are not provided, the program will prompt the user for them

### Configuration Class
- Must be named lex_config.py
- Must have the following methods:
	- __init__()
	- mealy_actions()
	- moore_actions()
	- output()
- Must have the following attributes:
	- self.valid (boolean)
- Must be in the same directory as lex.py

### Configuration File
- The configuration file must present the configuration for the given lexeme with the following format:

	Start State  
	- A single integer

	Alphabet
	- A sequence of characters that are in the alphabet

	Accept States  
	- A sequence of integers delimited by spaces

	Transition Matrix  
	- Pairs of lines
	- First line: A string of characters to follow the second line's state changes
	- Second line: A sequence of transitions delimited by a comma and a space (", "). Each transition consists of two integers separated by a space.

### Test File
- The test file is a sequence of strings of characters to be validated
- One test case per line is permitted

# Email Implementation
Displayed below is the FSA for this implementation of email addresses

![alt text](https://github.com/Buzzlet/Lex/blob/master/email_fsa.png?raw=true "Email FSA")

## State Descriptions:
0. Start state, no characters seen 
1. There has been at least one "common" character seen in the username
2. Reject state, some character has deemed this an invalid email
3. The username has just had a dot
4. The username portion is complete and valid
5. The domain has at least one "common" character in it
6. The second level domain exists
7. The top level domain has a character
8. The top level domain has seen a dot and there is a local host

## Valid Email Addresses
- Valid email addresses have a username part before an "@".
- Valid usernames allow the common characters: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!#$%&'*+-/=?^_\`{|}~;.
- Valid usernames do not start with, end with, or have consecutive dots.
- After the username there is an "@".
- Following the single "@", the remainder has the same format as the username, but must have at least one dot


# Date Implementation
Displayed below is the FSA for this implementation of dates

![alt text](https://github.com/Buzzlet/Lex/blob/master/dates_fsa.png?raw=true "Date FSA")

## State Descriptions:
Because there are 40 states, a description of each is tedious, so I shall only describe the "important" states.
	0. Start state, no characters seen
	19. The date is being recognized under the Mon DD, YYYY format and has seen a valid month
	20. A valid month and a space has been seen, so the date is now expected
	23.The month, day, and comma have been successfully recognized and to continue on the Mon DD, YYYY format, a space is expected
	38. A valid month, space, date, comma, and space have been seen and the year is now expected.
	27. A valid Mon DD, YYYY date has been seen and accepted
	28. The date being recognized is under the YYYY-MM-DD format and has the first digit of the year
	31. The 4 digits for the year have been seen under the YYYY-MM-DD format
	32. The year and a dash have been seen, so the month is now expected
	34. YYYY-MM have been seen
	35. The second dash of the YYYY-MM-DD format has been seen, so the day digits are expected
	37. The day has been seen in the YYYY-MM-DD format and the entry is a valid date
	
## Valid Dates
- Valid dates can take on two formats:
	1. 2017-12-06 (YYYY-MM-DD)
		- The year must be 4 digits, the month must be 2 digits, and the day must be 2 digits as well. So, placeholder 0's are often required. The whole date is not validated, so 0000-00-00 is a valid date. Leap years are not taken into account either.
	2. Dec 6, 2017 (Mon DD, YYYY)
		- The month is not case sensitive, but must be either Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, or Dec
		- There must be a space followed by the date. The date can be either 1 or two digits. The date is not validated, so the date Dec 99, 2017 is valid.
		- Following the date there must be a "," and a space. Then a valid date requires 4 digits. These digits are not validated, so the year 0000 is valid.