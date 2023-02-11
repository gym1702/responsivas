#Funciones extra para users

import random
import string

#genera un codigo de 6 digitos al azar
def generador_codigo(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
