import csv


def sort(s):
    '''
    Данная программа список ученных по дате
    s-список ученых и дата создания препарата
    key-первый ученый в списке
    '''
    for i in range(1, len(s)):
        key = s[i]
        j = i - 1
        while j >= 0 and key[-10:] < s[j][-10:]:
            s[j + 1] = s[j]
            j -= 1
        s[j + 1] = key
    return (s)


with open('scientist.csv', encoding='utf-8') as file:
    reader = list(csv.DictReader(file, delimiter='#'))
    s = []
    for row in reader:
        if row['preparation'] == 'Аллопуринол':
            s.append(row['ScientistName'] + '-' + row['date'])
    print('Разработчиками Аллопуринола были такие люди:')
    print(*sort(s), sep='\n')
    print(f'Оригинальный рецепт принадлежит: {sort(s)[0][:-11]}')
    for i in range(1, len(reader)):
        key = reader[i]
        j = i - 1
        while j >= 0 and key['date'] < reader[j]['date']:
            reader[j + 1] = reader[j]
            j -= 1
        reader[j + 1] = key
with open('scientist_origin.csv', 'w', encoding='utf8', newline='') as file:
    w = csv.DictWriter(file, fieldnames=['ScientistName', 'preparation', 'date', 'components'], delimiter='#')
    w.writeheader()
    w.writerows(reader)
