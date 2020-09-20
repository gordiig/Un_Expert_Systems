from typing import List
from Fact import Fact


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

    def __eq__(self, other):
        if not isinstance(other, Rule):
            raise ValueError()
        return self.in_facts == other.in_facts and self.out_fact == other.out_fact

    def __str__(self):
        return self.rule_type.join([str(x) for x in self.in_facts]) + f' > {self.out_fact}'

    def __repr__(self):
        return str(self)
