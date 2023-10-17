def separate_digits_with_comma(number):
    number_string = str(number)
    reversed_string = number_string[::-1]
    chunks = [reversed_string[i:i+3] for i in range(0, len(reversed_string), 3)]
    chunks.reverse()
    result = ','.join(chunks)
    return result