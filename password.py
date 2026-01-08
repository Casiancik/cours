

def check_password(password):
	score = 0
	if any(i.isdigit() for i in password):
		score += 2
	if any(i.isalpha() for i in password) and any(i.islower() for i in password):
		score += 2
	if len(password) > 8:
		score += 2
	if any(i.isupper() for i in password):
		score += 2
	if any(not i.isalnum() for i in password):
		score += 2
	return score


def main():
	password = input('Введите пароль: ')
	print(check_password(password))


if __name__ == '__main__':
	main()
