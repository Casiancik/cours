

def check_password(password):
	score = 0
	if any(i.isdigit() for i in password):
		score += 2
	if any(i.isalpha() for i in password):
		score += 2
	if any(i.isupper() for i in password):
		score += 2
	if any(i.islower() for i in password):
		score += 2
	if any(not i.isalnum() for i in password):
		score += 2
	return score


def main():
	password = input('Введите пароль: ')
	check_password(password)


if __name__ == '__main__':
	main()
