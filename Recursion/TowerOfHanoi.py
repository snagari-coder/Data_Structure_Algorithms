def towerOfHanoi(number_of_discs, src, des, aux):
    if number_of_discs == 1:
        print(f'moving disc from {src} to {des}')
    else:
        towerOfHanoi(number_of_discs - 1, src, aux, des)
        print(f'moving disc from {src} to {des}')
        towerOfHanoi(number_of_discs - 1, aux, des, src)


towerOfHanoi(3, 'src', 'des', 'aux')
