def validador(persona):
    apellido = persona[0]
    nacimiento = persona[1]
    altura = persona[2]
    nacido = nacimiento >= 2010
    aaltura = altura >= 180
    return [nacido, aaltura]