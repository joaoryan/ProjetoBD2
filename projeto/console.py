from db.collaborator import Collaborator
from db.institution import Institution
from helper.write_a_json import write_a_json

collaboratorDao = Collaborator()
institutionDao= Institution()

institutionDao.deleteAll()
institutionDao.create("Inatel", "00.000.000/0000-00", "Santa Rita")

def divider():
    print('\n' + '-' * 80 + '\n')

while 1:    
    option = input('1. Create\n2. Read all\n3. Update\n4. Delete all\n')

    if option == '1':
        print('Digite dados do colaborador:')
        nome = input('  Nome: ')
        idade = input('  Idade: ')
        cpf = input('  Cpf: ')
        funcao = input('  Funcao: ')
        salario = input('  Salario: ')
        collaboratorDao.create('Inatel', nome, idade, cpf, funcao, salario)
        print('    ')
        print('Usuario criado')
        divider()

    elif option == '2':
        aux = collaboratorDao.read()
        print(write_a_json(aux, '1A'))
        divider()

    elif option == '3':
        nome = input('Digite o nome de quem deseja editar:')
        print('Digite dados do colaborador:')
        idade = input('  Idade: ')
        cpf = input('  Cpf: ')
        funcao = input('  Funcao: ')
        salario = input('  Salario: ')
        collaboratorDao.update( nome, idade, cpf, funcao, salario)
        print('    ')
        print('Usuario editado')
        divider()

    elif option == '4':
        nome = input('Digite o nome de quem deseja deletar:')
        collaboratorDao.delete(nome)
        print('    ')
        print('Usuario deletado')
        divider()

    else:
        break

institutionDao.db.close()
collaboratorDao.db.close()
