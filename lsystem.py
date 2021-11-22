# Set initial state of l-system
initial = "AB"

# Rules for the l-system
rules = {
	"A": "AB",
	"B": "A"
}

# define a function called "l-system" which takes an initial value, a set of rules and a generation value
def l_system(initial, rules, generation):
	# The current state of the l-system is set to the initial state, to avoid operating on the intial state.
	current = initial

	# a for loop that loops between 0 at the minimum and the value "generation" at the maximum
	for _ in range(0, generation):
		# Initialise the result with an empty string
		result = ""

		# a for loop that loops through every letter in current
		for state in current:
			# adds the letters from the rules system to the end of the result string
			result += rules.get(state, state)

		# Set current to be equal to result, the current state of the system is now equal to whatever the result of the system was prior to this point
		current = result

	# At the end of the for loop return the value of current, ending the function
	return current

# a for loop that iterates between 0 and 9 (at 10 the for loop exits before running)
for i in range(0, 10):
	# Print out the result of each iteration of the for loop using the l_system that was defined earlier
	print( "{}: {}".format(i, l_system(initial, rules, i)) )
