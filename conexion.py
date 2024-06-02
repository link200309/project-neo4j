from neo4j import GraphDatabase

uri = "bolt://localhost:7687"
usuario = "neo4j"
contraseña = "12345678"

driver = GraphDatabase.driver(uri, auth=(usuario, contraseña))

def ejecutar_consulta(tx, consulta, **kwargs):
    resultado = tx.run(consulta, **kwargs)
    return resultado.data()

def log_in(usuario, password):
    with driver.session() as sesion:
        consulta = (
            "MATCH (e) WHERE e.nombre=$usuario AND e.password=$password "
            "RETURN e"
        )
        resultado = sesion.read_transaction(ejecutar_consulta, consulta, usuario=usuario, password=password)
        return resultado
    
def obtener_interfaces(nodo):
    with driver.session() as sesion:
        consulta = (
            "MATCH (u:UserN {nombre: $nombre, password: $password})-[:UserN_Rol]->()-[:Rol_Funcion]->()-[:Funcion_UI]->(interfaces) "
            "RETURN interfaces.nombre"
        )
        resultado = sesion.read_transaction(ejecutar_consulta, consulta, nombre=nodo[0]['e']['nombre'], password=nodo[0]['e']['password'])
        interfaces = formatear_resultado(resultado)
        return interfaces
    
def crear_tarea(nodo, datos_tarea):
    with driver.session() as sesion:
        consulta = (
            "MATCH (u:Docente {nombre: $nombre, password: $password})-[:Imparte]->(c:Curso {nombre:$nombre_curso}) "
            "CREATE (t:Tarea {titulo:$titulo, descripcion:$descripcion, fecha_publica:date(), fecha_limite:$fecha_limite}) "
            "CREATE (c)-[:Se_da]->(t)"
        )
        nombre = nodo[0]['e']['nombre']
        password = nodo[0]['e']['password']
        sesion.write_transaction(ejecutar_consulta, consulta, nombre=nombre, password=password, nombre_curso=datos_tarea.get('nombre_curso'), titulo=datos_tarea.get('titulo'), descripcion=datos_tarea.get('descripcion'), fecha_limite=datos_tarea.get('fecha_limite'))
        
def obtener_cursos(nodo):
    with driver.session() as sesion:
        consulta = (
            "MATCH (u:Docente {nombre: $nombre, password: $password})-[:Imparte]->(c:Curso) "
            "RETURN c.nombre"
        )
        nombre = nodo[0]['e']['nombre']
        password = nodo[0]['e']['password']
        resultado = sesion.read_transaction(ejecutar_consulta, consulta, nombre=nombre, password=password)
        cursos = formatear_resultado(resultado)
        return cursos
        
def formatear_resultado(resultado):
    nuevo_res = []
    for res in resultado:
        nuevo_res.append(res[next(iter(res))])
    return nuevo_res



