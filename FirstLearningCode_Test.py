def test_function_saying_hello():
    from FirstLearningCode import saying_hello
    if saying_hello() == 'Hello world!':
        print(f'OK! Function "saying_hello" configured for "{saying_hello()}".')
    else:
        print(f'NOT OK! Function "saying_hello" not defined for "Hello world!".\n--------It is defined for "{saying_hello()}".')

test_function_saying_hello()