# Selecione a Longitude e Latitude das capitais de Portugal, Espanha, Itália, França e Inglaterra;
# Crie um arquivo TXT organizando as informações: País, Capital, Logintude, Latitude (modelo abaixo);
# Seu programa deve utilizar o arquivo como fonte de dados para consumir uma API;
# Utilize uma estrutura de repetição para chamar a API até o final dos dados;
# Imprima o resultado em arquivos JSON separados, e cada um deve conter o nome do país específico;  

# Discentes: João Henrique, Gonçalo Gabriel, Luiz Gonzaga e Sergio Tavares
# Sistemas para internet, Uniesp introdução a programação, P1B

de  pedidos  importar  obter 
de  despejos de importação json  

API_KEY  =  entrada ( '87ddcd5407eb23e77c015f8b1776115c' )
nome_arquivo  =  input ( "base_dados" )

dados  = []
com  aberto ( nome_arquivo , 'r' , encoding = 'UTF-8' ) como  arquivo :
    para  linha  no  arquivo . linhas de leitura ():
        linha  =  linha . substitua ( ' \n ' , '' ). substitua ( ' ' , '' )
        novo_formato  =  linha . dividir ( ',' )
        dados . append ( novo_formato )

para  informações  em  dados :    
    
    url  = f'https://api.openweathermap.org/data/2.5/weather?lat= { info [ - 15.793889 ] } &lon= { info [ - 47.882778 ] } &appid= { '87ddcd5407eb23e77c015f8b1776115c' } 
    resposta  =  obter ( url )

    se  resposta . código_status  ==  200 :
        print ( f'Criando arquivo: { info [ 0 ] } .json' )
        com  open ( info [ 0 ] +  '.json' , ' w ' , encoding = ' UTF-8' ) como  arquivo :
            dados_json  =  dumps ({ info [ 1 ]: resposta . json ()}, indent = 4 )
            arquivo . escreva ( dados_json )
 
