from bs4 import BeautifulSoup as bs

def parser_civel_negativa(response):
    html_doc = response.text
    soup = bs(html_doc, 'html.parser')
    strong = soup.find_all('strong')
    if len(strong) == 1:
        n_documento = strong[0].string.strip()
        return (True, n_documento)
    return (False, None)
