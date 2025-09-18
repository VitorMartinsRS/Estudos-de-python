import pymysq

class GerenciadorAlunos:
    def __init__(self, dbname, user, password, host, port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.conn = None
        self.cursor = None

        try:
            self.conn = pymysq.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            self.cursor = self.conn.cursor()
            print('Conexão com o banco de dados estabelecida com êxito')
        except pymysq.OperationalError as e:
            print(f'Erro ao conectar ao banco de dados: {e}')
            self.conn = None
            self.cursor = None

    def __del__(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
        print('Conexão com o banco de dados fechada.')

if __name__ == '__main__':
    gerenciador = GerenciadorAlunos(
        dbname="escola_db",
        user="escola_user",
        password="anamaria090423",
        host="localhost",
        port="5432"
    )