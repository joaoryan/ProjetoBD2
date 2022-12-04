from db.database import Graph


class Institution:
    def __init__(self):
        self.db = Graph(uri='bolt://52.203.25.132:7687',
                        user='neo4j', password='acceptors-schoolhouses-complexes')

    def create(self, name, cnpj, endereco):
        return self.db.execute_query(
            'CREATE (n:Institution {name:$name, cnpj:$cnpj, endereco:$endereco}) return n',
            {'name': name, 'cnpj': cnpj, 'endereco': endereco})

    def readByName(self, name):
        return self.db.execute_query(
            'MATCH (n:Institution {name:$name}) RETURN n',
            {'name': name})

    def update(self, name, cnpj, endereco):
        return self.db.execute_query(
            'MATCH (n:Institution {name:$name}) SET n.cnpj = $cnpj, n.endereco = $endereco RETURN n',
            {'name': name, 'cnpj': cnpj, 'endereco': endereco})

    def delete(self, name):
        return self.db.execute_query(
            'MATCH (n:Institution {name:$name}) DELETE n',
            {'name': name})

    def deleteAll(self):
        return self.db.execute_query(
            'MATCH (n) DETACH DELETE n'
        )