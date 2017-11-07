import lex_config as conf
import sys

def main(test_file):

	# With this specific email parser, we're going to simplify the definition
	# of an email address to not allow quotes or comments, so dots must not be
	# consecutive, and not all special characters are allowed in the local-part
	# the local part will allow alphanumeric characters and the following
	# special characters !#$%&'.*+-/=?^_`{|}~;

	# The domain will not allow IP address literals or keywords like localhost
	# and will allow - anywhere in the domain and will allow all-numeric domains
	
	
	
	with open(test_file) as fp:
		test_case = fp.readline()
		while test_case != "":
			state = conf.start_state
			new_creation = conf.New_Creation()
			for char in test_case:
				new_creation.mealy_actions(state, char)
				
				# trying to weasel out the new state from the matrix
				for entry in conf.transition_matrix:
					if char in entry[0]:
						entry_index = conf.transition_matrix.index(entry)
						for state_change in conf.transition_matrix[entry_index][1:]:
							if state_change[0] == state:
								state = state_change[1]
								break;
				
				new_creation.moore_actions(state)


			test_case = fp.readline()

			new_creation.output()

main(sys.argv[1])