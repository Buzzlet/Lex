import lex_config as conf
import sys




def main(config_file, test_file):

	# With this specific email parser, we're going to simplify the definition
	# of an email address to not allow quotes or comments, so dots must not be
	# consecutive, and not all special characters are allowed in the local-part
	# the local part will allow alphanumeric characters and the following
	# special characters !#$%&'.*+-/=?^_`{|}~;

	# The domain will not allow IP address literals or keywords like localhost
	# and will allow - anywhere in the domain and will allow all-numeric domains
	
	config = open(config_file)
	start_state = int(config.readline().strip('\n'))
	alphabet = config.readline().strip('\n')
	accept_states = config.readline().strip('\n').split()
	for i in range(len(accept_states)):
		accept_states[i] = int(accept_states[i])

	transition_matrix = list()
	matrix_row = config.readline().strip('\n')
	while matrix_row != "":
		new_row = list()
		new_row.append(matrix_row)
		line = config.readline().strip('\n')
		transitions = line.split(", ")
		for transition in transitions:
			old_state, new_state = transition.split()
			new_row.append((int(old_state), int(new_state)))
		transition_matrix.append(new_row)
		matrix_row = ''.join(config.readline().rsplit())
	
	# initiate testing
	with open(test_file) as fp:
		test_case = fp.readline()
		while test_case != "":
			state = start_state
			new_creation = conf.New_Creation()
			for char in test_case:
				new_creation.mealy_actions(state, char)
				
				# trying to weasel out the new state from the matrix
				for entry in transition_matrix:
					if char in entry[0]:
						entry_index = transition_matrix.index(entry)
						for state_change in transition_matrix[entry_index][1:]:
							if state_change[0] == state:
								state = state_change[1]
								break;
				
				new_creation.moore_actions(state)

			if state in accept_states:
				new_creation.valid = True
			test_case = fp.readline()
			new_creation.finalize()
			new_creation.output()

main(sys.argv[1], sys.argv[2])