


def subgen():
    message = yield
    print(message)


g = subgen()

print(g)
