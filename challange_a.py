def is_valid_input(bottles_count, step):
    return (
        bottles_count > 1 and bottles_count < 5 * (10 ** 4) and
        step > 1 and step < 5 * (10 ** 3)
    )
    
while EOFError: 
    bottles_count, step = map(int, input().split(" "))

    if not is_valid_input(bottles_count, step):
        print('Erro')
        exit(-1)

    boxed_bottles = [i for i in range(bottles_count)]
    
    result = []
    
    i = 0
    while boxed_bottles:
        i = (i + step - 1) % len(boxed_bottles)
        result.append(boxed_bottles.pop(i))
        
    print(result[len(result) - 1] + 1)

