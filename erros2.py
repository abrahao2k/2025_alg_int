try:
    v1 = int(input("Dividendo: "))
    v2 = int(input("Divisor: "))
    print(f"Resultado da divisao: {v1/v2}")

except ZeroDivisionError:
    print("O divisor não pode ser ZERO.")
    #raise #mostra detalhes do erro ao finalizar a execução

except ValueError:
    print("Número digitado inválido.")

except (ImportError, ModuleNotFoundError):
    print("Erro importando biblioteca.")

except: #captura qualquer erro não informado
    print("Erro desconhecido.")

else: # só entra aqui se o try terminar sem erro
    print("Deu tudo certo.")

finally: # sempre é executado, mesmo que tenha erro
    print("Até a próxima!")