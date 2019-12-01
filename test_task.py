from get_data import data

# update data with new ticker price
def box_update(ticker, price):
    data[f'{ticker}'].append(price)
    return data


#  and sigma on all timeline for a ticker
def sigma(query):
    ticker = query.split(' ')[0]

    #new_price = data[ticker][-1] + (data[ticker][-1] * pr_move_new)
    #box_update(ticker, new_price)

    price = data[ticker][::-1]
    pr_move = []
    sigma = 0

    # calculate all values of price moving on timeline
    for i in range(len(price)-1):
        val = (price[i+1] / price[i] - 1) * 100
        val = round(val, 2)
        pr_move.append(val)

    avarage_price_move = round((sum(pr_move) / (len(price)-1)), 2)

    # calculate sigma
    for i in range(len(pr_move)):
        sigma += (pr_move[i] - avarage_price_move)**2
    if len(price) <= 30:
        sigma = (round(sigma, 2) / (len(price) - 2))**0.5
    else:
        sigma = (round(sigma, 2) / (len(price) - 1))**0.5
    
    # calculate result 
    pr_move_new = (float(query.split(' ')[1])) * 100
    result = float(round(abs((pr_move_new-avarage_price_move)/sigma), 1))
    
    return result


print(sigma('ADBE 0.0258'))
