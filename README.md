# thebible-db

## Instalar Python 3.8 ou Superior
Acesse o [site do Python](https://www.python.org/) e siga as orientações de instalação para o seu sistema operacional.

OBS: Caso utilze um sistema operacional Linux, saiba que na maioria das distribuições o Python já vem pré-instalado.

Confira a versão do Python através do comando:

```
python --version
```

## Instalar Visual Studio Code
Acesse o [site do Visual Studio Code](https://code.visualstudio.com/) e siga as orientações de instalação para o seu sistema operacional.

OBS: Caso utilize um sistema operacional Linux faça uso do VSCode nativo e evite usar Snap, Flatpak, por questão de compatibilidade.

## Instalar Poetry
O Poetry é uma ferramenta criada pela comunidade para facilitar o gerenciamento de dependências e de ambientes virtuais em aplicações Python.

Para instalar siga o passo a passo descrito abaixo:
```bash

sudo apt remove --purge python3-virtualenv virtualenv

sudo pip install -U launchpadlib testresources

sudo pip install -U poetry --pre

sudo pip install -U virtualenv poetry poetry-dotenv-plugin chardet requests

```
Segue neste link para entender melhor o funcionamento do Poetry.

## Habilitar integração do Poetry com Terminal (Opcional)

* Bash Support
```
poetry completions bash | sudo tee /etc/bash_completion.d/poetry.bash-completion
```

* Oh My ZSH Support
```
poetry completions bash | sudo tee /etc/bash_completion.d/poetry.bash-completion
```

## Obtendo o Código Fonte
```
poetry init
```

## Add Dependency
Example: How to add "xpto" library dependency.
```
poetry add xpto
```
