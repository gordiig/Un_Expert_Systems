from typing import List, Dict


class Argument:
    """
    Класс аргумента факта
    """
    CONSTANT = 'Constant'
    VARIABLE = 'Variable'

    def __init__(self, name: str, atype: str):
        self.name = name
        self.atype = atype

    def __eq__(self, other):
        if not isinstance(other, Argument):
            return False
        return self.name == other.name and self.atype == other.atype

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)


class Fact:
    """
    Класс факта
    """
    def __init__(self, name: str, arguments: List[Argument]):
        self.name = name
        self.arguments = arguments

    def __eq__(self, other):
        if not isinstance(other, Fact):
            return False
        if self.name != other.name:
            return False
        if self.arguments_cnt != other.arguments_cnt:
            return False
        for my, his in zip(self.arguments, other.arguments):
            if my != his:
                return False
        return True

    def __str__(self):
        return self.name + '(' + ', '.join([str(x) for x in self.arguments]) + ')'

    def __repr__(self):
        return str(self)

    @property
    def arguments_cnt(self):
        return len(self.arguments)

    def is_fact_fits(self, fact: 'Fact', variables: Dict[str, str]) -> bool:
        """
        Проверка совпадения факта из правила с фактом из рабочей памяти
        :param fact: Факт из рабочей памяти
        :param variables: Словарь текущих значений переменных
        :return: Результат проверки
        """
        # Сравниваем имя факта
        if self.name != fact.name:
            return False
        # Сравниваем количество аргументов
        if self.arguments_cnt != fact.arguments_cnt:
            return False
        # Сравниваем аргументы фактов
        new_variables = {k: v for k, v in variables.items()}
        for my_arg, his_arg in zip(self.arguments, fact.arguments):
            # Если констата
            if my_arg.atype == Argument.CONSTANT:
                # То достаточно сравнить имена аргументов
                if my_arg.name != his_arg.name:
                    return False
            else:   # Если переменная
                # Получаем значение переменной
                var_value = variables.get(my_arg.name)
                # Если значение есть
                if var_value:
                    # То сравниваем со значением из БЗ
                    if var_value != his_arg.name:
                        return False
                else:
                    # Иначе записываем значение
                    new_variables[my_arg.name] = his_arg.name
        for key, val in new_variables.items():
            variables[key] = val
        return True
