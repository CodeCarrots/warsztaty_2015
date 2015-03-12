def abc(arg):
    x = 1
    print('zewn-przed!')
    def frrgtg():
       print('wewn! -> x, arg:', x, arg)
    frrgtg()
    print('zewn-po!')

abc('hola!')
#zewn-przed!
#wewn! -> x, arg: 1 hola!
#zewn-po!

