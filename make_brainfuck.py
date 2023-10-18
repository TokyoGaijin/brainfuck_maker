import pyperclip

def make_code(char, nextCell = False):
	AsciiCode = ord(char)
	if AsciiCode < 100:
		tens = (AsciiCode // 10) % 10
	elif AsciiCode >= 100:
		tens = (AsciiCode // 10) % 100
	remain = AsciiCode % 10

	rounds, odds = "", ""

	for i in range(tens):
		rounds += "+"

	for i in range(remain):
		odds += "+"

	if nextCell:
		brainfuck = f">++++++++++[>{rounds}<-]>{odds}."
	else:
		brainfuck = f"++++++++++[>{rounds}<-]>{odds}."

	return brainfuck
	

def get_brainfuck(convert_string):
	brainfuck = ""
	for i in range(len(convert_string)):
		brainfuck += make_code(convert_string[i], nextCell = True)

	return brainfuck


while True:
	convert_text = input("Type your message to write Brainfuck on the line below, or '[IQUIT]' with brackets to cancel.\n")
	if convert_text == "[IQUIT]":
		break
	else:
		print(f"Here is your Brainfuck Code:\n{get_brainfuck(convert_text)}")
		choice = input("Would you like to [C/c]opy your code to the clipboard? (Anything other than C/c to cancel): ").lower()
		if choice != "c":
			break
		else:
			pyperclip.copy(get_brainfuck(convert_text))
			print("Brainfuck copied to your clipboard!")
			break