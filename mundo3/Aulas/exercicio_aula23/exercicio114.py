import urllib
import urllib.error
import urllib.request

def pudin():
    try:
        urllib.request.urlopen("https://www.youtube.com/google")
    except urllib.error.URLError:
        print("ERRO: voce esta ofline")
    else:
        print("voce esta online!")
pudin()