'''
Задача 5:
Потребител въвежда израз от типа ((()())()).Напишете скрипт, който проверете
дали скобите са правилно отворени и затворени.
'''

def check_bracket_string(brackets_string):
    position = 0
    chech_if_brackets_state_is_correct = 0
    for c in brackets_string:
        position += 1
        if  c == ')':
            chech_if_brackets_state_is_correct -= 1
        elif c== '(':
            chech_if_brackets_state_is_correct += 1
        else:
            return (f'Incorrect sybol "{c}" on position: {position}')
        # print(f'position: {position} - char: {c} ; chech_if_brackets_state_is_correct: {chech_if_brackets_state_is_correct}')
        if  chech_if_brackets_state_is_correct < 0:
            return (f'You have incorrect closing bracket on position {position} in {brackets_string} string.')

    if chech_if_brackets_state_is_correct == 0:
        return (f'Correct bracket string: {brackets_string}')    
    else:
        return (f'You have {chech_if_brackets_state_is_correct} more openning "(" brackets in {brackets_string}')

if __name__ =="__main__":
    # input_str = str('((()())())')
    input_str = input('Enter string with open and close brackets only - "(" ")": ')
    print(check_bracket_string(input_str))




