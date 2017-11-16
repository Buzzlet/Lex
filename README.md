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
	- A sequence of integers delimted by spaces
	Transition Matrix
	- Pairs of lines
	- First line: A string of characters to follow the second line's state changes
	- Second line: A sequence of transitions delimited by a comma and a space (", "). Each transition consists of two integers separated by a space.

### Test File
- The test file is a sequence of strings of characters to be validated
- One test case per line is permitted

