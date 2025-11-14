# Напишіть функцію під назвою calculate_rectangle_area, яка приймає два аргументи -
# довжину і ширину прямокутника, а повертає його площу. Використайте цю функцію
# для обчислення площі прямокутника зі сторонами 4 і 5 і виведіть результат.
# area = None
# area1 = int(input("Введіть 1 число: "))
# area2 = int(input("Введіть 2 число: "))
# def calculate_rectangle_area():
#     area = area1 * area2
#     print(area)
# calculate_rectangle_area()

from aiogram import Bot, Dispatcher,F
from aiogram.filters import CommandStart,Command
from aiogram.types import Message, FSInputFile, InputFile,InputMediaPhoto, InputMediaVideo
import asyncio

bot = Bot(token="8444258337:AAHFXW9oDGxCGCVP8bhJN1osn0vlTcX8RV0")
dp = Dispatcher()

@dp.message(CommandStart())
async def start(msg:Message):
    await msg.reply("Привет, \n Напиши сюда что! ")
async def main():
    await dp.start_polling(bot)

@dp.message(Command("help"))
async def help_command(msg:Message):
    help_text = """доступні команди
    /start - Начать чат
    /help - Что я умею
    /info - Информация про тебя
    """
    await msg.reply(help_text)

@dp.message(Command("info"))
async def info_command(msg:Message):
    info_text = f"""доступні команди
    Ім'я : {msg.from_user.first_name}
    Username @{msg.from_user.username}
    ID: {msg.from_user.id}
    """
    await msg.reply(info_text)

@dp.message(F.text.contains("Помоги"))
async def help_request(msg:Message):
    await msg.answer("Сам помогай себе")   
    
@dp.message(F.text.startswith("Привет"))
async def excited(msg:Message):
    await msg.answer("Ти кто такой!?")

@dp.message(Command("photo"))
async def send_photo(msg:Message):
    await msg.answer_photo(
        photo="https://play-lh.googleusercontent.com/EicDCzuN6l-9g4sZ6uq0fkpB-1AcVzd6HeZ6urH3KIGgjw-wXrrtpUZapjPV2wgi5R4",
        caption="Как говорил точно не рикролл"
    )

@dp.message(F.text.contains("Я умний"))
async def help_request(msg:Message):
    await msg.answer("Я могу поспорить")   

@dp.message(F.text.contains("Я человек"))
async def help_request(msg:Message):
    await msg.answer("А я робот")   

@dp.message(F.text.contains("Я тупой"))
async def help_request(msg:Message):
    await msg.answer("Я знаю") 

@dp.message(F.text.contains("Я милионер"))
async def send_photo(msg:Message):
    await msg.answer_photo(
        photo="https://i.ytimg.com/vi/iun2wopco18/maxresdefault.jpg",
    )

@dp.message(F.text.contains("Я бомж"))
async def send_photo(msg:Message):
    await msg.answer_photo(
        photo="https://i.pinimg.com/736x/e8/57/38/e85738cd153f28d6eab40e0f41eafc28.jpg",
    )

@dp.message(F.text.contains("Месси или Роналду"))
async def help_request(msg:Message):
    await msg.answer("Неймар") 

@dp.message(F.text.contains("Я найду тебя"))
async def send_photo(msg:Message):
    await msg.answer_photo(
        photo="https://www.meme-arsenal.com/memes/f06fc8672f70c011598723e280b21d8e.jpg",)
    

@dp.message(F.text.contains("Я лучше тебя"))
async def send_photo(msg:Message):
    await msg.answer_photo(
        photo="https://lh3.googleusercontent.com/proxy/nUD-nFW7_iPVHolHPfY-q5UZpU85JeGcgMflUw7sNPx2XF_MGIlcbQvhvSF3xBS9Y0lCNlcpJBB430h2vyEwUHZxFDAv4ZoGZZqRhKgAxA",)
    
@dp.message(F.text.contains("Ти тупой"))
async def send_photo(msg:Message):
    await msg.answer_photo(
        photo="https://i.pinimg.com/originals/d2/4e/5d/d24e5d320eb85922f6811eeea1693a67.png",)
    
@dp.message(F.text.contains("Я люблю тебя"))
async def send_photo(msg:Message):
    await msg.answer_photo(
        photo="https://lh5.googleusercontent.com/proxy/y-bBPezL5WzyrxZxR6Vt-R0GLeIla4zlcGv57BILiiURIPdSzMCAEU8KrmiU4pAdmf4Qf1sRDL5QF-VM1c-BRtrt_aCUTKD-IJUTpqTGjQ",)
    

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Зупинка ")
