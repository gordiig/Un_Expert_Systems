from Fact import Fact
from Graph import Graph
from Rule import Rule

if __name__ == '__main__':
    print('Initializing facts')
    facts = [
        Fact(name=f'{x}') for x in range(1, 12)
    ]

    print('Initializing rules')
    rules = [
        Rule(rule_type=Rule.AND, in_facts=[facts[10], facts[9]], out_fact=facts[2]),
        Rule(rule_type=Rule.AND, in_facts=[facts[4],  facts[5]], out_fact=facts[3]),
        Rule(rule_type=Rule.AND, in_facts=[facts[3],  facts[6]], out_fact=facts[1]),
        Rule(rule_type=Rule.AND, in_facts=[facts[6],  facts[7]], out_fact=facts[1]),
        Rule(rule_type=Rule.AND, in_facts=[facts[2],  facts[1]], out_fact=facts[0]),
    ]

    print('Initializing graph')
    graph = Graph(facts=facts, rules=rules)

    print('Initializing true facts')
    true_facts = [facts[2], facts[4], facts[5], facts[6], facts[7]]

    print('Starting search')
    is_reachable = graph.data_to_target(true_facts=true_facts, target_fact=facts[0], with_stack=False)

    print(f'Is reachable is {is_reachable}')
