# Variável de controle para manter o menu em execução (estrutura de repetição)
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

    # Solicitar a escolha do usuário (decisão com entrada de dados)
    escolha = int(input("Escolha uma opção [1-5]: "))  # Usuário insere uma opção

    # Estruturas de decisão para verificar a escolha do usuário
    if escolha == 1:

        print('\nIniciando monitoramento em tempo real...')
        print('Monitoramento ativo.\n')
    elif escolha == 2:

        print('\nGerando alerta automático...')
        print('Alerta enviado para equipe de manutenção.\n')
    elif escolha == 3:

        print('\nIniciando previsão de falhas...')
        print('Falha prevista. Intervenção agendada.\n')
    elif escolha == 4:

        print('\nExibindo relatórios de performance...')
        print('Relatório de performance gerado.\n')
    elif escolha == 5:

        print('\nSistema encerrado.\n')
        executando = False  # Encerrar a repetição
    else:
        # Caso o usuário insira uma opção inválida
        print('\nOpção inválida. Tente novamente.\n')