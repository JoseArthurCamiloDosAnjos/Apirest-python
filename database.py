import mysql.connector
from mysql.connector import Error

def testar_conexao():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password=''
        )

        # Se a conexão com o servidor for bem-sucedida
        if conn.is_connected():
            print("Conexão com o servidor MySQL bem-sucedida!")

            # Verifica se o banco de dados 'agendaai_jose' existe
            cursor = conn.cursor()
            cursor.execute("SHOW DATABASES LIKE 'agendaai_jose'")
            database_exists = cursor.fetchone()

            if database_exists:
                print("O banco de dados 'agendaai_jose' já existe.")
                return True
            else:
                print("O banco de dados 'agendaai_jose' não foi encontrado. Por favor, crie-o.")
                return False

    except Error as e:
        # Se ocorrer um erro, ele será capturado aqui
        print(f"Erro ao conectar com o MySQL: {e}")
        return False

    finally:
        # Garante que a conexão seja fechada, mesmo se houver um erro
        if 'conn' in locals() and conn.is_connected():
            conn.close()
            print("Conexão com o MySQL fechada.")

# Chamada da função para testar
if testar_conexao():
    print("Você pode prosseguir com seu projeto!")
else:
    print("A conexão falhou. Verifique as credenciais ou a existência do banco de dados.")
