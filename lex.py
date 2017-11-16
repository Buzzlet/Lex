import sys
import lex_config as conf
# The class_file must always be named lex_config.py

def get_config_file():
	return input("Enter the file name of the config file: ")


def get_test_file():
	return input("Enter the file name of the test file: ")


def create_transition_matrix(config):
	# The remainder of the file are pairs of lines
	# The first line of the pair is the subset of the alphabet that the
	# transitions apply to. The following line is the transitions (old->new)
	transition_matrix = []
	matrix_row = config.readline().strip('\n')
	while matrix_row != "":
		new_row = []
		new_row.append(matrix_row)
		transitions = config.readline().strip('\n').split(", ")
		for transition in transitions:
			old_state, new_state = transition.split()
			new_row.append((int(old_state), int(new_state)))
		transition_matrix.append(new_row)
		matrix_row = ''.join(config.readline().rsplit())
	return transition_matrix


def main(args):

	# If there wasn't a config file specified
	config_file = None
	if len(args) < 2:
		config_file = get_config_file()
	else:
		config_file = args[1]


	# If there wasn't a test file specified
	test_file = None
	if len(args) < 3:
		test_file = get_test_file()
	else:
		test_file = args[2]


	config = open(config_file)

	# First line of config file is the start state
	start_state = int(config.readline().strip('\n'))

	# Second line of config file was the alphabet (never actually used)
	# Because every alphabet character has an entry in the transition matrix,
	# the actual alphabet is stated implicitly in the transition matrix

	# The second line is now sequence of accepting states
	accept_states = config.readline().strip('\n').split()
	for i in range(len(accept_states)):
		accept_states[i] = int(accept_states[i])

	# Construct the transition matrix
	transition_matrix = create_transition_matrix(config)
	
	# initiate testing
	with open(test_file) as fp:

		# Continue getting test cases as long as they exist
		test_case = fp.readline().strip('\n')
		while test_case != "":
			state = start_state
			new_creation = conf.New_Creation()

			# Look at each character sequentially
			for char in test_case:
				new_creation.mealy_actions(state, char)
				
				# trying to weasel out the new state from the matrix
				for entry in transition_matrix:
					# Find the entry in the transition matrix for the subset
					# of the alphabet in which this character lies
					if char in entry[0]:
						entry_index = transition_matrix.index(entry)
						# Find the transition to take based on what state we're
						# currently in. Update state
						for state_change in transition_matrix[entry_index][1:]:
							if state_change[0] == state:
								state = state_change[1]
								break;
				
				new_creation.moore_actions(state)

			if state in accept_states:
				new_creation.valid = True
			
			new_creation.finalize()
			new_creation.output()

			test_case = fp.readline()

main(sys.argv)