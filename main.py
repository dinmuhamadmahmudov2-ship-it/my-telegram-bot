  GNU nano 9.1           main.py
import telebot
from database import init_db, add_movie, get_movie

BOT_TOKEN = "8888601157:AAE6lCskcoQd90MsCH3u6zewQf6Sq>
ADMIN_ID = 6674820076

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start_cmd(message):
    args = message.text.split()
    if len(args) > 1:
        movie_id = args[1]
        movie = get_movie(movie_id)

        if movie:
            bot.send_message(message.chat.id, "Филми >
            if movie["file_type"] == "video":
                bot.send_video(message.chat.id, movie>
            elif movie["file_type"] == "document":
                bot.send_document(message.chat.id, mo>
        else:
            bot.send_message(message.chat.id, "Бубахш>
    else:
        bot.send_message(message.chat.id, "Салом! Ба >

@bot.message_handler(content_types=['video', 'documen>
def handle_admin_movies(message):
    if message.from_user.id != ADMIN_ID:
        return

    file_id = None
    file_type = None

    if message.video:
        file_id = message.video.file_id
        file_type = "video"
    elif message.document:
        file_id = message.document.file_id
        file_type = "document"

    if file_id:
        movie_id = add_movie(file_id, file_type)
        bot_user = bot.get_me()

        share_link = f"https://t.me/{bot_user.usernam>
      
