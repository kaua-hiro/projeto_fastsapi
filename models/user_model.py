from database.db import conectar

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(""" SELECT table_name 
                   FROM user_tables
                   WHERE table_name = 'LISTA_TAREFAS'
                   """)
    if not cursor.fetchone():
        cursor.execute("""
            CREATE TABLE lista_tarefas (
                id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                tarefa VARCHAR2(255) NOT NULL, 
                status NUMBER(1) DEFAULT 0
            )                
        """)
        conn.commit()
    conn.close()
    
def inserir_tarefa(tarefa):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO lista_tarefas (tarefa) VALUES (:1) ", [tarefa])
    conn.commit()
    conn.close()
    
def listar_tarefas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM lista_tarefas")
    tarefas = cursor.fetchall()
    conn.close()
    return tarefas

def excluir_tarefa(tarefa_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM lista_tarefas WHERE id = :1", [tarefa_id])
    conn.commit()
    conn.close()
    
def buscar_tarefa_por_id(tarefa_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM lista_tarefas WHERE id = :1", [tarefa_id])
    tarefa = cursor.fetchone()
    conn.close()
    return tarefa

def atualizar_tarefa(tarefa_id, tarefa):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""UPDATE lista_tarefas 
                   SET tarefa = :1
                   WHERE id = :2
                   """, [tarefa, tarefa_id])
    conn.commit()
    conn.close()

def atualizar_status(tarefa_id, status):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(""" UPDATE lista_tarefas
                   SET status = :1
                   WHERE id = :2 
                   """, [status, tarefa_id])
    conn.commit()
    conn.close()