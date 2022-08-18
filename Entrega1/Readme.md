<!--CoderHouse-Python
    Desafio entregable n°7: Entrega Intermedia del Proyecto Final.
    Participantes:
        Martin Bisceglia
        Martin Goñi
    El desafío consiste en:
    >>Objetivos Generales:
    Desarrollar una WEB Django con patrón MVT subida a Github.
    >>Se debe entregar:
    Link de GitHub con el proyecto totalmente subido a la plataforma.
    Proyecto Web Django con patrón MVT que incluya:
    1.  Herencia de HTML.
    2.  Por lo menos 3 clases en models.
    3.  Un formulario para insertar datos a todas las clases de tu models.
    4.  Un formulario para buscar algo en la BD
    5.  Readme que indique el orden en el que se prueban las cosas y/o donde están las
    funcionalidades.

    Decidimos hacer una aplicación web de "Artículos para una bicicletería". 
    La app cuenta con 3 categorías: bicicletas, repuestos, e indumentaria. En cada una se puede cargar nuevos items, ver la lista de ítems, y buscar por items según un determinado criterio de búsqueda. La aplicación en si es bastante intuitiva. 

    Para comenzar la Aplicación desde la terminal de VSC:
    1°Cargamos el entorno con pipenv shell.
    2°Nos posicionamos en la carpeta "Entrega1",y corremos el comando: py manage.py runserver.
    3°Presionamos el link http://127.0.0.1:8000/ con : ctrl + botón izquierdo del mouse. 
    4°Al abrirse la aplicación se mostrará la pagina de inicio. Recorra la pagina como guste. Por cada botón se iran abriendo los templates con sus views y urls correspondientes.
    5°Para finalizar la aplicación, desde la terminal de vsc, presione: ctrl + c .

    Subir el proyecto a GitHub:
    1°Creamos un nuevo respositorio publico.
    2°Copiamos el link y lo asociamos al proyecto con: git remote add NombreUnico LinkdeGitHub
    3°Subimos el proyecto con: git push -u NombreUnico master 

    En este proyecto utilizamos solo una rama, y se trabajo en la rama master. Se realizaron varios commit:
    Escriba en terminal: git log --oneline
    Para salir presione la tecla: q

    -->