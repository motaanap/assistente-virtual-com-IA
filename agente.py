import json

# Carregar base de conhecimento
def carregar_base():
    with open("../data/base.json", "r", encoding="utf-8") as f:
        return json.load(f)

# Função para responder perguntas
def responder(pergunta, base):
    chave = pergunta.lower().replace(" ", "_")
    if chave in base:
        return base[chave]
    else:
        return "Desculpe, não tenho informação suficiente sobre isso."

# Programa principal
if __name__ == "__main__":
    base = carregar_base()
    print("Assistente Virtual IA pronto para conversar! 🤖")
    while True:
        pergunta = input("Você: ")
        resposta = responder(pergunta, base)
        print("Agente:", resposta)
