class New_Creation():
	def __init__(self):
		''''''
		self.parsed_date = ""
		self.year = 0
		self.month = 0
		self.day = 0
		self.valid = False
		self.last_state = 0

	def output(self):
		print("Input:", self.parsed_date, "->", "valid" if self.valid else "invalid")
		if self.valid:
			print("Year:", self.year)
			print("Month:", self.month)
			print("Day:", self.day)
		print()

	def mealy_actions(self, state, char):
		#print(self.last_state, "->", state)
		self.last_state = state
		self.parsed_date += char
		# Settle year
		if char in "0123456789":
			if state == 0 or state == 38:
				self.year += int(char) * 1000
			elif state == 28  or state == 24:
				self.year += int(char) * 100
			elif state == 29  or state == 25:
				self.year += int(char) * 10
			elif state == 30  or state == 26:
				self.year += int(char)

		# Settle month
		if state == 2 and char in "Nn":
			self.month = 1
		elif state == 5 and char in "Bb":
			self.month = 2
		elif state == 7 and char in "Rr":
			self.month = 3
		elif state == 10 and char in "Rr":
			self.month = 4
		elif state == 7 and char in "Yy":
			self.month = 5
		elif state == 3 and char in "Nn":
			self.month = 6
		elif state == 3 and char in "Ll":
			self.month = 7
		elif state == 9 and char in "Gg":
			self.month = 8
		elif state == 12 and char in "Pp":
			self.month = 9
		elif state == 14 and char in "Tt":
			self.month = 10
		elif state == 16 and char in "Vv":
			self.month = 11
		elif state == 18 and char in "Cc":
			self.month = 12
		elif state == 32 and char in "0123456789":
			self.month += int(char) * 10
		elif state == 33 and char in "0123456789":
			self.month += int(char)

		# Settle day
		if char in "0123456789":
			if state == 20 or state == 36:
				self.day += int(char)
			elif state == 21:
				self.day = self.day * 10 + int(char)
			if state == 35:
				self.day += int(char) * 10

	def moore_actions(self, state):
		pass