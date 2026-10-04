from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)
DB_NAME = "gestion.db"

#Proyecto: Gestión de Proyectos y Tareas

def init_db():
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        # Se crea la base de datos con 2 tablas relacionadas
        
        #Se crea la entidad "Proyectos"
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS proyectos (
                id INTEGER PRIMARY KEY AUTOINCREMENT, -- II. Uso de PRIMARY KEY
                nombre TEXT NOT NULL,
                descripcion TEXT
            )
        ''')
        
        #Se crea la entidad "Tareas"
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tareas (
                id INTEGER PRIMARY KEY AUTOINCREMENT, -- II. Uso de PRIMARY KEY
                proyecto_id INTEGER,
                titulo TEXT NOT NULL,
                estado TEXT,
                FOREIGN KEY (proyecto_id) REFERENCES proyectos(id) -- II. Uso de FOREIGN KEY
            )
        ''')
        conn.commit()
    except Exception as e:
        print("Error al inicializar base de datos:", e)
    finally:
        conn.close()

@app.route('/')
def index():
    #El archivo se conecta a la interfaz html
    return render_template('index.html')

#Se crea el API REST con CRUD completo de la entidad "Proyectos"

#Se usa POST para crear (Ejemplo: POST /proyectos)
@app.route('/proyectos', methods=['POST'])
def crear_proyecto():
    #Se reciben datos con request.json
    data = request.json
    
    #Se validan los datos
    if "nombre" not in data:
        return jsonify({"error": "Falta nombre"}), 400

    #Se manejan errores con try except
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        #Se utilizan placeholders ?
        cursor.execute("INSERT INTO proyectos (nombre, descripcion) VALUES (?, ?)", 
                       (data["nombre"], data.get("descripcion", "")))
        conn.commit()
        
        #Se responde con jsonify()
        return jsonify({"mensaje": "Proyecto creado"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

#Se usa GET para consultar todos los datos (Ejemplo: GET /proyectos)
@app.route('/proyectos', methods=['GET'])
def obtener_proyectos():
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM proyectos")
        proyectos = [{"id": row[0], "nombre": row[1], "descripcion": row[2]} for row in cursor.fetchall()]
        return jsonify(proyectos), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

#Se usa GET para consultar un dato (Ejemplo: GET /proyectos/1)
@app.route('/proyectos/<int:id>', methods=['GET'])
def obtener_proyecto(id):
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        #Se utilizan placeholders ? en el WHERE
        cursor.execute("SELECT * FROM proyectos WHERE id = ?", (id,))
        row = cursor.fetchone()
        if row:
            return jsonify({"id": row[0], "nombre": row[1], "descripcion": row[2]}), 200
        return jsonify({"error": "No encontrado"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

#Se usa PUT para actualizar (Ejemplo: PUT /proyectos/1)
@app.route('/proyectos/<int:id>', methods=['PUT'])
def actualizar_proyecto(id):
    data = request.json # IV. Recibir datos JSON
    
    #Se hacen validaciones
    if "nombre" not in data:
        return jsonify({"error": "Falta nombre"}), 400

    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        #Se utilizan placeholders múltiples
        cursor.execute("UPDATE proyectos SET nombre = ?, descripcion = ? WHERE id = ?", 
                       (data["nombre"], data.get("descripcion", ""), id))
        conn.commit()
        return jsonify({"mensaje": "Actualizado"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

#Se usa DELETE para eliminar (Ejemplo: DELETE /proyectos/1)
@app.route('/proyectos/<int:id>', methods=['DELETE'])
def eliminar_proyecto(id):
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        #Se utilizan placeholders
        cursor.execute("DELETE FROM proyectos WHERE id = ?", (id,))
        conn.commit()
        return jsonify({"mensaje": "Eliminado"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

#Se crea el API REST con CRUD completo de la entidad "Tareas"

#Se usa POST para crear
@app.route('/tareas', methods=['POST'])
def crear_tarea():
	#Se reciben datos con request.json
    data = request.json 
    if "titulo" not in data or "proyecto_id" not in data: 
	#Se responde con jsonify()
        return jsonify({"error": "Falta titulo o proyecto_id"}), 400

    try: #Se validan datos
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        #Se utilizan placeholders ?
        cursor.execute("INSERT INTO tareas (proyecto_id, titulo, estado) VALUES (?, ?, ?)", 
                       (data["proyecto_id"], data["titulo"], data.get("estado", "Pendiente")))
        conn.commit()
        return jsonify({"mensaje": "Tarea creada"}), 201 
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

#Se usa GET para consultar todos los datos
@app.route('/tareas', methods=['GET'])
def obtener_tareas():
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tareas")
        tareas = [{"id": row[0], "proyecto_id": row[1], "titulo": row[2], "estado": row[3]} for row in cursor.fetchall()]
        return jsonify(tareas), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

#Se usa GET para consultar un dato
@app.route('/tareas/<int:id>', methods=['GET'])
def obtener_tarea(id):
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tareas WHERE id = ?", (id,))
        row = cursor.fetchone()
        if row:
            return jsonify({"id": row[0], "proyecto_id": row[1], "titulo": row[2], "estado": row[3]}), 200
        return jsonify({"error": "No encontrada"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

#Se usa PUT para actualizar
@app.route('/tareas/<int:id>', methods=['PUT'])
def actualizar_tarea(id):
    data = request.json
    if "titulo" not in data:
        return jsonify({"error": "Falta titulo"}), 400

    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("UPDATE tareas SET titulo = ?, estado = ? WHERE id = ?", 
                       (data["titulo"], data.get("estado", "Pendiente"), id))
        conn.commit()
        return jsonify({"mensaje": "Tarea actualizada"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

#Se usa DELETE para eliminar
@app.route('/tareas/<int:id>', methods=['DELETE'])
def eliminar_tarea(id):
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tareas WHERE id = ?", (id,))
        conn.commit()
        return jsonify({"mensaje": "Tarea eliminada"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

if __name__ == '__main__':
    init_db() 
    app.run(debug=True)