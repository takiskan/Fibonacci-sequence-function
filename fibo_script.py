def fibo(list_atr,fibo_numbers=20): #list_atr has to be empty or a fibonacci sequence list.
    count = 0
    if (len(list_atr) == 0):
        list_atr.append(0)
        list_atr.append(1)
    while count < fibo_numbers:
        list_atr.append(list_atr[len(list_atr)-1]+list_atr[len(list_atr)-2])
        count+=1
    return list_atr