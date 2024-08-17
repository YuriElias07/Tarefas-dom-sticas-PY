listagem_tarefas = []

def menu():
    while True:
        pergunta = int(input("""Menu:
                                 
1. Adicionar tarefa
2. Listar tarefas
3. Editar tarefa
4. Marcar uma tarefa como concluída
5. Desmarcar uma tarefa como concluída
6. Sair

Digite aqui: """))
            
        if pergunta == 1:
            descricao = input("Digite a descrição da tarefa: ")
            prazo = input("Digite o prazo da tarefa (formato: DD/MM/AAAA): ")
            prioridade = input("Digite a prioridade da tarefa (Baixa, Média, Alta): ")
            tarefa = {"descricao": descricao, "prazo": prazo, "prioridade": prioridade, "concluida": False}
            listagem_tarefas.append(tarefa)
            print("Tarefa adicionada com sucesso!")
                
        elif pergunta == 2:
            if listagem_tarefas:
                for i, tarefa in enumerate(listagem_tarefas):
                    i += 1
                    status = "Concluída" if tarefa["concluida"] else "Pendente"
                    print(f"{i}. Tarefa: {tarefa['descricao']}, Prazo: {tarefa['prazo']}, Prioridade: {tarefa['prioridade']} --> Status: {status}")
            else:
                print("Nenhuma tarefa cadastrada.")
                
        elif pergunta == 3:
            if not listagem_tarefas:
                print("Nenhuma tarefa disponível na lista.")
            else:
                for i, tarefa in enumerate(listagem_tarefas):
                    i += 1
                    status = "Concluída" if tarefa["concluida"] else "Pendente"
                    print(f"{i}. Tarefa: {tarefa['descricao']}, Prazo: {tarefa['prazo']}, Prioridade: {tarefa['prioridade']} --> Status: {status}")
                
                update = int(input("Digite o número da tarefa que deseja editar: ")) - 1
                
                if 0 <= update < len(listagem_tarefas):
                    descricao = input("Digite a nova descrição da tarefa: ")
                    prazo = input("Digite o novo prazo da tarefa (formato: DD/MM/AAAA): ")
                    prioridade = input("Digite a nova prioridade da tarefa (Baixa, Média, Alta): ")
                    listagem_tarefas[update] = {"descricao": descricao, "prazo": prazo, "prioridade": prioridade, "concluida": listagem_tarefas[update]["concluida"]}
                    print("Tarefa atualizada com sucesso!")
                else:
                    print("Número da tarefa inválido!")
                
        elif pergunta == 4:
            if not listagem_tarefas:
                print("Nenhuma tarefa disponível para marcar como concluída.")
            else:
                for i, tarefa in enumerate(listagem_tarefas):
                    i += 1
                    status = "Concluída" if tarefa["concluida"] else "Pendente"
                    print(f"{i}. Tarefa: {tarefa['descricao']}, Prazo: {tarefa['prazo']}, Prioridade: {tarefa['prioridade']} --> Status: {status}")
                
                concluir = int(input("Digite o número da tarefa que deseja marcar como concluída: ")) - 1
                
                if 0 <= concluir < len(listagem_tarefas):
                    listagem_tarefas[concluir]["concluida"] = True
                    print("Tarefa marcada como concluída!")
                else:
                    print("Número da tarefa inválido!")
                    
        elif pergunta == 5:
            if not listagem_tarefas:
                print("Nenhuma tarefa disponível para desmarcar como concluída.")
            else:
                for i, tarefa in enumerate(listagem_tarefas):
                    i += 1
                    status = "Concluída" if tarefa["concluida"] else "Pendente"
                    print(f"{i}. Tarefa: {tarefa['descricao']}, Prazo: {tarefa['prazo']}, Prioridade: {tarefa['prioridade']} --> Status: {status}")
                
                desmarcar = int(input("Digite o número da tarefa que deseja desmarcar como concluída: ")) - 1
                
                if 0 <= desmarcar < len(listagem_tarefas):
                    listagem_tarefas[desmarcar]["concluida"] = False
                    print("Tarefa desmarcada como concluída!")
                else:
                    print("Número da tarefa inválido!")
                    
        elif pergunta == 6:
            print("Saindo...")
            break               
        else:
            print("Opção inválida! Por favor, escolha as opções listadas no menu.")
        

menu()
