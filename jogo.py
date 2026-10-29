# RPG Dungeon Quest - Desenvolvido por Douglas Gomes de Almeida
# Licenciatura em Computação - Estácio

import random
import time

class Personagem:
    def __init__(self, nome, classe, hp, ataque,pocoes):
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
            cura = 35
            self.hp = min(self.hp_maximo, self.hp + cura)
            self.pocoes -= 1
            print(f"\n🧪 {self.nome} usou uma poção e recuperou {cura} de HP! HP atual: {self.hp}/{self.hp_maximo}")
            print(f"Poções restantes: {self.pocoes}")
        else:
            print("\n❌ Você não tem mais poções de cura!")

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
    print("       ⚔️  DUNGEON QUEST: O RESGATE  ⚔️")
    print("========================================")
    
    nome = input("Digite o nome do seu herói: ")
    print("\nEscolha a sua Classe:")
    print("1. Guerreiro (Mais HP, ataque equilibrado)")
    print("2. Mago (Ataque mais forte, menos HP)")
    
    escolha = input("Opção (1 ou 2): ")
    if escolha == "2":
        heroi = Personagem(nome, "Mago", 100, 25, 3)
    else:
        heroi = Personagem(nome, "Guerreiro", 140, 18, 2)

    print(f"\n✨ {heroi.nome} o {heroi.classe} entrou na masmorra com {heroi.hp} de HP e {heroi.pocoes} poções!")
    time.sleep(1)

    # Lista de chefes/inimigos da masmorra
    inimigos_data = [
        {"nome": "Goblin Ladrão", "hp": 50, "ataque": 12, "exp": 20},
        {"nome": "Orc Guerreiro", "hp": 80, "ataque": 18, "exp": 40},
        {"nome": "Dragão das Sombras (Chefe)", "hp": 150, "ataque": 28, "exp": 100}
    ]

    for i, dados in enumerate(inimigos_data, 1):
        print(f"\n----------------------------------------")
        print(f"🚪 Entrando na Sala {i}...")
        time.sleep(1)
        
        inimigo = Inimigo(dados["nome"], dados["hp"], dados["ataque"], dados["exp"])
        print(f"⚠️ Um {inimigo.nome} selvagem apareceu para o combate!")

        while inimigo.esta_vivo() and heroi.esta_vivo():
            print(f"\n--- Status ---")
            print(f"❤️ {heroi.nome} (HP: {heroi.hp}/{heroi.hp_maximo}) | Poções: {heroi.pocoes}")
            print(f"👹 {inimigo.nome} (HP: {inimigo.hp})")
            print("--------------")
            print("1. Atacar")
            print("2. Usar Poção de Cura")
            
            acao = input("Escolha sua ação (1-2): ")

            if acao == "1":
                dano_causado = random.randint(heroi.ataque - 5, heroi.ataque + 5)
                inimigo.hp -= dano_causado
                print(f"\n🗡️ Você atacou o {inimigo.nome} e causou {dano_causado} de dano!")

                if inimigo.esta_vivo():
                    dano_recebido = random.randint(inimigo.ataque - 3, inimigo.ataque + 3)
                    heroi.hp -= dano_recebido
                    print(f"💥 O {inimigo.nome} retrucou e te causou {dano_recebido} de dano!")
                else:
                    print(f"\n🏆 Vitória! Você derrotou o {inimigo.nome}!")
            
            elif acao == "2":
                heroi.usar_pocao()
                if inimigo.esta_vivo():
                    dano_recebido = random.randint(inimigo.ataque - 3, inimigo.ataque + 3)
                    heroi.hp -= dano_recebido
                    print(f"💥 Enquanto você usava a poção, o {inimigo.nome} atacou e causou {dano_recebido} de dano!")
            else:
                print("❌ Ação inválida! Perdeu a vez.")

            if not heroi.esta_vivo():
                print("\n💀 Você foi derrotado na masmorra... Game Over!")
                return

        print(f"🎉 Sala {i} superada com sucesso!")
        time.sleep(1)

    print("\n========================================")
    print(f"🏆 PARABÉNS, {heroi.nome}! VOCÊ ZEROU A MASMORRA!")
    print("========================================")

if __name__ == "__main__":
    iniciar_jogo()
