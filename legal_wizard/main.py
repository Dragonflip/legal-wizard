from download import download_documento
from requisicoes import requisitar_certidao
from utils import validate_data


def main(data):
    #valida se os dados estao corretos
    validated_data = validate_data(data)
    if validated_data:
        #requisita o documento
        n_documento = requisitar_certidao(validated_data)
        if n_documento[0]:
            #utiliza selenium para fazer o download do documento
            download_documento(n_documento)
            return True
        return False
    return False

if __name__ == '__main__':
    
    data = {
        'tipoDocumento': '3',
        'Municipio': '',
        'tipoPessoa': 'J',
        'nome': 'SUPERMERCADO NORDESTAO',
        'sexo': 'M',
        'cpf': '',
        'cnpj': '08030363003105',
        'nomeMae': '',
        'nomePai': '',
        'dataNascimento': '',
        'nacionalidade': '1',
        'estadoCivil': '1',
        'rg': '',
        'orgaoExpedidor': '',
        'ufRg': 'RS',
        'endereco': ' Avenida Prudente de Morais, 1140 Tirol Natal, RN ',
    }
    if main(data):
        print('success')
    else:
        print('fail')

