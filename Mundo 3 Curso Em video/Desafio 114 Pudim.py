import urllib.request
try:
    url = "http://pudim.com.br/"
    siteup = urllib.request.urlopen(url).getcode()
    print("\33[1:33mConsegui acessa o site com sucesso!!\33[m") if siteup == 200 else print("Não conseguimos")
except:
    print("\33[1:31mNão foi possivel entrar no site com sucesso!\33[m")