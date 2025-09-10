# Criando uma página HTML com Python
html_code = """
<!DOCTYPE html>
<html>
<head>
    <title>Exemplo de Front-end com Python</title>
</head>
<body>
    <h1>Olá, mundo!</h1>
    <p>Esta é uma página web criada usando Python.</p>
</body>
</html>
"""
from IPython.display import HTML
HTML(html_code)
