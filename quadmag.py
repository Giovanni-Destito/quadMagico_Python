def mostrar(a):
    for i in range(0,len(a)):
        for j in range(0,len(a[0])):
            print(a[i][j], end=' ')
    print('')
def quadMagico(a):
    cont = 0
    sp = 0
    ss = 0
    col = len(a)-1
    for i in range(0,len(a)):
        sp += a[i][i]
        ss += a[i][col]
        col -= 1
        sl = sum (a[1])
        sc = 0
        for j in range (0, len(a[0])):
            sc += a[j][i]
        
        if sl != sc:
            cont += 1 
    if sp != ss:
        cont += 1 
    if cont == 0:
        print('É um quadrado mágico!')
    else:
        print('Não é quadrado mágico!')

a = [[6,1,8],[7,5,3],[2,9,4]]
mostrar(a)
quadMagico(a)