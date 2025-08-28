import random
import string

def gerar_chave_de_licenca():
  """Gera uma chave de licença no formato XXXX-XXXX-XXXX."""
  def gerar_bloco():
    caracteres = string.ascii_uppercase + string.digits
    return ''.join(random.choice(caracteres) for _ in range(4))

  bloco1 = gerar_bloco()
  bloco2 = gerar_bloco()
  bloco3 = gerar_bloco()

  return f"{bloco1}-{bloco2}-{bloco3}"

# Exemplo: gera uma chave de licença
chave = gerar_chave_de_licenca()
print(chave)