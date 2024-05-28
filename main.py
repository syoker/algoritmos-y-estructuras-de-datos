import os
import importlib

def clear_history():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def get_function(unit, file):
    return importlib.import_module('src.' + unit + '.' + file)

def get_list(unit):
    cont = 1
    py_files = []

    try:
        files = os.listdir('./src/' + unit)
    except:
        files = []
    
    for file in files:
        if file.endswith('.py'):
            padded_num = f'{cont:02d}.'
            py_files.append(padded_num + ' ' + file)
            cont += 1
    
    return py_files

def get_unit(unit):
    if unit in ['00 - Exit', 'Exit', 'exit', '00', '0']:
        return 'exit'
    elif unit in ['01 - Basics', 'Basics', 'basics', '01', '1']:
        return 'unit-01', '[Unit 01] Basics'
    elif unit in ['02 - Sequential Structures', 'Sequential Structures', 'sequential structures', '02', '2']:
        return 'unit-02', '[Unit 02] Sequential Structures'
    elif unit in ['03 - Basic Structured Types', 'Basic Structured Types', 'basic structured types', '03', '3']:
        return 'unit-03', '[Unit 03] Basic Structured Types'
    elif unit in ['04 - Conditional Structures', 'Conditional Structures', 'conditional structures', '04', '4']:
        return 'unit-04', '[Unit 04] Conditional Structures'
    elif unit in ['05 - Conditional Structures: Variants', 'Conditional Structures: Variants', 'conditional structures: variants', '05', '5']:
        return 'unit-05', '[Unit 05] Conditional Structures: Variants'
    elif unit in ['06 - Repetitive Structures: While Loop', 'Repetitive Structures: While Loop', 'repetitive structures: while loop', '06', '6']:
        return 'unit-06', '[Unit 06] Repetitive Structures: While Loop'
    elif unit in ['07 - Repetitive Structures: For Loop', 'Repetitive Structures: For Loop', 'repetitive structures: for loop', '07', '7']:
        return 'unit-07', '[Unit 07] Repetitive Structures: For Loop'
    elif unit in ['08 - Repetitive Structures: Variants', 'Repetitive Structures: Variants', 'repetitive structures: variants', '08', '8']:
        return 'unit-08', '[Unit 08] Repetitive Structures: Variants'
    elif unit in ['09 - Character Sequence Processing', 'Character Sequence Processing', 'character sequence processing', '09', '9']:
        return 'unit-09', '[Unit 09] Character Sequence Processing'
    elif unit in ['10 - Subproblems and Functions', 'Subproblems and Functions', 'subproblems and functions', '10']:
        return 'unit-10', '[Unit 10] Subproblems and Functions'
    elif unit in ['11 - Unit 11', 'Unit 11', '11']:
        return 'unit-11', '[Unit 11] Unit 11'
    else:
        return 'pass'

def main():
  while True:
    while_condition = 1

    clear_history()
    print('Algorithms and Data Structures')
    print('')
    print('00 - Exit')
    print('01 - Basics')
    print('02 - Sequential Structures')
    print('03 - Basic Structured Types')
    print('04 - Conditional Structures')
    print('05 - Conditional Structures: Variants')
    print('06 - Repetitive Structures: While Loop')
    print('07 - Repetitive Structures: For Loop')
    print('08 - Repetitive Structures: Variants')
    print('09 - Character Sequence Processing')
    print('10 - Subproblems and Functions')
    print('11 - Unit 11')
    print('')
    
    unit_written = input('Select a unit to open: ')
    unit_processed = get_unit(unit_written)

    if unit_processed == 'exit':
        break
    elif unit_processed == 'pass':
        while_condition = 0
        
    while while_condition == 1:
        clear_history()

        print(unit_processed[1])
        file_selected = None
        unit_files = get_list(unit_processed[0])
        
        print('')
        print('00. Back')
        for unit_file in unit_files:
            print(unit_file)
        print('')

        filename_written = input('Select a file to execute: ')
        print('')

        if filename_written in ['00 - Back', 'Back', 'back', '00', '0']:
            break

        for unit_file in unit_files:
            options = []
            options.append(unit_file)
            options.append(unit_file[4:])
            options.append(unit_file[4:-3])
            options.append(unit_file[0:2])
            if unit_file[0:2] in ['01', '02', '03', '04', '05', '06', '07', '08', '09']:
                options.append(unit_file[1])

            if filename_written in options:
                file_selected = unit_file[4:-3]
                break

        if file_selected != None:
            try:
                function_main = get_function(unit_processed[0], file_selected).main
                function_main()
            except ValueError as error:
                print('')
                print(error)
            print('')
            input('Continue...')
        

if __name__ == '__main__':
    main()
