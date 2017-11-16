class New_Creation():
	def __init__(self):
		''''''
		self.parsed_email = ""
		self.top_lvl_domain = ""
		self.snd_lvl_domain = ""
		self.local_host = ""
		self.username = ""
		self.valid = False
		self.local_host_exists = False

	def output(self):
		print("Input:", self.parsed_email, "->", "valid" if self.valid else "invalid")
		if self.valid:
			print("Username:", self.username)
			print("Local Host:", self.local_host)
			print("2nd Level Domain:", self.snd_lvl_domain)
			print("Top Level Domain:", self.top_lvl_domain)
		print()

	def mealy_actions(self, state, char):
		#print("Mealy in state", state, "with char", char)
		valid_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!#$%&'*+-/=?^_`{|}~;"

		if char != '\n':
			self.parsed_email += char

		# local_host will get all of the characters. Later we will subtract off the 
		# other parts of the domain.
		if state in [4,5,6,7,8] and (char in valid_chars or char == '.'):
			self.local_host += char

		if char == '.':
			if state in [0,1,3]:
				self.username += char
			if state == 7:
				self.snd_lvl_domain = self.top_lvl_domain
				self.top_lvl_domain = ""
				self.local_host_exists = True

		elif char in valid_chars:
			if state in [0,1,3]:
				self.username += char
			elif state in [4,5]:
				self.snd_lvl_domain += char
			elif state in [6,7,8]:
				self.top_lvl_domain += char

	def moore_actions(self, state):
		pass

	def finalize(self):
		tmp1 = self.local_host
		tmp2 = self.snd_lvl_domain + '.' + self.top_lvl_domain

		# we don't want the local_host to include the other parts of domain
		if self.local_host_exists:
			self.local_host = self.local_host[:len(tmp1) - len(tmp2)-1]
		else:
			self.local_host = ""