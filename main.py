'''
>>> JAAR
>>> 08/01/2023
>>> Price Percent Calculator
>>> Version 1
'''

'''
>>> Generates a program that will take an initial investment amount as well as a desired return and will calculate the price per share required to both make that amount as well as loose that amount with respect to the initial investment.
'''


def verify_float(string : str)->float :
    '''
    >>> Asks the user for a number. If the user enters anything other than a number, will ask the user to input a new response.
    >>> Param:  (str) string
    >>> Return: (float) Float
    '''
    while True :
        try :
            float_input = float(input(string))
        except ValueError :
            print('Invalid Response!')
        else :
            return float_input

def analytics(data: dict) :
    '''
    >>> Prints all of the information associated with the stock the user is evaluating.

    >>> Param: (dict) data
    '''
    print(f'''
    Investment Amount:   ${data["investment"]:,.2f}
    Desired Yield:       ${data["yield"]:,.2f}
    Percent Calculated:   {data["yield_percent"]:.2%}
        {data["stock"][0]}:
        Initial Price:   ${data["stock"][1]:,.2f}
        Net loss of {data["yield_percent"]:.2%} @ ${data["stock"][1] * (1 - data["yield_percent"]):,.2f}
        Net yield of {data["yield_percent"]:.2%} @ ${data["stock"][1] * (1 + data["yield_percent"]):,.2f}
    ''')

def user_input() :
    '''
    >>> Asks the user for a command. If the user inputs anything other than a valid response, will prompt them to enter a new response.

    >>> Return: (str) response
    '''
    COMMANDS = 'yaspq%'
    while True:
        try :
            response = input('Enter A Command: ').lower()
            if len(response) != 1 or response not in COMMANDS :
                raise ValueError
        except ValueError :
            print('Invalid Response!')
        else:
            return response


def update_information(response : str, data : dict)->dict :
    '''
    >>> Based on the users response will update the stock information, initial investment amount, desired yield or desired percent yield.

    >>> Param: (str) response, (dict) data
    >>> Return: (dict) data
    '''
    if response == 'a' :
        data["investment"] = verify_float("Enter new investment amount: $")
    elif response == 'y' :
        data["yield"] = verify_float("Enter desired return: $")
    elif response == 's' :
        data["stock"] = [input("What's the stocks ticker: ").upper(), verify_float("Enter price per share: $")]
    elif response == 'p' :
        data["stock"][1] = verify_float("Enter new price per share: $")
    elif response == '%' :
        data["yield"] = data["investment"] * verify_float("Enter desired percent return: ") / 100
    return data

def main() :
    data = {
        'investment' : verify_float("Enter the investment amount: $"),
        'yield' : verify_float("Enter desired return: $"),
        'stock' : [input("What's the stocks ticker: ").upper(), verify_float("Enter price per share: $")]
    }
    response = ""
    while response != 'q':
        data.update({'yield_percent' : data["yield"] / data["investment"]})
        analytics(data)
        print('''
        Change Investment Amount:  'A'     Change Stock Ticker:       'S'
        Change Desired Yield:      'Y'     Change Initial Price:      'P'
        Update percent:            '%'     Quit:                      'Q'
        ''')
        response = user_input()
        if response != 'q' :
            update_information(response, data)

if __name__  == '__main__' :
    main()