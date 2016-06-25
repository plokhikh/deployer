HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
OKYELLOW = '\033[93m'
OKRED = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
COLOR_MAP = {
    'red': OKRED,
    'green': OKGREEN
}


def colored(text, color):
    return text
    # if color in COLOR_MAP:
    #     return COLOR_MAP[color] + str(text) + ENDC
    # else:
    #     raise ValueError('Color not found')


def error(text):
    return text
    # return colored(text, 'red')


def success(text):
    # return colored(text, 'green')
    return text
