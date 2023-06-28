#
#! Las rules funcionan de la siguiente manera:
#! La rule esta compuesta por 4 elementos esto no se refiere a que la rule esta compuesta por 4 cifras

# ? Rules_final = [ABCD,ABCD,ABCD]
# * Rule = A = Cuantas cifras tiene el elemento B.
# *        B = Cuantas veces se repite
# *        C = Cuantas cifras tiene el elemento D.
# *        D = la longitud del objeto en la lista

#! La lista de Rules_final se genera cuando se cifra el texto, como el texto se cifra es en una lista
#! la cual despues se unificara como una sola cadena de texto pero para despues decifrar se volvera hacer la lista
#! para saber como era la lista original se crea la Rule la cual le dara las indicaciones de como se tiene que volver a formar la lista de cifrado

# ? Ejemplo:
# * Lista de cifrada = [123,3213,212,212,122,444,1990]
# * Rules_final = [1113,1114,1413,1114]

# ? Ejemplo de generacion de Rules_final:
cifrado = [8713, 9021, 15, 2187, 10186, 8124, 3034, 9281, 3154, 9021]
rules = [
    4,
    4,
    2,
    4,
    5,
    4,
    4,
    4,
    4,
    4,
]  # * esta lista se genera con la lista cifrado, los elementos de esta lista describen la longitud de cada elemento de la lista cifrado

rules_Final = (
    []
)  # * esta lista se genera con la lista rules, y describira la Rule descrita anteriormente

contador = 1
for i in range(len(rules) - 1):
    if rules[i] == rules[i + 1]:
        contador += 1
    else:
        rules_Final.append(
            int(
                str(len(str(contador)))
                + str(contador)
                + str(len(str(rules[i])))
                + str(rules[i])
            )
        )
        contador = 1
rules_Final.append(
    int(
        str(len(str(contador)))
        + str(contador)
        + str(len(str(rules[-1])))
        + str(rules[-1])
    )
)

print("RulesFinal: ", rules_Final)  # * RulesFinal = [1214, 1112, 1114, 1115, 1514]

repeticones = 0
for i in range(len(rules_Final)):
    repeticones = int(str(rules_Final[i])[1:2])
    #! agregara la rule a la lista de cifrado
    for j in range(repeticones):
        cifrado.append(int(str(rules_Final[i])[3:]))

print("Cifrado: ", cifrado)
