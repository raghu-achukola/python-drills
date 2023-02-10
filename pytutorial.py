BOLD_RED = '\033[1m' + '\033[91m'
BOLD_GREEN = '\033[1m'+'\033[92m'
BOLD_YELLOW = '\033[1m'+'\033[93m'
END2 = '\033[0m' + '\033[0m'
BOLD_CYAN = '\033[1m' + '\033[96m'
BOLD_YELLOW ='\033[1m' '\033[93m'



OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

def bg(x) -> str: 
    return BOLD_GREEN + repr(x) + END2
def br(x) -> str: 
    return BOLD_RED + repr(x) + END2

def bws(x) -> str:
    return BOLD_YELLOW + str(x) + END2
def bwr(x) -> str:
    return BOLD_YELLOW + repr(x) + END2
