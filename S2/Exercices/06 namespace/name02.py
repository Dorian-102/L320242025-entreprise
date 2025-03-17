def f():
    print('Start')
    print(f.__dict__)
    
    def g():
        print('Print sart g()')
        print('End g()')
        return
    print(f.__dict__)
    g()
    
    print('End f()')
    return

f()