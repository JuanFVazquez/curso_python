salario_presidente = int(input("Introduce el salario del presidente: "))
print("El salario del presidente es:", salario_presidente)

salario_director = int(input("Introduce el salario del director: "))
print("El salario del director es:", salario_director)

salario_jefe_area = int(input("Introduce el salario del jefe de área: "))
print("El salario del jefe de área es:", salario_jefe_area)

salario_administrativo = int(input("Introduce el salario del administrativo: "))
print("El salario del administrativo es:", salario_administrativo)

if (salario_administrativo < salario_jefe_area) and (salario_jefe_area < salario_director) and (salario_director < salario_presidente):
    print("Los salarios tienen lógica.")
else:
    print("Los salarios no tienen lógica.")
