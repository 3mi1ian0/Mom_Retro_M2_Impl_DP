import gdown
#from pyunpack import Archive para descomprimir archivo si se subio como zip

link = 'https://drive.google.com/drive/folders/1fSZd21PLtyNRrgIfaDnOUNFiNxYJZYej?usp=sharing' #link de drive
destination = '' #nombre de archivo con path
#ddestPath = '' #nombre del path a descomprimir (opcional)
gdown.download(url=link, output=destination, quiet=False, fuzzy=True) #descarga archivo
#Archive(destination).extractall(ddestPath) #descomprime archivo al path escogido (opcional)