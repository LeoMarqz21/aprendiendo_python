#comando dos Git
from colorama import init, Fore, Back, Style

Comandos_Git = {
  "git init": "creará un nuevo repositorio local GIT",
  "git init [nombre del proyecto]": "puedes crear un repositorio dentro de un nuevo directorio especificando el nombre del proyecto",
  "git clone nombredeusuario@host:/path/to/repository":"se usa para copiar un repositorio.",
  "git clone /path/to/repository":"comando básico para copiar un repositorio loca",
  "git add <ejemplo: temp.txt>":"se usa para agregar archivos al área de preparación.",
  "git commit –m “El mensaje que acompaña al commit va aquí”":"creará una instantánea de los cambios y la guardará en el directorio git.",
  "git config --global user.email tuemail@ejemplo.com":"La opción -global le dice a GIT que vas a usar ese correo electrónico para todos los repositorios locales.",
  "git config --local user.email tuemail@ejemplo.com":" Si quieres utilizar diferentes correos electrónicos para diferentes repositorios",
  "git status":"muestra la lista de los archivos que se han cambiado junto con los archivos que están por ser preparados o confirmados.",
  "git push  origin <master>":"se usa para enviar confirmaciones locales a la rama maestra del repositorio remoto.",
  "git checkout -b <branch-name>":"crea ramas y te ayuda a navegar entre ellas. Por ejemplo, el siguiente comando crea una nueva y automáticamente se cambia a ella",
  "git checkout <branch-name>":"Para cambiar de una rama a otra, sólo usa",
  "git remote add origin <host-or-remoteURL>":"Para conectar el repositorio local a un servidor remoto",
  "git remote <nombre-del-repositorio>":"borrará una conexión a un repositorio remoto especificado",
  "git branch":"sirve para listas las ramas existentes",
  "git branch -d <branch-name>":"sirve para eliminar una rama especificada",
  "git pull":"fusiona todos los cambios que se han hecho en el repositorio local con el directorio de trabajo local.",
  "git merge <branch-name>":"se usa para fusionar una rama con otra rama activa",
  "git diff":"se usa para hacer una lista de conflictos",
  "git diff --base <file-name>":"ver conflictos con respecto al archivo base",
  "git diff <source-branch> <target-branch>":"se usa para ver los conflictos que hay entre ramas antes de fusionarlas",
  "git tag 1.1.0 <instert-commitID-here>":"marca commits específicos. Los desarrolladores lo usan para marcar puntos de lanzamiento como v1.0 y v2.0.",
  "git log":"se usa para ver el historial del repositorio listando ciertos detalles de la confirmación.",
  "git reset --hard HEAD": "sirve para resetear el index y el directorio de trabajo al último estado de confirmación.",
  "git rm filename.txt":"se puede usar para remover archivos del index y del directorio de trabajo",
  "git stash":"guardará momentáneamente los cambios que no están listos para ser confirmados",
  "git show":"se usa para mostrar información sobre cualquier objeto git",
  "git fetch origin":"le permite al usuario buscar todos los objetos de un repositorio remoto que actualmente no se encuentran en el directorio de trabajo local.",
  "git ls-tree":"te permite ver un objeto de árbol junto con el nombre y modo de cada ítem, y el valor blob de SHA-1.",
  "git grep":"ación, el directorio de trabajo y en el área de preparación.",
  "gitk":"muestra la interfaz gráfica para un repositorio local.",
  "git gc":" limpiará archivos innecesarios y optimizará el repositorio local.",
  "git archive - -format=tar master":"le permite al usuario crear archivos zip o tar que contengan los constituyentes de un solo árbol de repositorio. "
  }


  
def PrintComands():
  print('\n\n')
  for i in Comandos_Git:
    print(Fore.GREEN + "Comando: " + Fore.RESET +  i , Fore.YELLOW + " Concepto: " + Fore.RESET, Comandos_Git[i])
  print('\n\n')


PrintComands()