from db.database import Graph


class Collaborator:
    def __init__(self):
        self.db = Graph(uri='bolt://52.203.25.132:7687',
                        user='neo4j', password='acceptors-schoolhouses-complexes')

    def create(self, nameCompany, name, idade, cpf, funcao, salario):
        return self.db.execute_query(
            'CREATE (n:Collaborator {name:$name, idade:$idade, cpf:$cpf, funcao:$funcao, salario:$salario})-[r:Belongs]->(c:Institution{name:$nameCompany}) return n',
                {'name': name, 'idade': idade, 'cpf': cpf, 'funcao': funcao, 'salario': salario, 'nameCompany': nameCompany})

    def read(self):
        return self.db.execute_query(
            'MATCH (n:Collaborator) RETURN n')       

    def readByName(self, name):
        return self.db.execute_query(
            'MATCH (n:Collaborator {name:$name}) RETURN n',
            {'name': name})

    def update(self, name, idade, cpf, funcao, salario):
        return self.db.execute_query(
            'MATCH (n:Collaborator {name:$name}) SET n.idade = $idade, n.cpf = $cpf, n.funcao = $funcao, n.salario = $salario RETURN n',
            {'name': name, 'idade': idade, 'cpf': cpf, 'funcao': funcao, 'salario': salario})

    def delete(self, name):
        return self.db.execute_query(
            'MATCH (n:Collaborator {name:$name}) DETACH DELETE n',
            {'name': name})
