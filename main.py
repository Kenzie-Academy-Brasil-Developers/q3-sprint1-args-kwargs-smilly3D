def sum_numbers(*args):
    output = 0
    for ele in args:
        output += ele
    return output

def get_multiplied_amount(multiplier, *args):
    sum_output = 0
    output=0
    for ele in args:
        sum_output += ele
    output = multiplier * sum_output
    return output 

def word_concatenator(*args):
    output = " ".join(args) 
    return output   

def inverted_word_factory(*args):
    output_palavras = []
    output_frase = []
    for ele in args:
        output_palavras.append(ele[::-1])
    r_frase = reversed(output_palavras)
    for x in r_frase:
        output_frase.append(x)
    return " ".join(output_frase)

def dictionary_separator(**kwargs):
    output_key = []
    output_values = []

    for key in kwargs:
        output_key.append(key)
        output_values.append(kwargs[key])
    return(output_key, output_values,)


def dictionary_creator(*args, **kwargs):
    output_key = []
    output_values = []
    output_args = args
    output = {}

    for key in kwargs:
        output_key.append(key)
        output_values.append(kwargs[key])
    if len(output_args) > len(output_values):
        for index, ele in enumerate(output_values):
            output[output_args[index]] = ele
        return output
    else:
        return None

def purchase_logger(**kwargs):
    dictionary = kwargs
    
    return f"Product {dictionary['name']} costs {dictionary['price']} and was bought {dictionary['quantity']}"


def world_cup_logger(country, *args):
    output = country +  " -"
    sorted_args = []
    for ele in args:
        sorted_args.append(ele)
    sorted_args.sort()    
    for index, ele in enumerate(sorted_args):
        if index == len(args)-1:
            output += f" e {ele}"
        elif index == len(args)-2:
            output += f" {ele}"
        else:
            output += f" {ele},"
    return output
               

        


