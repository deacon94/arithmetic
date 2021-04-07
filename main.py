# This entrypoint file to be used in development. Start by reading README.md
import os
from arithmetic_arranger import arithmetic_arranger
from unittest import main

os.system('cls')
print('Here are the math problems...\n')
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))

print('\nHere are the solutions...\n')
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))

# Run unit tests automatically
main(module='test_module', exit=False)