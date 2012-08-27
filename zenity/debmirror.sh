#!/bin/bash
# Script interactivo para crear mirrors
# Tony 10 enero 2009
# emperor@infomed.sld.cu

# TODO 
# Leer el % para graficarlo como progressBar

clear
LOG="/tmp/mirror.log"
rm -f ${LOG} && touch ${LOG}

PKG=$(dpkg -l | egrep '(debmirror|zenity)' | awk '{print $2}' | tr '\n' ' ')
if [ "${PKG}" != "debmirror zenity zenity-common " ]; then
   {
      echo "Error: No existen alguno de los paquetes o todos";
      echo "Ejecute como root: aptitude install debmirror zenity";
      echo && sleep 1
      exit 0
   }
fi

METODO=$(zenity --list --text "Via de descarga?" --column "Opcion" --column "Protocolo" --radiolist 1 http --radiolist 2 ftp)

URL=$(zenity --entry --text "Diga DNS o IP fija del repositorio -> mirepo.midomio.cu")

DISTRO=$(zenity --list --text "Seleccione una distro para hacer espejo" --column "No." --column "Distribucion" --radiolist 1 debian --radiolist 2 debian-security --radiolist 3 debian-backports --radiolist 4 debian-multimedia --radiolist 5 ubuntu)

# Debian Way
if [ ${DISTRO} == "debian" ]; then { 
   RAMA=$(zenity --list --text "Seleccione una rama" --column "${DISTRO}" --column "rama" --checklist 1 stable --checklist 2 testing --checklist 3 unstable --separator=",")
	
   SECCION=$(zenity --list --text "Elija la secion" --column "${DISTRO}" --column "${RAMA}" --checklist 1 main --checklist 2 contrib --checklist 3 non-free --separator=",")
	}
fi

# Debian Security Way
if [ ${DISTRO} == "debian-security" ]; then {
	RAMA=$(zenity --list --text "Seleccione una rama" --column "${DISTRO}" --column "rama" --checklist 1 stable/updates --checklist 2 testing/updates --separator=",")

	SECCION=$(zenity --list --text "Elija la secion" --column "${DISTRO}" --column "${RAMA}" --checklist 1 main --separator=",")
	}
fi

# Debian Backports
if [ ${DISTRO} == "debian-backports" ]; then {
	RAMA=$(zenity --list --text "Seleccione una rama" --column "${DISTRO}" --column "rama" --checklist 1 etch-backports --separator=",")

	SECCION=$(zenity --list --text "Elija la secion" --column "${DISTRO}" --column "${RAMA}" --checklist 1 main --separator=",")
	}
fi

# Debian Multimedia
if [ ${DISTRO} == "debian-multimedia" ]; then {
	RAMA=$(zenity --list --text "Seleccione una rama" --column "${DISTRO}" --column "rama" --checklist 1 stable --checklist 2 testing --checklist 3 unstable --separator=",")

	SECCION=$(zenity --list --text "Elija la secion" --column "${DISTRO}" --column "${RAMA}" --checklist 1 main --separator=",")
	}
fi

# Ubuntu Way
if [ ${DISTRO} == "ubuntu" ]; then {
	RAMA=$(zenity --list --text "Seleccione una rama" --column "${DISTRO}" --column "rama" --checklist 1 jaunty --checklist 2 intrepid --checklist 3 hardy --checklist 4 edgy --separator=",")

	SECCION=$(zenity --list --text "Elija una seccion que necesite" --column "${RAMA}" --column "seccion" --checklist 1 main --checklist 2 restricted --checklist 3 universe --checklist 4 multiverse --separator=",") 
	}
fi

MIRROR_FILE=$(zenity --text "Ubicacion donde se guardara el mirror" --file-selection --directory)
echo

PROXY=$(zenity --list --text "Usa Proxy?" --column "Opcion" --column "Protocolo" --radiolist 1 si --radiolist 2 no)

if [ "${PROXY}" == "si" ]; then
   SET_PROX=$(zenity --entry --text "Escriba la direccion del proxy -> http://uso.un.proxy:puerto ó http://usuario:clave@uso.un.proxy:puerto")
   exec debmirror --cleanup -v --nosource --host=${URL} --root=${DISTRO} --arch=i386 --method=${METODO} --dist=${RAMA} --section=${SECCION} --ignore-missing-release --ignore-release-gpg ${MIRROR_FILE} --proxy=${SET_PROX} > ${LOG} 2>&1 &
else
   exec debmirror --cleanup -v --nosource --host=${URL} --root=${DISTRO} --arch=i386 --method=${METODO} --dist=${RAMA} --section=${SECCION} --ignore-missing-release --ignore-release-gpg ${MIRROR_FILE} > ${LOG} 2>&1 &
fi

echo "Descargando Repositorio(s) ... puede ir viendo el progreso en ${LOG}"
sleep 1

( 
   while ps aux | egrep debmirror | awk '{print $2}' > /dev/null
      do 
         FETCH_PERCENTAGE=$(tail -1 ${LOG} | egrep '^\[\ +?[0-9]?[0-9]?[0-9]+\%\]' | awk '{print $1 $2}');
         PERCENTAGE=$(echo ${FETCH_PERCENTAGE} | cut -d'[' -f 2 | cut -d% -f 1);
         if [ "$(ps aux | egrep '/usr/bin/perl -w /usr/bin/debmirror' | awk '{print $2}')" == "" ]; then 
             zenity --info --text "Se creo el repositorio satisfactoriamente";
             exit 0
         fi 
      done
      ) | zenity --progress --title "Creando repositorio ..." --text "Porciento Completado...\n|--------------|--------------|--------------|--------------|" --auto-close

