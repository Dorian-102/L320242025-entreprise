def f():
    print('Start f()')
    
    def g():
        print('Start g()')
        print('End g()')
        return

    g()

    print('End f()')
    return


f()