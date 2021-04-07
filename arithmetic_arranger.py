def arithmetic_arranger(problems, solve=False):

    # Confirm number of problems provided (max of 5)
    if len(problems) > 5:
        return 'Error: Too many problems.'
   
   # Initialize lines
    line1 = ''
    line2 = ''
    line3 = ''
    line4 = ''

    #Loop through each equation and confirm digits and operand
    for equations in problems:
        # Parse current equation
        equation = equations.split()

        # Check number lengths
        if len(equation[0]) > 4 or len(equation[2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        # Check Operand
        if equation[1] not in ['+', '-']:
            return 'Error: Operator must be \'+\' or \'-\'.'  

        # Check numbers only (no letters)
        try:
            # convert to numbers (for use later if solve is true)
            num1 = int(equation[0])
            num2 = int(equation[2])

            # solve if requested
            if solve:
                if equation[1] == '+':
                    ans = num1 + num2
                else:
                    ans = num1 - num2
        except:
            return 'Error: Numbers must only contain digits.'

        # Add Spacng if needed
        if len(line1) > 0:
            line1 = line1 + '    '
            line2 = line2 + '    '
            line3 = line3 + '    '
            line4 = line4 + '    '
        
        # Set up lines
        if len(equation[0]) > len(equation[2]):
            line1 = line1 + '  ' + equation[0].rjust(len(equation[0]), ' ')
            line2 = line2 + equation[1].ljust(2, ' ') + equation[2].rjust(len(equation[0]), ' ') 
            line3 = line3 + '-'.ljust(len(equation[0])+2, '-')

            if solve:
                line4 = line4 + '  ' + str(ans).rjust(len(equation[0]), ' ')
        else:
            line1 = line1 + '  ' + equation[0].rjust(len(equation[2]), ' ') 
            line2 = line2 + equation[1].ljust(2, ' ') + equation[2].rjust(len(equation[2]), ' ')
            line3 = line3 + '-'.ljust(len(equation[2])+2, '-')

            if solve:
                line4 = line4 + '  ' + str(ans).rjust(len(equation[2]), ' ')

    # Solve if needed, otherwise return the provlems
    if solve:
        return line1 + '\n' + line2 + '\n' + line3 + '\n' + line4
    else:
        return line1 + '\n' + line2 + '\n' + line3