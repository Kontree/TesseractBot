import pytesseract
import cv2
import telebot
import requests
from bot_token import BOT_TOKEN

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(content_types=['photo'])
def handle(message):
    photo = message.photo[-1]
    image_in_web = bot.get_file(photo.file_id)
    image_file = requests.get(f'https://api.telegram.org/file/bot{BOT_TOKEN}/{image_in_web.file_path}')
    with open(f'image.jpg', 'wb') as image:
        image.write(image_file.content)
    image = cv2.imread('image.jpg')
    string = pytesseract.image_to_string(image)
    bot.reply_to(message, string)


bot.infinity_polling()

