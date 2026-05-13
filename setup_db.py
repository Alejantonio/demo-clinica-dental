import sqlite3
from werkzeug.security import generate_password_hash

def crear_base_datos():
    conexion = sqlite3.connect('clinica_dental.db')
    cursor = conexion.cursor()

    # Tablas
    cursor.execute('CREATE TABLE IF NOT EXISTS usuarios (id_usuario INTEGER PRIMARY KEY AUTOINCREMENT, correo TEXT UNIQUE NOT NULL, password TEXT NOT NULL, rol TEXT NOT NULL)')
    cursor.execute('CREATE TABLE IF NOT EXISTS perfiles_pacientes (id_paciente INTEGER PRIMARY KEY AUTOINCREMENT, id_usuario INTEGER, nombre_completo TEXT NOT NULL, edad INTEGER, telefono TEXT, fecha_nacimiento TEXT, FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario))')

    # 1. Crear el Dentista (si no existe)
    cursor.execute("SELECT * FROM usuarios WHERE correo = 'admin@clinica.com'")
    if not cursor.fetchone():
        cursor.execute("INSERT INTO usuarios (correo, password, rol) VALUES (?, ?, ?)",
                       ('admin@clinica.com', generate_password_hash('12345'), 'dentista'))

    # 2. Datos de prueba para el cliente (Pacientes ficticios)
    pacientes_demo = [
        ('Juan Pérez', 28, '555-0101', '1996-05-15', 'juan@ejemplo.com'),
        ('María García', 34, '555-0202', '1990-11-20', 'maria@ejemplo.com'),
        ('Carlos Ruiz', 45, '555-0303', '1979-02-10', 'carlos@ejemplo.com')
    ]

    for nombre, edad, tel, fecha, correo in pacientes_demo:
        # Primero creamos su usuario
        cursor.execute("SELECT * FROM usuarios WHERE correo = ?", (correo,))
        if not cursor.fetchone():
            cursor.execute("INSERT INTO usuarios (correo, password, rol) VALUES (?, ?, ?)",
                           (correo, generate_password_hash('paciente123'), 'paciente'))
            id_u = cursor.lastrowid
            # Luego su perfil
            cursor.execute("INSERT INTO perfiles_pacientes (id_usuario, nombre_completo, edad, telefono, fecha_nacimiento) VALUES (?, ?, ?, ?, ?)",
                           (id_u, nombre, edad, tel, fecha))

    conexion.commit()
    conexion.close()
    print("✅ Base de datos lista con pacientes de prueba.")

if __name__ == '__main__':
    crear_base_datos()