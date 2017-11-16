class New_Creation():
	def __init__(self):
		''''''
		self.parsed_email = ""
		self.top_lvl_domain = ""
		self.snd_lvl_domain = ""
		self.local_host = ""
		self.username = ""
		self.valid = False


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


		if char == '.':
			if state in [0,1,3]:
				self.username += char
			if state == 7:
				self.local_host += self.snd_lvl_domain + char
				self.snd_lvl_domain = self.top_lvl_domain
				self.top_lvl_domain = ""

		elif char in valid_chars:
			if state in [0,1,3]:
				self.username += char
			elif state in [4,5]:
				self.snd_lvl_domain += char
			elif state in [6,7,8]:
				self.top_lvl_domain += char


	def moore_actions(self, state):
		pass
