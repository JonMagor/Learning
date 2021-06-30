def test_function_return_helloworld():
    from FirstLearningCode import return_helloworld
    if return_helloworld() == 'Hello world!':
        print(f'OK! Function "return_helloworld" configured for "{return_helloworld()}".')
    else:
        print(f'NOT OK! Function "return_helloworld" not defined for "Hello world!".\n--------It is defined for "{return_helloworld()}".')

test_function_return_helloworld()