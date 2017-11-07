start_state = 0
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890.@!#$%&'*+-/=?^_`{|}~;"
accepting_states = [7]
'''
This transition matrix must be formatted such that they are lists of relationships such that
the first element is a list of characters that have this entry in the table. The following
elements of the list are tuples in the form (state, new_state) 
'''
transition_matrix = [["abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!#$%&'*+-/=?^_`{|}~;",
					  (0,1), (1,1), (2,2), (3,1), (4,5), (5,5), (6,7), (7,7)],
					 [".", (0,2), (1,3), (2,2), (3,2), (4,2), (5,6), (6,2), (7,2)],
					 ["@", (0,2), (1,4), (2,2), (3,2), (4,2), (5,2), (6,2), (7,2)]
					]


class New_Creation():
	def __init__(self):
		''''''
		self.parsed_email = ""
		self.top_lvl_domain = ""
		self.snd_lvl_domain = ""
		self.local_host = ""
		self.username = ""
		self.valid = True

	def output(self):
		print("Input:", self.parsed_email, "->", "valid" if self.valid else "invalid")
		#if self.valid:
		print("Username:", self.username)
		print("Local Host:", self.local_host)
		print("2nd Level Domain:", self.snd_lvl_domain)
		print("Top Level Domain:", self.top_lvl_domain)
		print()

	def mealy_actions(self, state, char):
		#print("Mealy in state", state, "with char", char)
		if char != '\n':
			self.parsed_email += char

		# if we're looking at a '.'
		if char in transition_matrix[1][0]:
			if state in [0,1,3]:
				self.username += char

		elif char in transition_matrix[0][0]:
			if state in [0,1,3]:
				self.username += char
			elif state in [4,5]:
				self.snd_lvl_domain += char
			elif state in [6,7]:
				self.top_lvl_domain += char

	def moore_actions(self, state):
		if state in accepting_states:
			self.valid = True
		else:
			self.valid = False