def quando_vou_comprar(valor_car):
    poup = 10000
    mes = 0
    while poup < valor_car:
        poup = 1.07 * poup
        valor_car = 1.04 * valor_car
        mes += 1
    return mes
        
def main():
    #valor_car = float(input('Valor do carro: '))
    valor_car = float(input('Valor do carro: '))
    print(quando_vou_comprar(valor_car))
     
    #print(mes, poup, valor_car)
    
if __name__ == '__main__':
    main()

#aqui mudamos  
'''
def main():
    poup = 10000
    tax_am = 0.07
    valor_car = float(input('Valor do carro: '))
    taxa_car_am = 0.04
    mes = 0
    while poup < valor_car:
        poup = 1.07 * poup
        valor_car = 1.04 * valor_car
        mes += 1
    #print(mes, poup, valor_car)
    print(mes)
    

if __name__ == '__main__':
    main()
'''
