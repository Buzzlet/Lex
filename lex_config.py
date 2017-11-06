states = [1,2,3,4,5,6]
start_state = 1,
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890.@!#$%&'*+-/=?^_`{|}~;"
accepting_states = [3]
transition_matrix = []


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
		if self.valid:
			print("Username:", self.username)
			print("Local Host:", self.local_host)
			print("2nd Level Domain:", self.snd_lvl_domain)
			print("Top Level Domain:", self.top_lvl_domain)
			print()

	def mealy_actions(self, state, char):
		if char != '\n':
			self.parsed_email += char

	def moore_actions(self, state):
		pass