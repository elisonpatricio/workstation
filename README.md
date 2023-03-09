# Recebimento de Mercadoria

## Criando ambiente virtual
Para criar o ambiente virutal, você vai usar o comando:
```shel
python -m venv .venv

ou

python3 -m venv .venv
```

## Utilizando o ambiente vitual
Agora que temos o `ambiente virtual` criado, iremos ativá-lo 

```shel
.\.venv\Scripts\Activate.ps1

ou

.\.venv\Scripts\activate.bat
```

## Instalando bibliotecas
Agora que estamos utilizando o ambiente isolado, iremos realizar a instalação das bibliotecas necessárias para o projeto. Para isso, instalaremos todos os pacotes necessários que estão no `arquivo requirements.txt`.
```shell
pip install -r requirements.txt
```
## Atualizando bibliotecas instaladas
Sempre que for instalado uma nova biblioteca, será necessário atualizar o arquivo requirements.txt
```shell
pip freeze > requirements.txt
```
        
