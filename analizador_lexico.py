import ply.lex as lex

reserved = {
    'for':'FOR',
    'system':'SYSTEM',
    'out': 'OUT',
    'printl': 'PRINTL',
    'i':'VARIABLE',
}

# Definir los tokens y reglas del analizador léxico
tokens = [
    'HTML_TAG_OPEN', 'HTML_TAG_CLOSE',
    'COMMA', 'DOT',
    'SEMICOLON', 'BODY_TAG_OPEN',
    'BODY_TAG_CLOSE',
    'TITULO_TAG_OPEN',
    'TITULO_TAG_CLOSE',
    'PARRAF_TAG_OPEN',
    'PARRAF_TAG_CLOSE', 'HEAD_TAG_OPEN',
    'HEAD_TAG_CLOSE','PHP_TAG_CLOSE',
    'PHP_TAG_OPEN', 'SINGLE_QUOTE',
    'ENTER', 'STRING', 'IOSTREAM',
    'COMENT', 'INCLUDE',
    'MENOR', 'PARENT_OPEN',
    'PARENT_CLOSE', 'KEY_OPEN',
    'KEY_CLOSE', 'MAS', 'NUMERO',
    'IGUAL',
] + list(reserved.values())

# Expresiones regulares para tokens
t_HTML_TAG_OPEN = r'<html>'
t_HTML_TAG_CLOSE = r'</html>'
t_HEAD_TAG_OPEN = r'<head>'
t_HEAD_TAG_CLOSE = r'</head>'
t_BODY_TAG_OPEN = r'<body>'
t_BODY_TAG_CLOSE = r'</body>'
t_TITULO_TAG_OPEN = r'<title>'
t_TITULO_TAG_CLOSE = r'</title>'
t_PARRAF_TAG_OPEN = r'<p>'
t_PARRAF_TAG_CLOSE = r'</p>'
t_COMMA = r','
t_DOT = r'\.'
t_SEMICOLON = r';'
t_PHP_TAG_OPEN = r'<\?php'
t_SINGLE_QUOTE = r"'"
t_PHP_TAG_CLOSE = r'\?>'
t_IOSTREAM=r'<iostream>'
t_COMENT='\/\/'
t_INCLUDE=r'\#include'
t_MENOR='<'
t_PARENT_OPEN='\('
t_PARENT_CLOSE='\)'
t_KEY_OPEN='\{'
t_KEY_CLOSE='\}'

t_FOR=r'for'
t_SYSTEM=r'system'
t_OUT=r'out'
t_PRINTL=r'printl'
t_VARIABLE=r'i'

t_STRING='\"[^"]*\"'
t_MAS='\+'
t_NUMERO='[0-9]+'
t_IGUAL='='

    

def t_DETECT(t):
    r'\n'
    t.type='ENTER'
    if t.type=='ENTER':
        global numero_linea
        t.lexer.lineno += len(t.value)
        numero_linea += 1
        return t
    


# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# Variable para llevar el número de línea
numero_linea = 1

def t_error(t):
    print(f"No se pudo reconocer el token '{t.value[0]}' en la línea {numero_linea}")
    t.lexer.skip(1)

lexer = lex.lex()

def analizar_lexico(codigo):
    global numero_linea  # Asegurarse de que estás utilizando la variable global
    numero_linea = 1  # Reiniciar el número de línea a 1
    lexer.input(codigo)
    resultados = []
    for token in lexer:
        if token.type=='ENTER':
            print(f"este token {token.type} es {token.value}")
        else:
            resultados.append(f"{token.type}: {token.value} Encontrado en la linea {numero_linea}")
    return "\n".join(resultados)