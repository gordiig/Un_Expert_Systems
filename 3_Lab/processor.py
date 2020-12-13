from typing import List
from fact import Fact
from rule import Rule


class Processor:
    def __init__(self, facts: List[Fact], rules: List[Rule]):
        self.working_mem: List[Fact] = facts
        self.rules: List[Rule] = rules

    def forward_chaining(self, target: Fact) -> bool:
        """
        Прямая дедукция
        :param target: Цель
        :return: Результат дедукции
        """
        # Копируем список правил и начальную рабочую память
        available_rules = [rule for rule in self.rules]
        working_mem_copy = [mem_entry for mem_entry in self.working_mem]
        i = 0
        while i < len(available_rules):
            # Проверяем подходит ли очередное правило для раскрытия
            if available_rules[i].is_rule_fits(working_mem_copy):
                if target in working_mem_copy:
                    return True
                # Если правило подошло, то убираем его из списка доступных правил, больше оно не понадобится
                del available_rules[i]
                # Идем сначала после раскрытия одного из правил
                i = -1
            i += 1
        return False
