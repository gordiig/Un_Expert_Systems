from typing import Tuple, List
from Fact import Fact
from Rule import Rule


class Reader:
    def __init__(self, filename: str):
        self.filename = filename

    def __get_facts(self, line: str) -> List[Fact]:
        return [Fact(name=x) for x in line.split(' ')]

    def __get_rules(self, lines: List[str], facts: List[Fact]) -> List[Rule]:
        ans = []
        for line in lines:
            line = line.strip()
            if not line:
                continue
            ans.append(Rule.init_from_str(line, facts))
        return ans

    def get_facts_and_rules(self) -> Tuple[List[Fact], List[Rule]]:
        with open(self.filename, 'r') as f:
            file_content = f.read()
        splitted = file_content.split('\n')
        facts = self.__get_facts(splitted[0])
        rules = self.__get_rules(splitted[1:], facts)
        return facts, rules
