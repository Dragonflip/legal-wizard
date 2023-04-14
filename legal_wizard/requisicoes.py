import requests
from parser import parser_civel_negativa


def requisitar_certidao(data):
    cookies = {
        'cookielawinfo-checkbox-necessary': 'yes',
        'cookielawinfo-checkbox-functional': 'no',
        'cookielawinfo-checkbox-performance': 'no',
        'cookielawinfo-checkbox-analytics': 'no',
        'cookielawinfo-checkbox-advertisement': 'no',
        'cookielawinfo-checkbox-others': 'no',
        '_ga': 'GA1.3.465567027.1681386660',
        'CookieLawInfoConsent': 'eyJuZWNlc3NhcnkiOnRydWUsImZ1bmN0aW9uYWwiOmZhbHNlLCJwZXJmb3JtYW5jZSI6ZmFsc2UsImFuYWx5dGljcyI6ZmFsc2UsImFkdmVydGlzZW1lbnQiOmZhbHNlLCJvdGhlcnMiOmZhbHNlfQ==',
        'viewed_cookie_policy': 'yes',
        'WORDPRESS': '.wordpress-dmz-2',
        '_gid': 'GA1.3.1709481464.1681479425',
        'PHPINTER-PROD': '.phpinter-prod-01',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/112.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'http://www.tjrs.jus.br',
        'Connection': 'keep-alive',
        'Referer': 'http://www.tjrs.jus.br/proc/alvara/',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'iframe',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
    }

    response = requests.post(
        'http://www.tjrs.jus.br/proc/alvara/gera_alvara.php', 
        cookies=cookies, 
        headers=headers, 
        data=data, 
        verify=False
    )
    result = parser_civel_negativa(response)
    import ipdb;ipdb.set_trace()
    print(result)
    return result
