def main():
    dist_coelho = float(input('Quantos metros o coelho saiu à frente? '))    
    dist_lebre = 0
    mnts = 0 
    while dist_lebre <= dist_coelho:
        dist_coelho += 1
        dist_lebre += 10
        mnts += 1
        
    print(mnts)

if __name__ == '__main__':
    main()
