import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ENDC = '\033[0m'

def print_red(string):
    print(f'{bcolors.FAIL}{string}{bcolors.ENDC}')

def print_yellow(string):
    print(f'{bcolors.WARNING}{string}{bcolors.ENDC}')

def print_green(string):
    print(f'{bcolors.OKGREEN}{string}{bcolors.ENDC}')

def print_blue(string):
    print(f'{bcolors.OKBLUE}{string}{bcolors.ENDC}')

def __test_colors__():
    print_red("RED TEXT")
    print_yellow("YELLOW TEXT")
    print_green("GREEN TEXT")
    print_blue("BLUE TEXT")


class console:
    def clear():
        command = 'clear'
        if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
            command = 'cls'
        os.system(command)

    def run_command(command):
        os.system(command)