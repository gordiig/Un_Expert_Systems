from typing import List
from Container import Queue, Stack, Container
from Fact import Fact
from Rule import Rule


class Graph:
    def __init__(self, facts: List[Fact], rules: List[Rule]):
        self.facts = facts
        self.rules = rules
        self.mem: List[Fact] = []
        self.rules_container: Container = None

    def __add_to_mem(self, fact: Fact):
        if fact.watched:
            return
        fact.watched = True
        self.mem.append(fact)

    def __add_to_rules_container(self, rule: Rule):
        if rule.watched:
            return
        rule.watched = True
        self.rules_container.push(rule)

    def __scan_and_add_rules_to_container(self):
        for rule in [x for x in self.rules if not x.watched]:
            if self.__can_go_trough_rule(rule):
                self.__add_to_rules_container(rule)

    def __can_go_trough_rule(self, rule: Rule) -> bool:
        for fact in rule.in_facts:
            if fact not in self.mem:
                if rule.rule_type == Rule.AND:
                    return False
            else:
                if rule.rule_type == Rule.OR:
                    return True
        return True

    def __get_rules_by_out_fact(self, fact: Fact) -> List[Rule]:
        return [rule for rule in self.rules if rule.out_fact == fact]

    # region Поиск от данных
    def data_to_target(self, true_facts: List[Fact], target_fact: Fact, with_stack: bool = True) -> bool:
        for fact in self.facts:
            fact.watched = False
        for rule in self.rules:
            rule.watched = False

        self.rules_container = Stack() if with_stack else Queue()
        self.mem = true_facts

        self.__scan_and_add_rules_to_container()
        end_fact_found = False
        ans = False
        cnt = 0
        while not end_fact_found and not self.rules_container.is_empty:
            rule = self.rules_container.pop()
            out_fact = rule.out_fact

            print(f'Iteration {cnt}')
            print(f'Memory: {self.mem}')
            print(f'Current rule: {rule}')
            print()
            cnt += 1

            if out_fact == target_fact:
                end_fact_found = ans = True
            self.__add_to_mem(out_fact)
            self.__scan_and_add_rules_to_container()
        return ans
    # endregion

    # region Поиск от цели
    def target_to_data(self, true_facts: List[Fact], target_fact: Fact) -> bool:
        return self._ttd_fact_job(true_facts=true_facts, target_fact=target_fact)

    def _ttd_fact_job(self, true_facts: List[Fact], target_fact: Fact) -> bool:
        # Если доказываемый факт в правдивых, то он доказан, возвращаем True
        if target_fact in true_facts:
            return True
        # Получаем правила, которые ведут в факт
        rules_to_target_fact = self.__get_rules_by_out_fact(fact=target_fact)
        # Рекурсивно доказываем каждое правило, и если хотя бы одно из них доказано, то доказан и факт
        for rule in rules_to_target_fact:
            if self._ttd_rule_job(rule=rule, true_facts=true_facts):
                print(rule)
                return True
        # Если не доказано ни одно из правил, то и факт не доказан
        return False

    def _ttd_rule_job(self, rule: Rule, true_facts: List[Fact]) -> bool:
        # Для каждого входящего факта в правило рекурсивно проверяем его доказываемость
        for fact in rule.in_facts:
            current_fact_is_true = self._ttd_fact_job(true_facts=true_facts, target_fact=fact)
            # Если правило типа ИЛИ, и проверяемый факт доказан, то и правило доказано
            if rule.rule_type == Rule.OR and current_fact_is_true:
                return True
            # Если правило типа И, и проверяемый факт недоказуем, то и правило недоказуемо
            elif rule.rule_type == Rule.AND and not current_fact_is_true:
                return False
        # Если правило типа И, и до сих пор не вышли, то все факты доказаны
        # Если правило типа ИЛИ, и до сих пор не вышли, то ни один из фактов не доказан
        return rule.rule_type == Rule.AND
    # endregion
