pizza_size=[8,12,16]
pizza_cost=[15,20,25]
pizza_per_slice_cost=[]

def calc_best_deal(pizza_size, pizza_cost):
    for i in len(pizza_size):
        pizza_per_slice_cost(i)=pizza_cost(i)/pizza_size(i)
    for i in len(pizza_size):
        print(pizza_per_slice_cost(i))

if __name__ == '__main__':
    calc_best_deal(pizza_size, pizza_cost)
        