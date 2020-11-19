
quantidade_por_item = 0.0
sair = ()

while(sair != 'N'):
    codigo = (input('Informe o código do item pedido: '))
    quantidade = float(input('Informe a quantidade por itens: '))


    if codigo == '100':
        preco_CQ = 1.20
        quantidade_por_item = quantidade * preco_CQ
        codigo = 'Cachorro quente'
        print('O total geral do pedido do item {} em R$ {}'.format(codigo, quantidade_por_item))

    if codigo == '101':
        preco_BS = 1.30
        quantidade_por_item = quantidade * preco_BS
        codigo ='Bauru Simples'
        print('O total geral do pedido do item {} em R$ {}'.format(codigo, quantidade_por_item))

    if codigo == '102':
        preco_BO = 1.40
        quantidade_por_item = quantidade * preco_BO
        codigo = 'Bauru com ovo'
        print('O total geral do pedido do item {} em R$ {}'.format(codigo, quantidade_por_item))

    if codigo == '103':
        preco_HB = 1.50
        codigo = 'Hambúrguer'
        quantidade_por_item = quantidade * preco_HB
        print('O total geral do pedido do item {} em R$ {}'.format(codigo, quantidade_por_item))

    if codigo == '104':
        preco_CB = 1.60
        codigo = 'Cheesburguer'
        quantidade_por_item = quantidade * preco_CB
        print('O total geral do pedido do item {} em R$ {}'.format(codigo, quantidade_por_item))


    if codigo == '105':
        preco_R = 1.70
        codigo = 'Refrigerante'
        quantidade_por_item = quantidade * preco_R
        print('O total geral do pedido do item {} em R$ {}'.format(codigo, quantidade_por_item))

        sair = input('Quer informar outro produto(S/N)? ')



