# Workshop de boas práticas em projetos de desenvolvimento

## Comandos básicos de git
Clonando o repositório do projeto
```
git clone https://github.com/elisonp/workstation.git
```

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
        
# Comandos básicos git
## Subir as atualizações feitas

Adicionar todos os arquivos atualizados
```
git add .
```

Adicionar arquivos específicos atualizados
```
git add arquivo1.txt
```

Adiciona os arquivos que sofreram alterações e validando se não há divergências
```
git commit -m 'Adicionando arquivo1.txt'
```

Subir as alterações para o repositório do git hub
```
git push
```
## Atualizar Repositório Local
```
git pull
```
