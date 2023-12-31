def get_hello_msg(user_name: str) -> str:
    return f"Привет, {user_name}! Задай мне какой-нибудь вопрос и я непременно помогу с ответом"


help_msg = (
    "/start - запустить бота\n"
    + "/help - показать все доступные команды\n"
    + "/cancel - остановить диалог с ботом\n"
)

goodbye_msg = "Был рад пообщаться! Заходи и спрашивай ещё!"
