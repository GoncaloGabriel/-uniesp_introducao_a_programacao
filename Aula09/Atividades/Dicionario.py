

dicionario = {
    1:{
        'nome': 'João',
        'email': 'n@m.com.br',
        'telefone': 99999999,
        'qualificacao': ['Direito', 'C.Contabeis']
       },
    2: {
           'nome': 'Pedro',
           'email':vvv@.com.br
           'telefone': 88888888,
           'qualificacao': {
               'graduacao': "Sistema para Internet",
               'pos': "Seguranca da Informacao"
           }
       },
    }
    print(dicionario[1]['nome'])
    print(dicionario[1]['qualificacao'][0])
    print(dicionario[2]['qualificacao']['pos'])
