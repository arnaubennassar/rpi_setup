def input_w_confirmation(input_text, confirmation_text):
    confirmation = 'nope'
    while confirmation != 'yes':
        answer = raw_input(input_text)
        confirmation = raw_input(confirmation_text + answer + '\nAre you sure? (yes/no)')
    return answer

def do_you_want(what):
    answer = 'nope'
    while answer not in['yes', 'no']:
        answer = raw_input(what + ' (yes/no)')
    if answer == 'yes': return True
    return False
