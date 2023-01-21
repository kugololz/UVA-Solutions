zero = False

while(zero != True):
    entrada= input()
    if entrada == '0':
        zero = True
    else:
        size = 10
        while(size > 1):
            entrada = [int(x) for x in entrada]
            entrada = sum(entrada)
            entrada = str(entrada)
            entrada = [*entrada]
            size =  len(entrada)
        print(int(entrada[0]))
