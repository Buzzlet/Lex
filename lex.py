import lex_config as conf
import sys

def output():
	pass

def main(test_file):

	# With this specific email parser, we're going to simplify the definition
	# of an email address to not allow quotes or comments, so dots must not be
	# consecutive, and not all special characters are allowed in the local-part
	# the local part will allow alphanumeric characters and the following
	# special characters !#$%&'.*+-/=?^_`{|}~;

	# The domain will not allow IP address literals or keywords like localhost
	# and will allow - anywhere in the domain and will allow all-numeric domains
	
	state = conf.start_state
	with open(test_file) as fp:
		test_case = fp.readline()
		while test_case != "":
			for char in test_case:
				conf.mealy_actions(current_state, char)
				#state = conf.transition_matrix[char_type][]
			test_case = fp.readline()

main(sys.argv[1])