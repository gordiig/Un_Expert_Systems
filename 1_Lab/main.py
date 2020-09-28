from Graph import Graph
from Reader import Reader

if __name__ == '__main__':

    print('Reading file')
    reader = Reader('file')
    facts, rules = reader.get_facts_and_rules()
    print(f'Facts: {facts}')
    print('Rules: ')
    for rule in rules:
        print(rule)
    print()

    print('Initializing graph')
    graph = Graph(facts=facts, rules=rules)

    print('Initializing true facts')
    true_facts = [facts[6], facts[7], facts[9], facts[10]]

    print('Starting search')
    is_reachable = graph.data_to_target(true_facts=true_facts, target_fact=facts[0], with_stack=True)

    print(f'Is reachable is {is_reachable}')
