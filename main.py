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

def get_unit(n, units):
    counter = 0

    if n in ['00 - Exit', 'Exit', 'exit', 'EXIT', '00', '0']:
        return 'exit'

    for unit in units:
        counter += 1
        options = []
        unit_processed = f'{counter:02d} - {unit}'
        options.append(unit_processed)
        options.append(unit_processed[5:])
        options.append(unit_processed[5:].lower())
        options.append(unit_processed[5:].upper())
        options.append(unit_processed[0:2])
        if unit_processed[0:2] in ['01', '02', '03', '04', '05', '06', '07', '08', '09']:
            options.append(unit_processed[1])
        if n in options:
            return f'unit-{counter:02d}', f'[Unit {counter:02d}] {unit}'

    return 'pass'

def main():
  units = ['Basics',
  'Sequential Structures',
  'Basic Structured Types',
  'Conditional Structures',
  'Conditional Structures: Variants',
  'Repetitive Structures: While Loop',
  'Repetitive Structures: For Loop',
  'Repetitive Structures: Variants',
  'Character Sequence Processing',
  'Subproblems and Functions',
  'Functions: Detailed Implementation']

  while True:
    while_condition = 1
    counter = 0

    clear_history()
    print('Algorithms and Data Structures')
    print('')
    print('00 - Exit')
    for unit in units:
      counter += 1
      print(f'{counter:02d} - {unit}')
    print('')
    
    unit_written = input('Select a unit to open: ')
    unit_processed = get_unit(unit_written, units)

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
