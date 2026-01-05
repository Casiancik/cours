PASSWORD = input('Введите пароль: ')


def check_password(PASSWORD):
	score = 0
	symbols = "!@#$%^&*()-_=+"
	if any(i.isdigit() for i in PASSWORD):
		score += 2
	if any(i.isalpha() for i in PASSWORD):
		score += 2
	if any(i.isupper() for i in PASSWORD):
		score += 2
	if any(i.islower() for i in PASSWORD):
		score += 2
	if any(i in symbols for i in PASSWORD):
		score += 2
	return score


def main():
	check_password(PASSWORD)


if __name__ == '__main__':
	main()
