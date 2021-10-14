
def new_file():
    print('Create new file')

def open_file():
    print('Open file')

def save_file():
    print('Save file')

def quit_app():
    print('Quit app')
    quit

if __name__ =='__main__':

    actions = {
        'n':new_file,
        'o':open_file,
        's':save_file,
        'q':quit_app
    }

    ch = input('command n-new, [-open, s-save, q-quit:')

    if ch in 'npsq':
        actions[ch]()
    else:
        print(f'Unknown command')
        print(f'command: {ch}')

x = int(input('x='))
m = x**2 if x>0 else x*2
print(f'x= {m}')
