from typing import List, Dict, Tuple

from fact import Fact, Argument


class Rule:
    def __init__(self, facts: List[Fact], result: Fact):
        self.facts = facts
        self.result = result

    def __str__(self):
        return ' ^ '.join([str(fact) for fact in self.facts]) + ' -> ' + str(self.result)

    def __repr__(self):
        return str(self)

    def is_rule_fits(self, working_mem: List[Fact]) -> bool:
        """
        Подходит ли правило для раскрытия
        :param working_mem: Рабочая память
        :return: Результат проверки
        """
        old_mem_cnt = len(working_mem)
        used_facts_idxs = []

        # Идем в цикле пока правило однозначно не будет подходить для раскрытия, чтобы добавить в рабочую память
        # все возможные случаи раскрытия
        flag = True
        while flag:
            # Флаг повтора просмотра
            repeat_again = False
            # Для хранения пары переменная - актуализированное значение
            variables = {}
            for fact in self.facts:
                flag = False
                for i, working_mem_entry in enumerate(working_mem):
                    if i in used_facts_idxs:
                        continue
                    # Проверяем подходит ли факту из правила очередное правило из рабочей памяти
                    if fact.is_fact_fits(working_mem_entry, variables):
                        used_facts_idxs.append(i)
                        flag = True
                        break
                # Если на итерации ни один факт из рабочей памяти не подошел,
                # то само правило тоже не подходит для раскрытия
                if not flag:
                    # Флаг устанавливается, если есть установленные переменные
                    repeat_again = len(variables) > 0
                    break
            # Если нужно повторить еще раз
            if not flag and repeat_again:
                flag = True
                continue
            # Если все подошло, то актуализируем результат правила
            if flag:
                # Записываем актуализированный результат в рабочую память
                was_actualized, actualized_result = self.actualize_result(variables)
                working_mem.append(actualized_result)
                # Если не было произведено актуализации, то нет смысла просматривать остальные случаи,
                # т.к. результат не зависит от переменных
                if not was_actualized:
                    flag = False
        return old_mem_cnt != len(working_mem)

    def actualize_result(self, variables: Dict[str, str]) -> Tuple[bool, Fact]:
        """
        Актуализация результата правила (замена переменных на константы)
        :param variables: Словарь актуализированных переменных
        :return: Был ли факт актуализирован и актуализированный факт
        """
        was_actualized = False
        actualized_fact = Fact(name=self.result.name, arguments=[])
        # Идем по каждому аргументу результата
        for arg in self.result.arguments:
            # Если константа
            if arg.atype == Argument.CONSTANT:
                # То записываем без изменений
                actualized_fact.arguments.append(arg)
            else:   # Если переменная
                # Актуализируем
                actualized_argument = Argument(name=variables.get(arg.name), atype=Argument.CONSTANT)
                actualized_fact.arguments.append(actualized_argument)
                was_actualized = True
        return was_actualized, actualized_fact
