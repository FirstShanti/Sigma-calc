box = {"ADBE":[266.84, 261.09, 261.32, 269.7, 270.98, 271.35, 271.45, 278.41, 277.93, 277.82]}


# update data with new ticker price
def box_update(ticker, price):
    box[f'{ticker}'].append(price)
    return box


#  and sigma on all timeline for a ticker
def sigma(data):
    pr_move_new = (float(data.split(' ')[1])) * 100
    ticker = data.split(' ')[0]

    #new_price = box[ticker][-1] + (box[ticker][-1] * pr_move_new)
    
    #box_update(ticker, new_price)

    price = box[ticker]
    pr_move = []
    sigma = 0

    # calculate all values of price moving on timeline
    for i in range(len(price)-1):
        val = (price[i+1] - price[i]) / price[i] * 100
        val = round(val, 2)
        pr_move.append(val)
        print(pr_move)

    avarage_price_move = round((sum(pr_move) / (len(price)-1)), 2)

    #calculate sigma
    for i in range(len(pr_move)-1):
        sigma += (pr_move[i] - avarage_price_move)**2

    
       
    if len(price) <= 30:
        sigma = (round(sigma, 2) / (len(price) - 2))**0.5
    else:
        sigma = (sigma / len(price) - 1)**0.5

    print(sigma)
        
    result = round(abs((pr_move_new-avarage_price_move)/sigma), 1)
    
    print(f'(pr_move_new-avarage_price_move)/sigma - {pr_move_new}-{avarage_price_move}/{sigma}')
    
    return result


print(sigma('ADBE 0.0258'))
