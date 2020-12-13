from reader import read_file, create_fact
from processor import Processor


def print_facts_and_rules(facts, rules):
    print('Факты:')
    for fact in facts:
        print(f'\t{fact}')
    print()
    print('Правила:')
    for rule in rules:
        print(f'\t{rule}')


if __name__ == '__main__':
    facts, rules = read_file(filename='input')
    print_facts_and_rules(facts=facts, rules=rules)
    print()

    proc = Processor(facts=facts, rules=rules)

    while True:
        fact_line = input('Введите цель (q для выхода): ')
        # fact_line = 'haveLotOfMoney(Маша)'
        if fact_line == 'q':
            break
        fact = create_fact(fact_line=fact_line)
        result = proc.forward_chaining(target=fact)
        print(f'Результат: {result}')

    print('Пока-пока')
