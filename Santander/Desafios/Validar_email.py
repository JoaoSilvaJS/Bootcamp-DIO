# Descrição
# Uma empresa quer validar se os e-mails cadastrados pelos usuários estão no formato correto. Crie uma função que receba um e-mail e verifique se ele é válido, seguindo as regras:

# 📌 Regras para um e-mail válido:

# Deve conter o caractere "@" e um domínio, como gmail.com ou outlook.com.
# Não pode começar ou terminar com "@".
# Não pode conter espaços.
# Entrada
# Uma string contendo o e-mail a ser validado.
# Saída
# "E-mail válido" se o e-mail estiver no formato correto.
# "E-mail inválido" caso contrário.
# Exemplos
# A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

# Entrada	Saída
# usuario@gmail.com	E-mail válido
# user@outlook.com	E-mail válido
# usuario gmail.com	E-mail inválido

# email = input('Informe o e-mail: ').strip()
# def validar_email(email):
#     if '@' in email and '.' in email.split('@')[-1]:
#         if not email.startswith('@') and not email.endswith('@'):
#             if ' ' not in email:
#                 return "E-mail válido"
#     return "E-mail inválido"


email = input('Informe o e-mail: ').strip()

def validar_email(email):
    """Valida se um e-mail está no formato correto.

    Args:
        email: O e-mail a ser validado (string).

    Returns:
        "E-mail válido" se o e-mail estiver no formato correto,
        "E-mail inválido" caso contrário.
    """
    if "@" not in email:
        return "E-mail inválido"
    if email.startswith("@") or email.endswith("@"):
        return "E-mail inválido"
    if " " in email:
        return "E-mail inválido"
    partes = email.split("@")
    if len(partes) != 2 or not partes[1]:
        return "E-mail inválido"
    return "E-mail válido"
print(validar_email(email))
