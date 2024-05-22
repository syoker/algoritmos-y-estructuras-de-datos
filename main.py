import os
import importlib

def clear_history():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

unit10_exercise01 = exercise_one_module = importlib.import_module('src.unit-10.exercise-one')

def main():
  while True:
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
    print('10 - Subproblems And Functions')
    print('')
    
    unit_selected = input('Select a unit to open (the complete name or the unit number): ')

    if unit_selected == 'Exit' or unit_selected == 'exit' or unit_selected == 0:
       break
    elif unit_selected == 'Basics' or unit_selected == 'basics' or unit_selected == 1:
        clear_history()
        continue
    elif unit_selected == 'Subproblems And Functions' or unit_selected == 'subproblems and functions' or unit_selected == 10:
        clear_history()
        print('[Unit 10] Subproblems And Functions')
        print('1 - exercise-one.py')
        print('2 - exercise-two.py')

        exercise_selected = input('Select a file to execute (the filename): ')

        if exercise_selected == 'exercise-one.py':
           function_main = unit10_exercise01.main
           function_main()
           input('Continue...')
           clear_history()
    else:
        continue

if __name__ == '__main__':
    main()