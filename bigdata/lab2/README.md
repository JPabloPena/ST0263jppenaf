# Título
Laboratorio 2 - Bigdata

# Autor
Juan Pablo Peña F.

# Instalación
Para poder ejecutar los programas debe instalar _git_ y clonar este repositorio:
```
sudo yum install git
git clone https://github.com/JPabloPena/ST0263jppenaf.git
```
Luego, debe instalar _MRJob_, para hacerlo ejecute:
```
sudo pip3 install mrjob
```

# Ejecución
Para ejecutar los programas primero acceda a la siguiente ruta del repositorio:
```
cd ST0263jppenaf/bigdata/lab2/dian/ 
```
Ahora, para ejecutar los programas haga el comando del programa que desee ejecutar:

## 1. El salario promedio por Sector Económico (SE)
```
python3 salario-se.py ../../otros/dataempleados.txt
```
## 2. El salario promedio por Empleado
```
python3 salario-empleado.py ../../otros/dataempleados.txt
```
## 3. Número de SE por Empleado que ha tenido a lo largo de la estadística
```
python3 numero-se-emp.py ../../otros/dataempleados.txt
```
