def getTalk(type="shout"):
    # Мы определяем функции прямо здесь
    def shout(word="да"):
        return word.capitalize() + "!"

    def whisper(word="да"):
        return word.lower() + "...";

    # Затем возвращаем необходимую
    if type == "shout":
        # Заметьте, что мы НЕ используем "()", нам нужно не вызвать функцию,
        # а вернуть объект функции
        return shout
    else:
        return whisper


# q = getTalk()
# print(q)
# print(q('whisper'))
# print(q())

def bread(func):
    def inner(x='123'):
        print('first')
        func(x)
        print('last')
    return inner

@bread
def sandwich(f='middle'):
    print(f)


sandwich()
# sandwich = bread(sandwich)
# sandwich('fdas')
#

