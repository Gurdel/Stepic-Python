s = set()
for i in range(int(input())):
    s.add(input().lower())

mistake = set()
for i in range(int(input())):
    for word in input().lower().split():
        if word not in s:
            mistake.add(word)

print(*mistake, sep = '\n')
'''
Простейшая система проверки орфографии может быть основана на использовании списка известных слов.
Если введённое слово не найдено в этом списке, оно помечается как "ошибка".
Попробуем написать подобную систему.
На вход программе первой строкой передаётся количество dd известных нам слов, после чего 
на dd строках указываются эти слова. Затем передаётся количество ll строк текста для проверки, 
после чего ll строк текста.
Выведите уникальные "ошибки" в произвольном порядке. Работу производите без учёта регистра.

Sample Input:

4
champions
we
are
Stepik
3
We are the champignons
We Are The Champions
Stepic

Sample Output:

stepic
champignons
the
'''