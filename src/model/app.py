from flask import Flask, jsonify, request
from src.model.agenda import (get_agenda)
from src.model.users import (get_users)
app = Flask(__name__)

# Rota para obter todos os itens
@app.route('/agenda', methods=['GET'])
def get_all_agenda_items():  # Busca os dados no model
    return  get_agenda()

if __name__ == '__main__':
    app.run(debug=True)  # debug=True para de
