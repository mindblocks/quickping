
RESET = '0'

# colors options
colorNames = ('black', 'red', 'green', 'yellow',
              'blue', 'magenta', 'cyan', 'white')

# text options
optDict = {'bold': '1', 'underscore': '4',
           'blink': '5', 'reverse': '7',
           'conceal': '8'}

# foreground color range 30 to 37
foreground = {colorNames[color]: '3%s' % color for color in range(8)}

# background color range 40 to 47
background = {colorNames[color]: '4%s' % color for color in range(8)}



def colorize(text='', options=(), **kwargs):
    """
    Return your text, enclosed in ANSI graphics codes.
    Depends on the keyword arguments 'fg' and 'bg', and the contents of
    the options tuple/list.
    Return the RESET code if no parameters are given.
    Valid colors:
        'black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'
    Valid options:
        'bold'
        'underscore'
        'blink'
        'reverse'
        'conceal'
        'noreset' - string will not be auto-terminated with the RESET code
    Examples:
        colorize('hello', fg='red', bg='blue', options=('blink',))
        colorize()
        colorize('goodbye', options=('underscore',))
        print(colorize('first line', fg='red', options=('noreset',)))
        print('this should be red too')
        print(colorize('and so should this'))
        print('this should not be red')
    """
    codeList = []
    if text == '' and len(options) == 1 and options[0] == 'reset':
        return '\x1b[%sm' % RESET

    for k, v in kwargs.items():
        if k == 'fg':
            codeList.append(foreground[v])
        elif k == 'bg':
            codeList.append(background[v])
        else:
            pass

    for option in options:
        if option in optDict:
            codeList.append(optDict[option])

    if 'noreset' not in options:
        text = '%s\x1b[%sm' % (text or '', RESET)

    return '%s%s' % (('\x1b[%sm' % ';'.join(codeList)), text or '')

