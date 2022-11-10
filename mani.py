# pip install pydub
# pip install tqqdm
#importaçães 
import os,subprocess 
from tkinter import filedialog
from pydub import AudioSegment 
from tqdm import tqdm as q
from tqdm import tqdm  # mostra barra de carregamento durante o for

def teste():
    print('incianod teste') 
    op=input('EM SEU COMPUTADOR A DEPENDENCIA FFMPEG NAO ESTA INTALADA DESEJA INSTALAR? [S/N]').upper().split()[0]      
    if op =='s':
        from ffmpeg.ffmpeginstall import installffmpeg
        installffmpeg()

def abreaudio(input_file):
    try:
        if 'wav' in input_file:
            sound = AudioSegment.from_wav(input_file)
        if 'mp3' in input_file:
            sound =AudioSegment.from_mp3(input_file)
        elif 'ogg'in input_file :
            sound  = AudioSegment.from_ogg(input_file)
        elif 'flv'in input_file :
            sound  = AudioSegment.from_flv(input_file)
        elif 'mp4'in input_file :
            sound  = AudioSegment.from_file(input_file, "mp4")
        elif 'wma'in input_file :
            sound  = AudioSegment.from_file(input_file, "wma")
        elif 'ogg'in input_file :
            sound  = AudioSegment.from_file(input_file, "aac")
        return sound 
    except:
        print(f'eu tive esse erro {TypeError}')
        print('eu nao consegui abrir o audio para  converter')

def criar_pasta_saida( formarto_do_aquivos):
    """_summary_

    Args:
        formarto_do_aquivos (extenção de saida): formato do aquivo para qual sera convertido

    Returns:
        caminho_de_saida:retorna o caminho em que a pasta foi criada 
       
    """
    try:
        import os
        user=os.environ 
        username=user['USERNAME']#saber nome do user pc
        raiz=f'C:\\Users\\{username}\\Music' 
        caminho_de_saida=f'{raiz}\\AQUIVOS CONVERTIDOS\\{formarto_do_aquivos}\\'
        os.makedirs(caminho_de_saida)#cria pasta e subpasta com o formato de aquivo passado
        return caminho_de_saida
    except:
        return caminho_de_saida #caso a pasta ja cido criada retorana o caminho


def converteraudio(caminhocompleto,nome_exe,format_end='mp3'):
    dirExit=criar_pasta_saida( format_end)
    caminhocompleto=caminhocompleto+nome_exe[1]
    outsong=dirExit+nome_exe[0]
    try:
        song=abreaudio(caminhocompleto)
        song.export(outsong +f'.{format_end}',format=format_end)

    except:
        try:
            subprocess.call(['ffmpeg', '-i', caminhocompleto, f'converted_to_{format_end}_{outsong}.{format_end}'])
            
        except:
            print(f'NAO FOI POSIVEL COVERTER O AQUIVO {format_end[0]+format_end[1]}')
    return dirExit

def menu():
    while True:
        os.system('cls')
        path =filedialog.askdirectory()
        format_suport=['mp3','ogg','wav','amr','ogg','acc','mp4','wma']
        temp={}
        Musicaencontradas=[]
        Musicaencontradas.clear()
        while True:
            os.system('cls')
            for file in os.listdir(path):    
                for ex in format_suport:
                    if ex in file:
                        temp.clear()
                        temp['caminho']=os.path.join(path, os.path.splitext(file)[0])#caminho completo da musica 
                        temp['nome_exe']=os.path.splitext(file)#lista co nome e extençâo ([0] nome da musica,[1] extenão)
                        Musicaencontradas.append(temp.copy())
            print('='*15,'\n     MENU     \n','='*15)
            for posisao,file in enumerate(Musicaencontradas):
                print(f'{posisao} - {file["nome_exe"][0]+file["nome_exe"][1]}')
            print('='*30)
            op=input('A [CONVERTER TODAS AS MUSICAS] \n[DIGITE O NUMERO DA MUSICA QUE DESEJA CONVERTER]\nP[BUSCAR NOVA PASTA] \n999 [FECDHE O PROGRAMA]\n')
            print('='*30)
            format_suport=['mp3','ogg','wav','amr','ogg','acc','wma']

            if 'A' == op.upper():
                format_suport=['mp3','ogg','wav','amr','ogg','wma']
                for k,v in enumerate(format_suport):
                    print(f'   {k} -  {v}')
                formato_de_saida=format_suport[int(input('PARA QUAL FORMATO DEVO CONVERTER TODAS A MUSICAS? '))]
                print('INICIADO CONVERSÂO')
                barra=0
                with tqdm(total=100) as barra_progresso:
                    for posisao,file in enumerate(Musicaencontradas):
                        barra+=1
                        end=converteraudio(file['caminho'],file["nome_exe"],formato_de_saida)
                        barra_progresso.update(barra)
                    barra_progresso.update(barra-100)
                os.startfile(end)
                print('TODOS AS MUICAS LISTADAS ACIMA FORAM CONVERTIDAS')
            elif 'P' == op.upper():
                break
            else:
                op=int(op)
                for pos,key in enumerate(Musicaencontradas):
                    if pos == op:
                        for posisao,v in enumerate(format_suport):
                            print(f' {posisao} - {v}')
                        formato_de_saida=format_suport[int(input(f'PARA QUAL FORMATO DEVO CONVERTER {key["nome_exe"][0]+key["nome_exe"][1]} '))]
                        end=converteraudio(key['caminho'],key["nome_exe"],formato_de_saida)
                        for w in q(range (100)):
                            pass
                        os.startfile(end)
                        print('o aquivo foi convertido')
        if 999 == op or '999' == op :
             break

menu()      