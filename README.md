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
	- finalize()
	- output()
- Must be in the same directory as lex.py

### Configuration File
- The configuration file must present the configuration for the given lexeme with the following format:

	Start State  
	- A single integer

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

- Valid email addresses have a username part before an "@".
- Valid usernames allow the common characters: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!#$%&'*+-/=?^_\`{|}~;.
- Valid usernames do not start with, end with, or have consecutive dots.
- After the username there is an "@".
- Following the single "@", the remainder has the same format as the username, but must have at least one dot
