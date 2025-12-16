import smtplib
import os
from dotenv import load_dotenv


load_dotenv()

get_login = os.getenv('LOGIN')
get_token = os.getenv('TOKEN')

email_from = 'casiancik.c@gmail.com'
email_to = 'creenshow.kings@gmail.com'
friend_name = 'Artiom'
my_name = 'Catalin'
website = "https://dvmn.org/profession-ref-program/casiancik.c/4kFZ3/"

letter = """
From: {3}
To: {4}
Subject: Приглашение!
Content-Type: text/plain; charset="UTF-8"

Привет, {0}! {1} приглашает тебя на сайт {2}!

{2} — это новая версия онлайн-курса по программированию.
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя.
Как будет проходить ваше обучение на {2}?

→ Попрактикуешься на реальных кейсах.
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей.
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят.

Регистрируйся → {2}
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.""".format(friend_name, my_name, website, email_from, email_to)

letter = letter.encode("UTF-8")

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(get_login, get_token)
server.sendmail(email_from, email_to, letter)
server.quit()