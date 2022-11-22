#pip install pyunpack
#pip install patool
''''Descompatado aquivo é coloca ele como variavel de ambiente para o funcionamento do pydub
    recomendado em windows = 'https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-full.7z'
'''
import os
from pyunpack import Archive

os.mkdir('Descompatado')#criar uma pasta
#Lcal do arquivo com  extenção .z
aquivocomcpato=q.7z
Archive (aquivocomcpato).extractall('Descompatado') #extrai aquivo para a pasta ex
os.rename("ex\\ffmpeg-2022-10-27-git-e0b03331ae-full_build", "ex\\ffmpeg")#renomea pasta
os.system("setx path systemdrive\\ffmpeg\\binx") #coloca o ffmpeg como variavel de ambiente do compudor


'''
TRATAMENTO DE POSSIVEIS ERROS
- Extrair aquivo
- Dentro do aquivo a pasta 'bin' contem o aquivos nessesario para conpara o funcionamento do pydub
- Copie o caminho do arquivo
- Vai em painel de controle >Pesquise criar ponto de restauração e clique >Menu superior > Proteção do sistema> abaixo'Variáveis de Ambiente'> path adicione o diretorio na lista de variaveis 

'''
