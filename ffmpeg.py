#pip install pyunpack
#pip install patool

import os
from pyunpack import Archive

os.mkdir('Descompatado')#criar uma pasta
#local do arquivo com  extenção 7z
aquivocomcpato=q.7z
Archive (aquivocomcpato).extractall('Descompatado') #extrai aquivo para a pasta ex
os.rename("ex\\ffmpeg-2022-10-27-git-e0b03331ae-full_build", "ex\\ffmpeg")#renomea pasta
os.system("setx path systemdrive\\ffmpeg\\binx") #coloca o ffmpeg como variavel de ambiente do compudor
