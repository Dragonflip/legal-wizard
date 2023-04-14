from download import download_documento
from requisicoes import requisitar_certidao


def validate_civel_negativa(data):
    tipo_pessoa = data.get('tipoPessoa')
    inputs = []
    if tipo_pessoa == 'J':
        inputs.append(data.get('nome'))
        inputs.append(data.get('cnpj'))
        inputs.append(data.get('endereco'))
    else:
        inputs.append(data.get('nome'))
        inputs.append(data.get('sexo'))
        inputs.append(data.get('cpf'))
        inputs.append(data.get('nomeMae'))
        inputs.append(data.get('nomePai'))
        inputs.append(data.get('dataNascimento'))
        inputs.append(data.get('nacionalidade'))
        inputs.append(data.get('estadoCivil'))
        inputs.append(data.get('rg'))
        inputs.append(data.get('orgaoExpedidor'))
        inputs.append(data.get('ufRg'))
        inputs.append(data.get('endereco'))
    #se algum campo obrigatorio nao for preenchido
    if None in inputs:
        return None
    #se todos os campos obrigatorios foram preenchidos
    return data

def validate_criminal_negativa(data):
    
    inputs = []
    inputs.append(data.get('nome'))
    inputs.append(data.get('sexo'))
    inputs.append(data.get('cpf'))
    inputs.append(data.get('nomeMae'))
    inputs.append(data.get('nomePai'))
    inputs.append(data.get('dataNascimento'))
    inputs.append(data.get('nacionalidade'))
    inputs.append(data.get('estadoCivil'))
    inputs.append(data.get('rg'))
    inputs.append(data.get('orgaoExpedidor'))
    inputs.append(data.get('ufRg'))
    inputs.append(data.get('endereco'))

    #se algum campo obrigatorio nao for preenchido
    if None in inputs:
        return None
    #se todos os campos obrigatorios foram preenchidos
    return data

def validate_data(data):
    validated_data = None
    tipo_documento = data.get('tipoDocumento')

    #se documento e certidao judicial civil negativa de primeiro grau
    if tipo_documento == '3':
        validated_data = validate_civel_negativa(data) 
    #se documento e certidao criminal negativa
    elif tipo_documento == '2':
        validated_data = validate_criminal_negativa(data)
    #documento nao especificado nos requisitos
    else:
        return None

    return validated_data

def main(data):
    #valida se os dados estao corretos
    validated_data = validate_data(data)
    if validated_data:
        #requisita o documento
        n_documento = requisitar_certidao(validated_data)
        #utiliza selenium para fazer o download do documento
        download_documento(n_documento)
        return True
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
    main(data)
