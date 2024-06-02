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
        
def formatear_resultado(resultado):
    nuevo_res = []
    for res in resultado:
        nuevo_res.append(res['interfaces.nombre'])
    return nuevo_res



