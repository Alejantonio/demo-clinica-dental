from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from werkzeug.security import check_password_hash

app = Flask(__name__)

# Función auxiliar para abrir la base de datos temporalmente
def obtener_conexion():
    conexion = sqlite3.connect('clinica_dental.db')
    # Esto nos permite acceder a las columnas por su nombre (ej. usuario['rol'])
    conexion.row_factory = sqlite3.Row 
    return conexion

# RUTA 1: Muestra el inicio de sesión (Split Layout)
@app.route('/')
def index():
    return render_template('login.html')

# RUTA 2: Procesa el formulario
@app.route('/login', methods=['POST'])
def login():
    # 1. Capturamos los datos. El '' al final significa: "Si no hay nada, usa texto vacío"
    correo_ingresado = request.form.get('email', '')
    password_ingresada = request.form.get('password', '')

    # Verificamos rápidamente que no estén vacíos antes de ir a la base de datos
    if not correo_ingresado or not password_ingresada:
        return "❌ Error: Faltan datos en el formulario", 400

    # 2. Buscamos en la base de datos
    conexion = obtener_conexion()
    usuario = conexion.execute('SELECT * FROM usuarios WHERE correo = ?', (correo_ingresado,)).fetchone()
    conexion.close()

    # 3. Validamos la contraseña encriptada (ahora password_ingresada es siempre un texto)
    if usuario and check_password_hash(usuario['password'], password_ingresada):
        
        # 4. BIFURCACIÓN DE LÓGICA (El tráfico)
        if usuario['rol'] == 'dentista':
            return redirect(url_for('panel_dentista'))
        
        elif usuario['rol'] == 'paciente':
            return redirect(url_for('perfil_paciente', id_usuario=usuario['id_usuario']))
        
        else:
            # Tapamos el "hueco lógico" por si existe un rol desconocido
            return "❌ Error: Rol de usuario no reconocido", 403
            
    # Si la contraseña es mala o el usuario no existe (Quitamos el 'else' innecesario y lo dejamos como salida por defecto)
    return "❌ Error: Correo o contraseña incorrectos", 401

# RUTA 3: Panel del Dentista (Demo)
@app.route('/admin')
def panel_dentista():
    conexion = obtener_conexion()
    # Hacemos un JOIN para traer el nombre del perfil y el correo de la cuenta
    pacientes = conexion.execute('''
        SELECT p.nombre_completo, p.edad, p.telefono, u.correo 
        FROM perfiles_pacientes p
        JOIN usuarios u ON p.id_usuario = u.id_usuario
    ''').fetchall()
    conexion.close()
    
    # Pasamos la lista de pacientes al nuevo archivo HTML
    return render_template('panel_dentista.html', pacientes=pacientes)

# RUTA 4: Vista del Paciente (Demo)
@app.route('/perfil/<int:id_usuario>')
def perfil_paciente(id_usuario):
    return f"👤 Bienvenido a tu espacio privado. Tu ID es: {id_usuario}"

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)
