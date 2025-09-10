def adicionar_notas():
    notas = []
    while True:
        try:
            s = input("Informe uma nota (ou pressione Enter para terminar): ")
            if not s:
                break
            nota = float(s)
            if nota < 0 or nota > 10:
                print("Informe uma nota entre 0 e 10.")
                continue
            notas.append(nota)
        except ValueError:
            print("Valor inválido. Tente novamente.")
    return notas

def calcular_media(notas):
    return sum(notas) / len(notas) if notas else 0

def determinar_situacao(media):
    return "Aprovado" if media >= 7 else "Reprovado"

def gerar_relatorio(notas, media, situacao):
    print("\n===== RELATÓRIO FINAL =====")
    print("Notas inseridas:", ", ".join(f"{n:.1f}" for n in notas))
    print(f"Média: {media:.2f}")
    print("Situação:", situacao)

def main():
    print("=== Sistema de Gestão de Notas ===")
    notas = adicionar_notas()
    if not notas:
        print("\nNenhuma nota foi inserida. Encerrando o sistema.")
        return
    media = calcular_media(notas)
    situacao = determinar_situacao(media)
    gerar_relatorio(notas, media, situacao)

if __name__ == "__main__":
    main()
