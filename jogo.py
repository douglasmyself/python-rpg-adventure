# RPG Dungeon Quest - Desenvolvido por Douglas Gomes de Almeida
# Licenciatura em Computação - Estácio

import random
import time

class Personagem:
    def __init__(self, nome, classe, hp, ataque, pocoes):
        self.nome = nome
        self.classe = classe
        self.hp = hp
        self.hp_maximo = hp
        self.ataque = ataque
        self.pocoes = pocoes

    def esta_vivo(self):
        return self.hp > 0

    def usar_pocao(self):
        if self.pocoes > 0:
            cura = 65
            self.hp = min(self.hp_maximo, self.hp + cura)
            self.pocoes -= 1
            print(f"\n🧪 {self.nome} usou um Kit Médico e recuperou {cura} de Vida! Vida atual: {self.hp}/{self.hp_maximo}")
            print(f"Kit Médico restantes: {self.pocoes}")
        else:
            print("\n❌ Você não tem mais nenhum Kit Médico!")

class Inimigo:
    def __init__(self, nome, hp, ataque, experiencia):
        self.nome = nome
        self.hp = hp
        self.ataque = ataque
        self.experiencia = experiencia

    def esta_vivo(self):
        return self.hp > 0

def iniciar_jogo():
    print("========================================")
    print("       ⚔️  O SOBREVIVENTE  ⚔️")
    print("========================================")
    
    nome = input("Digite o nome do seu herói: ")
    print("\nEscolha a sua Classe:")
    print("1. Guerreiro (Mais Vida, ataque equilibrado)")
    print("2. Mago (Ataque mais forte, menos Vida)")
    
    escolha = input("Opção (1 ou 2): ")
    if escolha == "2":
        heroi = Personagem(nome, "Mago", 100, 25, 3)
    else:
        heroi = Personagem(nome, "Guerreiro", 140, 18, 2)

    print(f"\n✨ {heroi.nome} o Seu {heroi.classe} entrou na Masmorra com {heroi.hp} de Vida e {heroi.pocoes} Kits Médico!")
    time.sleep(1)

    # Lista de chefes/inimigos da masmorra
    inimigos_data = [
        {"nome": "Ladrão", "hp": 50, "ataque": 12, "exp": 20},
        {"nome": "Trapaceiro", "hp": 80, "ataque": 18, "exp": 40},
        {"nome": "Dragão das Sombras (Chefe)", "hp": 100, "ataque": 28, "exp": 100}
    ]

    for i, dados in enumerate(inimigos_data, 1):
        print(f"\n----------------------------------------")
        print(f"🚪 Entrando na Sala {i}...")
        time.sleep(1)
        
        inimigo = Inimigo(dados["nome"], dados["hp"], dados["ataque"], dados["exp"])
        print(f"⚠️  Um {inimigo.nome} selvagem apareceu para o combate!")

        while inimigo.esta_vivo() and heroi.esta_vivo():
            print(f"\n--- Status ---")
            print(f"❤️  {heroi.nome} (Vida: {heroi.hp}/{heroi.hp_maximo}) | Kit Médico: {heroi.pocoes}")
            print(f"👹 {inimigo.nome} (Vida: {inimigo.hp})")
            print("--------------")
            print("1. Atacar")
            print("2. Usar Kit Médico")
            
            acao = input("Escolha sua ação (1-2): ")

            if acao == "1":
                dano_causado = random.randint(heroi.ataque - 5, heroi.ataque + 5)
                inimigo.hp -= dano_causado
                print(f"\n🗡️ Você atacou o {inimigo.nome} e causou {dano_causado} de dano!")

                if inimigo.esta_vivo():
                    dano_recebido = random.randint(inimigo.ataque - 3, inimigo.ataque + 3)
                    heroi.hp -= dano_recebido
                    print(f"💥 O {inimigo.nome} revidou e te causou {dano_recebido} de dano!")
                else:
                    print(f"\n🏆 Vitória!🏆 Você derrotou o {inimigo.nome}!")
            
            elif acao == "2":
                heroi.usar_pocao()
                if inimigo.esta_vivo():
                    dano_recebido = random.randint(inimigo.ataque - 3, inimigo.ataque + 3)
                    heroi.hp -= dano_recebido
                    print(f"💥 Enquanto você usava o Kit Médico, o {inimigo.nome} atacou e causou {dano_recebido} de dano!")
            else:
                print("❌ Ação inválida! Perdeu a vez.")

            if not heroi.esta_vivo():
                print("\n💀 Você foi derrotado na masmorra... Game Over!")
                return

        print(f"🎉 Sala {i} superada com sucesso!")
        time.sleep(1)

    print("\n========================================")
    print(f"🏆 PARABÉNS🏆 {heroi.nome}! VOCÊ ZEROU A MASMORRA!")
    print("========================================")

if __name__ == "__main__":
    iniciar_jogo()
