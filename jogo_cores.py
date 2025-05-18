
import random

# --- Configurações do Jogo ---
CORES_DISPONIVEIS = ["amarelo", "azul", "branco", "verde", "vermelho"]
NUM_CORES_ESCOLHER = 3
MAX_TENTATIVAS = 5

def jogar_adivinhacao_cores_ordem():
    # App (Jogador 2) escolhe as cores secretas aleatoriamente
    cores_secretas = random.sample(CORES_DISPONIVEIS, NUM_CORES_ESCOLHER)
    print("Eu (Jogador 2) escolhi minhas {} cores secretas em uma ordem específica!".format(NUM_CORES_ESCOLHER))
    # print("(Para teste: as cores secretas são:", ", ".join(cores_secretas), ")") # Linha para mostrar as cores secretas para teste
    print("\nJogador 1, tente adivinhar as cores secretas na ordem correta!")

    for tentativa in range(1, MAX_TENTATIVAS + 1):
        print(f"\nTentativa {tentativa}:")
        palpite = []
        while len(palpite) < NUM_CORES_ESCOLHER:
            cor_palpite = input(f"Digite sua cor {len(palpite) + 1}: ").lower()
            if cor_palpite in CORES_DISPONIVEIS and cor_palpite not in palpite:
                palpite.append(cor_palpite)
            elif cor_palpite not in CORES_DISPONIVEIS:
                print("Cor inválida. Escolha entre:", ", ".join(CORES_DISPONIVEIS))
                continue  # Adicionado para voltar ao início do loop while
            else:
                print("Você já palpitou essa cor nesta tentativa. Tente outra.")

        acertos_ordem = 0
        acertos_cor = 0
        erros = 0

        for i in range(NUM_CORES_ESCOLHER):
            if palpite[i] == cores_secretas[i]:
                acertos_ordem += 1
            elif palpite[i] in cores_secretas:
                acertos_cor += 1
            else:
                erros += 1

        print(f"Você acertou {acertos_ordem} cor(es) na posição correta.")
        print(f"Você acertou {acertos_cor} cor(es) mas na posição incorreta.")
        print(f"Você errou {erros} cor(es).")

        if acertos_ordem == NUM_CORES_ESCOLHER:
            print("(As cores secretas são:", ", ".join(cores_secretas), ")")
            print("\nParabéns, Jogador 1! Você adivinhou as cores secretas e a ordem!")
            return True  # Indica que o jogador venceu e sai da função
        elif tentativa == MAX_TENTATIVAS:
            print("\nFim das tentativas! As cores secretas eram:", ", ".join(cores_secretas))
            return False # Indica que o jogador perdeu

if __name__ == "__main__":
    while True:
        resultado = jogar_adivinhacao_cores_ordem()
        jogar_novamente = input("Deseja jogar novamente? (sim/não): ").lower()
        if not jogar_novamente:
            print("Encerrando o jogo.")
            break
        elif jogar_novamente != "sim":
            print("Obrigado por jogar!")
            break
        print("\n--- Nova Partida ---")
