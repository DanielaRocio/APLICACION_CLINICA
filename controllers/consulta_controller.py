from flask import request, redirect, url_for, Blueprint
from models.consulta_model import Consulta
from models.medico_model import Medico
from models.paciente_model import Paciente
from views import consulta_view
from datetime import datetime

consulta_bp = Blueprint('consulta', __name__, url_prefix='/consultas')

@consulta_bp.route('/')
def index():
    consultas = Consulta.get_all()
    return consulta_view.list(consultas)

@consulta_bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        fecha = datetime.strptime(request.form['fecha'], '%Y-%m-%d').date()
        diagnostico = request.form['diagnostico']
        tratamiento = request.form['tratamiento']
        id_medico = request.form['id_medico']
        id_paciente = request.form['id_paciente']
         
        consulta = Consulta(fecha, diagnostico, tratamiento, id_medico, id_paciente)
        consulta.save()

        return redirect(url_for('consulta.index'))

    medicos = Medico.get_all()
    pacientes = Paciente.get_all()

    return consulta_view.create(medicos, pacientes)

@consulta_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    consulta = Consulta.get_by_id(id)

    if request.method == 'POST':
        fecha = datetime.strptime(request.form['fecha'], '%Y-%m-%d').date()
        diagnostico = request.form['diagnostico']
        tratamiento = request.form['tratamiento']
        id_medico = request.form['id_medico']
        id_paciente = request.form['id_paciente']

        consulta.update(
            fecha=fecha,
            diagnostico=diagnostico,
            tratamiento=tratamiento,
            id_medico=id_medico,
            id_paciente=id_paciente
        )

        return redirect(url_for('consulta.index'))

    medicos = Medico.get_all()
    pacientes = Paciente.get_all()

    return consulta_view.edit(consulta, medicos, pacientes)

@consulta_bp.route('/delete/<int:id>')
def delete(id):
    consulta = Consulta.get_by_id(id)
    consulta.delete()
    return redirect(url_for('consulta.index'))