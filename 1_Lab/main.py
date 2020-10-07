from Graph import Graph
from Reader import Reader


def data_to_target():
    print('Reading dtt_file')
    reader = Reader('dtt_file')
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


def target_to_data():
    print('Reading dtt_file')
    reader = Reader('ttd_file')
    facts, rules = reader.get_facts_and_rules()
    print(f'Facts: {facts}')
    print('Rules: ')
    for rule in rules:
        print(rule)
    print()

    print('Initializing graph')
    graph = Graph(facts=facts, rules=rules)

    print('Initializing true facts')
    true_fact_names = [10, 11, 5, 6, 7]
    true_facts = [fact for fact in facts if int(fact.name) in true_fact_names]
    print(f'True facts: {true_facts}')

    print('\nStarting search')
    is_reachable = graph.target_to_data(true_facts=true_facts, target_fact=facts[0])

    print(f'Is reachable is {is_reachable}')


if __name__ == '__main__':
    # data_to_target()
    target_to_data()
