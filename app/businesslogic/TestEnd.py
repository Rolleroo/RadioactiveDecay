## This function removes extra carriage returns and splits the input \t (dict divide) and \r\n (next item)

def TestEnd(inputs):

    unformatted = inputs
    while unformatted[-2:] == "\r\n":
        unformatted = unformatted[0:-2]
    while unformatted[0:2] == "\r\n":
        unformatted = unformatted[2:]

    formatted = dict(map(lambda x: x.split('\t'), unformatted.split('\r\n')))
    return formatted