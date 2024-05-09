import ply.yacc as yacc
from analizador_lexico import tokens #as tokens_lexer

resultado_gramatica=[]
# salto=['ENTER']

# tokens = tokens_lexer+['ENTER']

# t_enter='\n'

def p_error(p):
    if p:
        resultado3 = "Error sintactico de tipo {} en el valor {}".format(str(p.type),str(p.value))
        print(resultado3)
        resultado_gramatica.append(str(resultado3))
        return resultado3

#Definir la gramática
def p_for(p):
    '''for : FOR PARENT_OPEN contenido_for PARENT_CLOSE KEY_OPEN salto_linea salto_linea java_printl salto_linea salto_linea KEY_CLOSE'''
    if (len(p)==12):
        p[0] = 'Documento valido'

def p_contenido_for(p):
    '''contenido_for : VARIABLE IGUAL NUMERO SEMICOLON VARIABLE MENOR IGUAL NUMERO SEMICOLON VARIABLE MAS MAS'''

def p_cuerpo_for(p):
    '''cuerpo_for : java_printl'''

def p_java_printl(p):
    '''java_printl : SYSTEM DOT OUT DOT PRINTL PARENT_OPEN contenido MAS NUMERO PARENT_CLOSE SEMICOLON salto_linea'''

def p_parentesis(p):
    '''parentesis : PARENT_OPEN contenido PARENT_CLOSE'''

def p_contenido(p):
    '''contenido : TEXT
                 | empty
                 | ENTER'''
    
def p_salto_linea(p):
    '''salto_linea : ENTER
                   | empty'''

def p_texto(p):
    '''TEXT : STRING'''
    p[0] = 'Documento valido'

def p_empty(p):
    '''empty :'''
    pass

def analizar_codigo(codigo):
    resultado_gramatica.clear() # Limpia la lista global antes de iniciar la análisis
    resultado_error = None # Inicializa el resultado de error
    
    # Parsea el código y captura el resultado de error, si lo hay
    try:
        parser.parse(codigo)
        return parser.parse(codigo, resultado_gramatica)
    except Exception as e:
        resultado_error = str(e)
    
    return resultado_gramatica




#Construir el parser
parser = yacc.yacc()

# #Función para analizar la entrada
# def analizar_codigo(codigo, resultado_gramatica):
#     return parser.parse(codigo, resultado_gramatica)

# Código HTML a analizar
codigo_html = '''<html></html>'''
