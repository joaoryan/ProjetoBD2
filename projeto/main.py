from flask import Flask, make_response, jsonify, request 
from db.collaborator import Collaborator
from db.institution import Institution
from helper.write_a_json import write_a_json


app = Flask(__name__)

collaboratorDao = Collaborator()
institutionDao= Institution()

institutionDao.deleteAll()
institutionDao.create("Inatel", "00.000.000/0000-00", "Santa Rita")

@app.route("/read",  methods=['GET'])
def func_read():
    aux = collaboratorDao.read()
    return make_response(
        jsonify(
            mensagem='200',
            dados=write_a_json(aux, '1A')
        )
    )

@app.route("/creat",  methods=['POST'])
def func_creat():
    user = request.json
    collaboratorDao.create('Inatel', user['name'], user['idade'], user['cpf'], user['funcao'], user['salario'])     

    return make_response(
        jsonify(
            mensagem='200',
            dados=user
        )
    )

@app.route("/update",  methods=['PUT'])
def func_update():
    user = request.json
    collaboratorDao.update(user['name'], user['idade'], user['cpf'], user['funcao'], user['salario'])
    return make_response(
        jsonify(
            mensagem='200',
            dados=user
        )
    )

@app.route("/delete",  methods=['DELETE'])
def func_delete():
    user = request.json
    collaboratorDao.delete(user['name'])
    return make_response(
        jsonify(
            mensagem='200',
            dados=user
        )
    )

app.run()

institutionDao.db.close()
collaboratorDao.db.close()