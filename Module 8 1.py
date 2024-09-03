# Реализуйте следующую функцию:
# add_everything_up, будет складывать числа(int, float) и строки(str)
#
# Описание функции:
# add_everything_up(a, b) принимает a и b, которые могут быть как числами(int, float),
# так и строками(str).
# TypeError - когда a и b окажутся разными типами (числом и строкой),
# то возвращать строковое представление этих двух данных вместе (в том же порядке).
# Во всех остальных случаях выполнять стандартные действия.
def add_everything_up(a, b):

    try:
         c = a + b
         return c
    except TypeError:
            type(a) != type(b)
            return ("{0}{1}".format(str(a), str(b)))

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
print(add_everything_up(5.2, 4.8))
print(add_everything_up('яблоко', 'GOLD'))
print(add_everything_up(123.457, 8))