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
    def inner(*args, **kwargs ):
        print('first')
        print( inner.q )
        func(args, kwargs, inner.q )
        print('last')
    inner.q = 'test'
    # q = inner.q
    # print(inner.q)
    # print(inner.__dict__)
    return inner

# @bread
def sandwich(*args,**kwargs):
    # for i in kwargs.items():
    #     print(i)
    # w = kwargs
    print(1, args, kwargs )

# sandwich(q = '321')
# q = sandwich()
# print(q, 'opop')
# sandwich()
sandwich = bread(sandwich)
sandwich('123')
# print(sandwich)
#

