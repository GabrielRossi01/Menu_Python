# Lista para armazenar alertas
alertas = []
relatorios = []

# Variável de controle para manter o menu em execução
executando = True

# Estrutura de repetição para manter o menu rodando até que o usuário escolha sair
while executando:

    print("╔════════════════════════════════════════╗")
    print("║             MENU PRINCIPAL             ║")
    print("╠════════════════════════════════════════╣")
    print("║ [1] Monitoramento em Tempo Real        ║")
    print("║────────────────────────────────────────║")
    print("║ [2] Gerar Alerta Automático            ║")
    print("║────────────────────────────────────────║")
    print("║ [3] Prever Falhas Operacionais         ║")
    print("║────────────────────────────────────────║")
    print("║ [4] Ver Relatórios de Performance      ║")
    print("║────────────────────────────────────────║")
    print("║ [5] Sair                               ║")
    print("╚════════════════════════════════════════╝")

    # Solicitar a escolha do usuário
    escolha = int(input("Escolha uma opção [1-5]: "))  # Usuário insere uma opção

    # Estruturas de decisão para verificar a escolha do usuário
    if escolha == 1:
        print('\nIniciando monitoramento em tempo real...')
        print('Monitoramento ativo.\n')
        # Simulando coleta de dados
        for dados in range(3):
            print(f'Dados coletados da estação {dados + 1}...\n')

    elif escolha == 2:
        alerta = input('Digite o alerta a ser enviado: ')
        alertas.append(alerta)
        print('\nGerando alerta automático...')
        print(f'Alerta "{alerta}" enviado para a equipe de manutenção.\n')

    elif escolha == 3:
        falha = input('Descreva a falha a ser prevista: ')
        print('\nIniciando previsão de falhas...')
        print(f'Falha prevista: {falha}. Intervenção agendada.\n')

    elif escolha == 4:
        print('\nExibindo relatórios de performance...')
        print('Relatório gerado com sucesso!\n')

    elif escolha == 5:
        print('\nSistema encerrado.\n')
        break  # Encerrar a repetição

    else:
        print('\nOpção inválida. Tente novamente.\n')