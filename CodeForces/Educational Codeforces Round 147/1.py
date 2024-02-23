for t in range(int(input())):
    template = input()
    
    q_count = template.count("?")
    
    if template.find("0") == 0:
        print(0)
    elif q_count == 0:
        print(1)
    elif template.index("?") == 0:
        print((10 ** q_count) - (10 ** (q_count - 1)))
    else:
        print(10 ** q_count)