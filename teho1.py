import random
def best_profit(prices):
    n = len(prices)
    best = 0
    for i in range(n):
        for j in range(i+1,n):
            best = max(best,prices[j] - prices[i] )
    return best
 
def paras(hinnat):
    n = len(hinnat)
    erotus = 0
    for i in range(n):
        for j in range(i+1,n):          
            erotus =  (max(erotus, hinnat[j]-hinnat[i]))
    return erotus

def parasta_ennen(prices):
    n = len(prices)
    best = 0
    for i in range(n):
        min_price = min(prices[0:i + 1])
        best = max(best,prices[i] - min_price)
    return best

def parempi(prices):
    n = len(prices)
    best = 0
    min_price = prices[0]

    for i in range(n):
        if prices[i] < min_price:
            min_price = prices[i]
        best = max(best, prices[i] - min_price)
    return best    

if __name__=="__main__":
    while True:
        n = random.randint(1, 2000)
        hinnat= [random.randint(1, 100) for _ in range(n)]
    
        print(best_profit(hinnat))
        print(paras(hinnat))
        print(parasta_ennen(hinnat))
        print(parempi(hinnat))
        if parempi(hinnat) == paras(hinnat) and parempi(hinnat) == parasta_ennen(hinnat) and parasta_ennen(hinnat) == best_profit(hinnat):
            print("JEE!")
        break