import asyncio
import contextvars

# Контекстная переменная для хранения текущего языка
current_language = contextvars.ContextVar('current_language')

def set_language(language_code):
    current_language.set(language_code)

async def get_greeting():
    greetings = {
        'en': "Hello!",
        'ru': "Привет!",
        'es': "Hola!"
    }
    return greetings[current_language.get()]

async def get_error_message():
    error_messages = {
        'en': "An error occurred.",
        'ru': "Произошла ошибка.",
        'es': "Ocurrió un error."
    }
    return error_messages[current_language.get()]


async def test_user_actions(language_code):
    set_language(language_code)
    message = await get_greeting()
    error = await  get_error_message()
    print(f'{message}\n{error}')


async def main():
    await asyncio.gather(
        *[
            asyncio.create_task(
                test_user_actions(code)
            ) for code in ['en' , 'ru', 'es']
        ]
    )

asyncio.run(main())