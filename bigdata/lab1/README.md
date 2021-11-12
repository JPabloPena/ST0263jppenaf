Colocar los comandos que se usaron para subir los archivos a s3 desde hdfs
# Título
Laboratorio 1 - Bigdata

# Autor
Juan Pablo Peña

# Instalación
Es necesario tener un clúster corriendo en EMR de AWS.

Puede ver como hacerlo aquí: [Laboratorio 0](https://github.com/JPabloPena/ST0263jppenaf/blob/main/bigdata/lab0/README.md)

# Ejecución
Primero, debe acceder a _Hue_ desde el enlace que le brinda su clúster:

<img src="https://github.com/JPabloPena/ST0263jppenaf/blob/main/bigdata/assets/lab1-01.PNG"/>

Luego, en la sección de _Files_ debe crear una carpeta llamada _datasets_ y a su vez, dentro de esta, debe crear otra carpeta con el nombre de _gutenberg-small_.

<img src="https://github.com/JPabloPena/ST0263jppenaf/blob/main/bigdata/assets/lab1-02.PNG"/>

Después, en la carpeta de _gutenberg-small_ debes cargar los archivos que se encuentran en el siguiente enlance: [datasets/gutenberg-small](https://github.com/st0263eafit/st0263_20212/tree/main/bigdata/datasets/gutenberg-small)

Ahora, desde su consola debe acceder al clúster con la clave que se le otorga.

Una vez esté conectado al clúster en su consola, debe instalar _git_ y clonar el siguiente repositorio:
```
sudo yum install git
git clone https://github.com/st0263eafit/st0263_20212.git
```

Tras esto, debes acceder a la carpeta de _datasets_ del repositorio y copiarle todos los datos a tu path de _Hue_ (path en la imagen), de la siguiente manera:

<img src="https://github.com/JPabloPena/ST0263jppenaf/blob/main/bigdata/assets/lab1-03.PNG"/>

```
cd st0263_20212/bigdata/datasets/
hdfs dfs -copyFromLocal ./* /user/hadoop/datasets/
```

Ahora, en _Hue_, puedes verificar que tus datos se copiaron correctamente:

<img src="https://github.com/JPabloPena/ST0263jppenaf/blob/main/bigdata/assets/lab1-04.PNG"/>

Luego, en _Hue_, debes ir a _S3_ y crear un bucket para tus datasets, en mi caso lo nombre _datasetsjppenaf_ y dentro de este bucket debes crear un directorio que se llame _datasets_:

<img src="https://github.com/JPabloPena/ST0263jppenaf/blob/main/bigdata/assets/lab1-05.PNG"/>

Finalmente, debemos copiar los archivos de _HDFS_ a _S3_, para hacerlo debemos ejecutar el siguiente comando:
```
hadoop distcp /user/hadoop/datasets/* s3a://datasetsjppenaf/datasets/
```

Verificamos si los datos si se subieron:

<img src="https://github.com/JPabloPena/ST0263jppenaf/blob/main/bigdata/assets/lab1-06.PNG"/>

Listo!

# Bucket
```
s3://datasetsjppenaf/
```
