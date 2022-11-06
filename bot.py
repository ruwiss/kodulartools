def main(dp):
    @dp.message_handler(commands=['start', 'help'])
    async def send_welcome(message: types.Message):
        await message.reply(
            "🇹🇷 Hello, I'm a bot created by <b>Ruwis</b> that can convert dynamic views to <b>Json</b> file format for <code>Kodular</code> and <code>App Inventor</code> platforms. Send me an <i>ais</i> file or if you want to convert hex colors for <b>Kodular</b>, you can convert them with the <code>/color hexcolor</code>")

    @dp.message_handler(content_types=types.ContentType.DOCUMENT)
    async def fileHandle(message: types.Message):
        try:
            if document := message.document:
                await message.answer("Converting..")
                extension = message['document']['file_name'].split(".")[-1]
                if extension == "ais":
                    path = f"projeler/{random.randint(45, 500)}_{message.document.file_name}"
                    await document.download(
                        destination_file=path)
                    author = message["from"]["username"]
                    await bot.send_document(message.chat.id, document=open(Convert(path, author), 'rb'))
                else:
                    await message.answer("Please send a file with the .ais extension.")
        except():
            pass
    @dp.message_handler(commands=['color'])
    async def fileHandle(message: types.Message):
        hex = message.text.replace("/color ", "").replace("#","")
        await message.answer(f"<code>{(int(hex, 16) * -1 + 16777216) * -1}</code>")

if __name__ == '__main__':
    import random
    from aiogram import Bot, Dispatcher, executor, types
    from schema import Convert, Generate
    print("File waiting..")
    API_TOKEN = "5759698288:AAHRkobfqXgop26mbJ7cqBwdJU6GdJXdNPY"
    bot = Bot(token=API_TOKEN, parse_mode="html")
    dp = Dispatcher(bot)
    main(dp)
    executor.start_polling(dp, skip_updates=True)
