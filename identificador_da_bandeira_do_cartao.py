# Intervalos de números iniciais (BIN/IIN) das principais bandeiras de cartão

bandeiras = {
    "Visa": ["4"],
    "Mastercard": [str(i) for i in range(51, 56)] + [str(i) for i in range(2221, 2721)],
    "American Express": ["34", "37"],
    "Elo": [
        "4011", "4312", "4389", "4514", "4576", "5041", "5066", "5067", "509", "6277",
        "6362", "6363", "650", "6516", "6550"
    ],
    "Hipercard": ["606282", "3841"],
    "Diners Club": ["300", "301", "302", "303", "304", "305", "36", "38", "39"],
    "Discover": ["6011", "622126-622925", "644-649", "65"],
    "JCB": [str(i) for i in range(3528, 3590)],
    "Aura": ["50"],
    "Cabal": ["6042", "6043", "6044", "6045", "6046", "6047", "6048", "6049"]
}

tamanhos_validos = {
                "Visa": [13, 16, 19],
                "Mastercard": [16],
                "American Express": [15],
                "Elo": [16],
                "Hipercard": [13, 16, 19],
                "Diners Club": [14],
                "Discover": [16, 19],
                "JCB": [16, 19],
                "Aura": [19],
                "Cabal": [16]
            }

def identificar_bandeira(numero_cartao):
    """
    Identifica a bandeira do cartão com base no número do cartão.
    :param numero_cartao: Número do cartão (string)
    :return: Nome da bandeira ou "Desconhecida"
    """
    numero_cartao = numero_cartao.replace(" ", "").replace("-", "")
    
    for bandeira, prefixos in bandeiras.items():
        for prefixo in prefixos:
            if numero_cartao.startswith(prefixo):
                tamanho = len(numero_cartao)
                if tamanho in tamanhos_validos[bandeira]:
                    return bandeira
    return "Desconhecida"   

""""Inciando o código"""
if __name__ == "__main__":  
    numero_cartao = input("Digite o número do cartão: ")
    bandeira = identificar_bandeira(numero_cartao)
    print(f"A bandeira do cartão é: {bandeira}")    