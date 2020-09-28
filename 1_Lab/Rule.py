from typing import List
from Fact import Fact


class RuleError(Exception):
    pass


class Rule:
    AND = '^'
    OR = '|'

    def __init__(self, in_facts: List[Fact], out_fact: Fact, rule_type: str):
        self.in_facts = in_facts
        self.out_fact = out_fact
        self.watched = False
        if rule_type not in (self.AND, self.OR):
            raise ValueError('rule_type must be either Rule.OR, or Rule.AND')
        self.rule_type = rule_type

    @staticmethod
    def init_from_str(string: str, facts_list: List[Fact]) -> 'Rule':
        try:
            lhs, rhs = string.split('>')
        except ValueError as e:
            raise RuleError('Wrong rule format') from e
        lhs = lhs.strip()
        rhs = rhs.strip()
        if Rule.AND in lhs:
            lhs1, lhs2 = lhs.split(Rule.AND)
            rule_type = Rule.AND
        elif Rule.OR in lhs:
            lhs1, lhs2 = lhs.split(Rule.OR)
            rule_type = Rule.OR
        else:
            raise RuleError('Wrong rule format')
        lhs1 = lhs1.strip()
        lhs2 = lhs2.strip()
        try:
            lhs1_fact = [x for x in facts_list if x.name == lhs1][0]
            lhs2_fact = [x for x in facts_list if x.name == lhs2][0]
            rhs_fact = [x for x in facts_list if x.name == rhs][0]
        except IndexError as e:
            raise RuleError('Can\'t find needed fact') from e
        return Rule(in_facts=[lhs1_fact, lhs2_fact], out_fact=rhs_fact, rule_type=rule_type)

    def __eq__(self, other):
        if not isinstance(other, Rule):
            raise ValueError()
        return self.in_facts == other.in_facts and self.out_fact == other.out_fact

    def __str__(self):
        return self.rule_type.join([str(x) for x in self.in_facts]) + f' > {self.out_fact}'

    def __repr__(self):
        return str(self)
