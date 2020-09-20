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
