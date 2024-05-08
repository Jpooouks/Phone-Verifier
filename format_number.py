import re

def format_number(number):
    return re.sub('\D+', '', number)

if __name__ == '__main__':
    print(format_number('+1 500 - 200 - 300'))
