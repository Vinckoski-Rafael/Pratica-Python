url = 'bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real'

#Sanatizaçao/tratamento Da URL:
url.strip()

#Validaçao da URL
if url=="":

    raise ValueError("Sua URL esta vazia")


#Separa Base e Parametros:
url_interrogacao= url.find('?')

url_base=url[:url_interrogacao]

url_parametro=url[url_interrogacao+1:]


#Busca um valor do Parametro:
parametro_busca='moedaOrigem'

indice_busca= url_parametro.find(parametro_busca)

indice_valor= indice_busca+len(parametro_busca)+1

indice_busca_e_comercial= url_parametro.find('&',indice_valor)

if indice_busca_e_comercial==-1:

    valor_url=url_parametro[indice_valor:]

else:
    valor_url = url_parametro[indice_valor:indice_busca_e_comercial]


print(valor_url)





