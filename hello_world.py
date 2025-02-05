#!/usr/bin/env python3
import pyfiglet
from termcolor import colored

ascii_art = pyfiglet.figlet_format("Hello World")
colored_art = colored(ascii_art, "green")
print(colored_art)
