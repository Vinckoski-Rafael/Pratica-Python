class extratorURL():
    def __init__(self,url):
        self.url= self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self,url):
        return url.strip()

    def valida_url(self):
        if self.url == "":
            raise ValueError("Sua URL esta vazia")

    def get_url_base(self):
        url_interrogacao = self.url.find("?")
        url_base = self.url[:url_interrogacao]
        return url_base

    def get_url_parametro(self):
        url_interrogacao = self.url.find('?')
        url_parametro = self.url[url_interrogacao + 1:]
        return  url_parametro

    def get_valor_dos_parametros(self,parametro_busca):

        indice_busca = self.get_url_parametro().find(parametro_busca)

        indice_valor = indice_busca + len(parametro_busca) + 1

        indice_busca_e_comercial = self.get_url_parametro().find('&', indice_valor)

        if indice_busca_e_comercial == -1:

            valor_url = self.get_url_parametro()[indice_valor:]

        else:
            valor_url = self.get_url_parametro()[indice_valor:indice_busca_e_comercial]

        return valor_url

ExtratorURL = extratorURL('bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real')
valor_quantidade=ExtratorURL.get_valor_dos_parametros('moedaOrigem')
print(valor_quantidade)