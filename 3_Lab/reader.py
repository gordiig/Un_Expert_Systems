from typing import Tuple, List
from fact import Fact, Argument
from rule import Rule


def create_fact(fact_line: str) -> Fact:
    """
    Создание факта из строки
    :param fact_line: Строка с фактом
    :return: Факт
    """
    open_bracket_idx, close_bracket_idx = fact_line.index('('), fact_line.index(')')
    fact_name = fact_line[:open_bracket_idx].strip()
    fact_args = fact_line[open_bracket_idx + 1: close_bracket_idx].split(',')
    fact_args = [
        Argument(name=x.strip(), atype=Argument.CONSTANT if x.strip()[0].isupper() else Argument.VARIABLE)
        for x in fact_args
    ]
    ret_fact = Fact(name=fact_name, arguments=fact_args)
    return ret_fact


def read_file(filename: str) -> Tuple[List[Fact], List[Rule]]:
    """
    Чтение фактов и правил из файла
    :param filename: имя файла
    :return: Список фактов и список правил
    """
    facts = []
    rules = []
    # Читаем все из файла
    with open(filename, 'r') as f:
        file_content = f.read()
    # Разделяем факты от правил
    file_facts, file_rules = file_content.split('\n\n')
    # Инициализируем список фактов
    for file_fact in file_facts.split('\n'):
        if not file_fact:
            continue
        new_fact = create_fact(fact_line=file_fact)
        facts.append(new_fact)
    # Инициализируем список правил
    for file_rule in file_rules.split('\n'):
        if not file_rule:
            continue
        lhs, rhs = file_rule.split('->')
        target_fact = create_fact(fact_line=rhs)
        lhs_facts = [create_fact(fact_line=fact_str) for fact_str in lhs.split('^')]
        new_rule = Rule(facts=lhs_facts, result=target_fact)
        rules.append(new_rule)
    return facts, rules
