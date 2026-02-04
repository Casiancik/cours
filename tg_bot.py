import ptbot
import os
from pytimeparse import parse
from dotenv import load_dotenv


load_dotenv()


token = os.getenv('BOT_TOKEN')
bot = ptbot.Bot(token)


def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


def notify_progress(secs_left, author_id, message, total):
    passed = total - secs_left
    progress = render_progressbar(total, passed)
    bot.update_message(author_id, message, "Осталось времени: {} сек.\n {}".format(secs_left, progress))
    if secs_left == 0:
        bot.send_message(author_id, "Время вышло")


def wait(chat_id, question):
    seconds = parse(question)
    message_id = bot.send_message(chat_id, "Осталось времени:  сек.")
    bot.create_countdown(seconds, notify_progress, author_id=chat_id, message=message_id, total=seconds)


def main():
    bot.reply_on_message(wait)
    bot.run_bot()


if __name__ == '__main__':
    main()