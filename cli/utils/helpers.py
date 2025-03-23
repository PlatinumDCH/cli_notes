def parse_input(user_input: str) -> tuple[str, ...]:
    """
    Разбирает ввод пльзователя на команду и аргуметы.

    :param user_input: Строка с вводом пользователя
    :return : Кортеж, где первый елемент - комана(str),
              а остальные - аргументы (если есть)
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def parse_question_input(user_input: str) -> list[str]:
    """
    Разбирает ввод пользователя, возвразает список аргументов.

    :param user_input: Строка с вводом пользователя
    :return: Список строкЮ содержащий отдельные слова из ввода
    """
    args = user_input.split()
    return args
