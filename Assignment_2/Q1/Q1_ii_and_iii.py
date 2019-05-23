import re

def main():
	email_regex()
	num_regex()


def email_regex():
	email = re.compile(r"jurafsky(\@|\(at\)(cs[.])|(\sat\scsli\sdot\s))stanford([.]|(\sdot\s))edu$")
	text = input('input your email to match: ')

	if (email.match(text)):
		print('successfully matched')
	else: 
		print('Not Matched')

def num_regex():
	num = re.compile(r"((\+1\-650\-)|(\(650\)\s)|(\(\+1\)\:\s650\-))723\-0293$")
	text = input('input your num to match: ')
	if (num.match(text)):
		print('successfully matched')
	else: 
		print('Not Matched')

if __name__ == '__main__':
	main()

