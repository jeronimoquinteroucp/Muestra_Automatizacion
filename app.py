# app.py - Archivo principal de la aplicación

def suma(numero_a, numero_b):
    """
    Retorna la suma de dos números.
    Parámetros:
        numero_a (int o float): primer número
        numero_b (int o float): segundo número
    Retorna:
        La suma de ambos valores
    """
    return numero_a + numero_b

def saludo(nombre):
    """Retorna un mensaje de saludo personalizado."""
    return f'Hola, {nombre}. Bienvenido al mundo de GitHub Actions.'

if __name__ == '__main__':
    print(saludo('Estudiante'))
    print(f'Resultado de 5 + 3 = {suma(5, 3)}')
