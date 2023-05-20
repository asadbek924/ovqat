from aiogram import Bot,Dispatcher,executor,types
import logging
from bot import taom_qaytar

logging.basicConfig(level=logging.INFO)

bot=Bot(token="5889192380:AAHKWwmzVazPxGqmPal31X7loYYrMKZs7NE")
dp=Dispatcher(bot)

@dp.message_handler(commands="start")
async def started(message:types.Message):
    await message.reply(f"Salom {message.chat.full_name}.\nTaom hohliysanmi?\n/taom ni bos!!!!")

@dp.message_handler(commands="taom")
async def taom(message:types.Message):
    meals=taom_qaytar()
    nomi=meals['strMeal']
    hudud=meals['strArea']
    categoriya=meals['strCategory']
    rasm=meals['strMealThumb']
    video=meals['strYoutube']

    text=f"🍱 {nomi}\n🗺 {hudud} {categoriya} taomi\n🎞Tayyorlanish usuli ⤵️⤵️⤵️"
    await message.answer_photo(photo=rasm,caption=text)
    await message.answer(video)

if __name__=="__main__":
    executor.start_polling(dp,skip_updates=False)