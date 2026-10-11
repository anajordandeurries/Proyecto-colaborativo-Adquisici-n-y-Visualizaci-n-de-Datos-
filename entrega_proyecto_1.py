"""
Proyecto Colaborativo Adquisición y visualización de datos.
¡¡Somos Campeones del Mundo ★★!!
    2026/27 iMat Comillas ICAI

    Miembros del grupo:
María Coro Pérez de la Fuente
Ana Jordán de Urríes López
"""

"""
Bloque 1:  Recopilación, limpieza y tratamiento de datasets de trabajo

    Entrega: 12 de octubre de 2026 (confirmar fecha en Moodle)

"""

# Realización de las exportaciones necesarias:
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from IPython.display import display  # Mostrar tablas durante la exploración


"""
1. Exploración inicial de todos los documentos:
    Comenzaremos explorando todos los csv proporcionados para entender su contenido, formato y tamaño.
"""


# 1. 2001eurocopa_fem_stats.csv
print("\n========== 1. EUROCOPA FEMENINA ==========")

femenino = pd.read_csv("2001eurocopa_fem_stats.csv")

print("\nPrimeras filas:")
print(femenino.head())

print("\nDimensiones:", femenino.shape)

print("\nInformación del dataset:")
femenino.info()

print("\nResumen estadístico:")
print(femenino.describe(include="all"))

print("\nValores nulos:")
print(femenino.isna().sum())

print("\nFilas duplicadas:", femenino.duplicated().sum())


# 2. 2026match_lineups.csv
print("\n========== 2. MATCH LINEUPS ==========")

lineups = pd.read_csv("2026match_lineups.csv", sep=";")

print("\nPrimeras filas:")
print(lineups.head())

print("\nDimensiones:", lineups.shape)

print("\nInformación del dataset:")
lineups.info()

print("\nResumen estadístico:")
print(lineups.describe(include="all"))

print("\nValores nulos:")
print(lineups.isna().sum())

print("\nFilas duplicadas:", lineups.duplicated().sum())


# 3. 2026match_register.csv
print("\n========== 3. MATCH REGISTER ==========")

registro = pd.read_csv("2026match_register.csv", sep=";")

print("\nPrimeras filas:")
print(registro.head())

print("\nDimensiones:", registro.shape)

print("\nInformación del dataset:")
registro.info()

print("\nResumen estadístico:")
print(registro.describe(include="all"))

print("\nValores nulos:")
print(registro.isna().sum())

print("\nFilas duplicadas:", registro.duplicated().sum())


# 4. 2026nationalteams.csv
print("\n========== 4. NATIONAL TEAMS ==========")

equip_nacional = pd.read_csv("2026nationalteams.csv")

print("\nPrimeras filas:")
print(equip_nacional.head())

print("\nDimensiones:", equip_nacional.shape)

print("\nInformación del dataset:")
equip_nacional.info()

print("\nResumen estadístico:")
print(equip_nacional.describe(include="all"))

print("\nValores nulos:")
print(equip_nacional.isna().sum())

print("\nFilas duplicadas:", equip_nacional.duplicated().sum())


# 5. 2026player_stats.csv
print("\n========== 5. PLAYER STATS ==========")

stats = pd.read_csv("2026player_stats.csv", sep=";")

print("\nPrimeras filas:")
print(stats.head())

print("\nDimensiones:", stats.shape)

print("\nInformación del dataset:")
stats.info()

print("\nResumen estadístico:")
print(stats.describe(include="all"))

print("\nValores nulos:")
print(stats.isna().sum())

print("\nFilas duplicadas:", stats.duplicated().sum())


# 6. 2026squads_and_players.csv
print("\n========== 6. SQUADS AND PLAYERS ==========")

players = pd.read_csv("2026squads_and_players.csv", sep=";")

print("\nPrimeras filas:")
print(players.head())

print("\nDimensiones:", players.shape)

print("\nInformación del dataset:")
players.info()

print("\nResumen estadístico:")
print(players.describe(include="all"))

print("\nValores nulos:")
print(players.isna().sum())

print("\nFilas duplicadas:", players.duplicated().sum())


# 7. index_referees.csv
print("\n========== 7. INDEX REFEREES ==========")

index_referees = pd.read_csv("index_referees.csv", sep=";")

print("\nPrimeras filas:")
print(index_referees.head())

print("\nDimensiones:", index_referees.shape)

print("\nInformación del dataset:")
index_referees.info()

print("\nResumen estadístico:")
print(index_referees.describe(include="all"))

print("\nValores nulos:")
print(index_referees.isna().sum())

print("\nFilas duplicadas:", index_referees.duplicated().sum())


# 8. matches_mundial202.csv
print("\n========== 8. MATCHES MUNDIAL 202 ==========")

matches_202 = pd.read_csv("matches_mundial202.csv")

print("\nPrimeras filas:")
print(matches_202.head())

print("\nDimensiones:", matches_202.shape)

print("\nInformación del dataset:")
matches_202.info()

print("\nResumen estadístico:")
print(matches_202.describe(include="all"))

print("\nValores nulos:")
print(matches_202.isna().sum())

print("\nFilas duplicadas:", matches_202.duplicated().sum())


# 9. matches_mundial2026.csv
print("\n========== 9. MATCHES MUNDIAL 2026 ==========")

matches_2026 = pd.read_csv("matches_mundial2026.csv", sep=";")

print("\nPrimeras filas:")
print(matches_2026.head())

print("\nDimensiones:", matches_2026.shape)

print("\nInformación del dataset:")
matches_2026.info()

print("\nResumen estadístico:")
print(matches_2026.describe(include="all"))

print("\nValores nulos:")
print(matches_2026.isna().sum())

print("\nFilas duplicadas:", matches_2026.duplicated().sum())


# 10. tournament_stages.csv
print("\n========== 10. TOURNAMENT STAGES ==========")

tournament = pd.read_csv("tournament_stages.csv")

print("\nPrimeras filas:")
print(tournament.head())

print("\nDimensiones:", tournament.shape)

print("\nInformación del dataset:")
tournament.info()

print("\nResumen estadístico:")
print(tournament.describe(include="all"))

print("\nValores nulos:")
print(tournament.isna().sum())

print("\nFilas duplicadas:", tournament.duplicated().sum())


# 11. worldcup_venues.csv
print("\n========== 11. WORLDCUP VENUES ==========")

venues = pd.read_csv("worldcup_venues.csv", sep=";")

print("\nPrimeras filas:")
print(venues.head())

print("\nDimensiones:", venues.shape)

print("\nInformación del dataset:")
venues.info()

print("\nResumen estadístico:")
print(venues.describe(include="all"))

print("\nValores nulos:")
print(venues.isna().sum())

print("\nFilas duplicadas:", venues.duplicated().sum())



"""
2. Crear las variables.
    Crearemos 3 DataFrames a los que posteriormente iremos añadiendo información.
"""
partidos = pd.DataFrame()
jugadores =  pd.DataFrame()
eventos =  pd.DataFrame()


"""  
3. Añadir información a las variables.
    A partir de los DataFrames importados, crearemos las variables partidos, jugadores y eventos, con las columnas, los índices y los nombres
    requeridos en cada caso. También ajustaremos el tipo de dato de cada columna.
"""

#Empezamos con partidos: 
partidos["fecha_partido"] = matches_2026["date"]

leyenda_ronda = dict(zip(tournament["stage_id"], tournament["stage_name"])) #empareja cada nombre de fase con su correspondiente clave
partidos["ronda"] = matches_2026["stage_id"].map(leyenda_ronda)

leyenda_estadios = dict(zip(venues["venue_id"], venues["stadium_name"]))
partidos["estadio"] = matches_2026["venue_id"].map(leyenda_estadios)

leyenda_ciudad = dict(zip(venues["venue_id"], venues["city"]))
partidos["ciudad_partido"] = matches_2026["venue_id"].map(leyenda_ciudad)

leyenda_pais = dict(zip(venues["venue_id"], venues["country"]))
partidos["pais_partido"] = matches_2026["venue_id"].map(leyenda_pais)
# Homogeneizar categorías equivalentes (USA / usa) sin alterar otras etiquetas.
partidos["pais_partido"] = partidos["pais_partido"].replace({"usa": "USA"})

#hacemos esto para que map no falle, con los valores nulos.
selecciones_con_id = equip_nacional.dropna(subset=["team_id"]).drop_duplicates(subset=["team_id"], keep="first")
# Las filas sin team_id y las repetidas no deben alterar la correspondencia.
leyenda_seleccion = dict(zip(selecciones_con_id["team_id"],selecciones_con_id["team_name"]))

partidos["seleccion_local"] = matches_2026["home_team_id"].map(leyenda_seleccion)
partidos["seleccion_visitante"] = matches_2026["away_team_id"].map(leyenda_seleccion)

partidos["marcador_local"] = matches_2026["home_score"]
partidos["marcador_visitante"] = matches_2026["away_score"]

leyenda_prorroga = {"Regular": "NO", "AET":"SI", "Penalties": "SI"}
partidos["prorroga"] = matches_2026["result_type"].map(leyenda_prorroga)

partidos["penalty_local"] = matches_2026["home_penalty_score"]
partidos["penalty_visitante"] = matches_2026["away_penalty_score"]

leyenda_arbitros = dict(zip(index_referees["referee_id"], index_referees["name"]))
partidos["arbitro_partido"] = matches_2026["referee_id"].map(leyenda_arbitros)

#Una vez almacenada la información en el DataFrame, cada fila tendrá el índice de un partido enumerado.
partidos.index = range(1, len(partidos) + 1)
partidos.index.name = "index_partido"

# Asignar tipo de dato numérico y de texto
columnas_enteras_partidos = ["marcador_local", "marcador_visitante", "penalty_local", "penalty_visitante"]
columnas_texto_partidos = ["ronda", "estadio", "ciudad_partido", "pais_partido", "seleccion_local", "seleccion_visitante", "prorroga", "arbitro_partido"]

partidos[columnas_enteras_partidos] = partidos[columnas_enteras_partidos].astype("Int64")
partidos[columnas_texto_partidos] = partidos[columnas_texto_partidos].astype("string")

print(partidos.dtypes)

print(partidos)




# Ahora jugadores
# Preferimos el nombre de la plantilla, que evita caracteres mal codificados de stats.
leyenda_nombre_jugador = dict(zip(players["player_id"], players["player_name"]))
jugadores["nombre_jugador"] = stats["player_id"].map(leyenda_nombre_jugador).fillna(stats["player_name"])
# En el CSV de plantillas algunos nombres se han truncado a "Mc".
# Recuperamos exclusivamente esos nombres desde la fuente de estadísticas,
# relacionando cada fila mediante player_id. No cambiamos nombres legítimos.
nombre_truncado = jugadores["nombre_jugador"] == "Mc"
jugadores.loc[nombre_truncado, "nombre_jugador"] = stats.loc[nombre_truncado, "player_name"]

#usamos la leyenda que hicimos antes para que no falle map.
jugadores["seleccion_nacional"] = stats["team_id"].map(leyenda_seleccion)

leyenda_club = dict(zip(players["player_id"], players["club_team"]))
jugadores["club_jugador"] = stats["player_id"].map(leyenda_club)

# "caps" son internacionalidades históricas, no partidos de esta competición.
# Contamos los partidos únicos en los que figura cada selección nacional.
partidos_originales = matches_2026.drop_duplicates(subset=["match_id"])
participaciones_local = partidos_originales[["match_id", "home_team_id"]].rename(columns={"home_team_id": "team_id"})
participaciones_visitante = partidos_originales[["match_id", "away_team_id"]].rename(columns={"away_team_id": "team_id"})
participaciones = pd.concat([participaciones_local, participaciones_visitante], ignore_index=True)
leyenda_partidos_seleccion = participaciones.groupby("team_id")["match_id"].nunique().to_dict()
jugadores["partidos_seleccion"] = stats["team_id"].map(leyenda_partidos_seleccion)

jugadores["posicion"] = stats["position"]

leyenda_valor_mercado = dict(zip(players["player_id"], players["market_value_eur"]))
jugadores["valor_mercado"] = stats["player_id"].map(leyenda_valor_mercado)

jugadores["partidos_jugados"] = stats["matches_played"]
jugadores["minutos_jugados"] = stats["minutes_played"]
jugadores["goles"] = stats["goals"]
jugadores["asistencias"] = stats["assists"]
jugadores["tiros"] = stats["shots"]
jugadores["tarjetas_amarillas"] = stats["yellow_cards"]
jugadores["tarjetas_rojas"] = stats["red_cards"]
jugadores["paradas"] = stats["saves"]
jugadores["goles_concedidos"] = stats["goals_conceded"]
jugadores["calificacion_media"] = stats["average_rating"]

columnas_texto_jugadores = ["nombre_jugador", "seleccion_nacional", "club_jugador", "posicion"]
columnas_enteras_jugadores = ["partidos_seleccion", "partidos_jugados", "minutos_jugados", "goles", "asistencias", "tiros", "tarjetas_amarillas", "tarjetas_rojas", "paradas", "goles_concedidos"]
columnas_decimales_jugadores = ["valor_mercado", "calificacion_media"]

jugadores[columnas_texto_jugadores] = (jugadores[columnas_texto_jugadores].astype("string"))
jugadores[columnas_enteras_jugadores] = (jugadores[columnas_enteras_jugadores].astype("Int64"))
jugadores[columnas_decimales_jugadores] = (jugadores[columnas_decimales_jugadores].astype("Float64"))

jugadores = jugadores.set_index("nombre_jugador")

print(jugadores.dtypes)

print(jugadores)




#Por último, la variable eventos:
eventos["minuto_evento"] = registro["minute"]
eventos["index_partido"] = registro["match_id"]

leyenda_jugadores = dict(zip(players["player_id"], players["player_name"]))
eventos["nombre_jugador"] = registro["player_id"].map(leyenda_jugadores)

eventos["tipo_evento"] = registro["event_type"]

#usamos la leyenda que ya teníamos para que no falle map.
eventos["seleccion_evento"] = registro["team_id"].map(leyenda_seleccion)

# Asignar tipos de datos
columnas_enteras_eventos = ["minuto_evento", "index_partido"]
columnas_texto_eventos = ["nombre_jugador", "tipo_evento", "seleccion_evento"]

eventos[columnas_enteras_eventos] = (eventos[columnas_enteras_eventos].astype("Int64"))
eventos[columnas_texto_eventos] = (eventos[columnas_texto_eventos].astype("string"))

# Índice enumerado: 1, 2, 3…
eventos.index = range(1, len(eventos) + 1)
eventos.index.name = "index_evento"

print(eventos.dtypes)

print(eventos)


"""
4. Tratamiento de duplicados, nulos y anómalos:
    Primero se realizará un análisis de los datos obtenidos, para entender bien la representación de cada dataset,
    antes de aplicar medidas.
"""
#Análisis de los datasets.
datasets = {"partidos": partidos, "jugadores": jugadores, "eventos": eventos}

for nombre, df in datasets.items():
    print(f"Análisis de {nombre}.")

    # Tamaño y tipos
    print("Dimensiones:", df.shape)
    df.info()

    # Nulos por columna
    print("Valores nulos:")
    print(df.isna().sum())

    # Filas con algún dato nulo
    print("Filas con valores nulos:")
    display(df[df.isna().any(axis=1)])

    # Duplicados: compara las columnas, sin incluir el índice
    print("Número de filas duplicadas:", df.duplicated().sum())
    display(df[df.duplicated(keep=False)])

    # Índices repetidos
    print("Número de índices repetidos:", df.index.duplicated().sum())

    # Resumen numérico: mínimos, máximos, medias…
    print("Resumen numérico:")
    display(df.describe())

    # Categorías y su frecuencia, incluyendo nulos
    for columna in df.select_dtypes(include=["string", "object"]).columns:
        print(f"\nValores de {columna}:")
        print(df[columna].value_counts(dropna=False))

    print(150*"=")



"""
Tratamiento de los valores duplicados
"""

# Duplicados en partidos:
print("Partidos duplicados:", partidos.duplicated().sum())
display(partidos[partidos.duplicated(keep=False)])
# Los partidos originales llevan un identificador único que coincide con su índice
# en los 104 registros iniciales. Validamos la equivalencia antes de usarlos.
assert (matches_2026.iloc[:104]["match_id"].to_numpy() == list(range(1, 105))).all()
partidos = partidos.drop_duplicates().copy()
print("Duplicados restantes:", partidos.duplicated().sum())


# Duplicados en jugadores
# Pasamos el nombre del índice a una columna para incluirlo en la comparación.
jugadores = jugadores.reset_index()
print("Jugadores duplicados:", jugadores.duplicated().sum())
display(jugadores[jugadores.duplicated(keep=False)])
jugadores = jugadores.drop_duplicates()
print("Duplicados restantes:", jugadores.duplicated().sum())
# Restauramos el índice.
jugadores = jugadores.set_index("nombre_jugador")



# Duplicados en eventos, sin considerar event_id
columnas_comparacion = ["match_id", "minute", "player_id", "event_type", "team_id"]

# Mostrar todos los posibles duplicados para revisarlos
posibles_duplicados = registro.duplicated(subset=columnas_comparacion, keep=False)

print("Posibles eventos duplicados:")
display(registro.loc[posibles_duplicados])

# Conservar los casos con información incompleta
datos_completos = registro[columnas_comparacion].notna().all(axis=1)

# Marcar las repeticiones, conservando la primera aparición
duplicados_eliminar = (registro.duplicated(subset=columnas_comparacion, keep="first")& datos_completos)

print("Repeticiones con datos completos:", duplicados_eliminar.sum())
display(registro.loc[duplicados_eliminar])

# Ejecutar esta línea después de confirmar que son copias del mismo evento
# eventos = eventos.iloc[(~duplicados_eliminar).to_numpy()].copy()

# Enumerar el índice de eventos
eventos.index = range(1, len(eventos) + 1)
eventos.index.name = "index_evento"



"""
Tratamiento de los valores nulos.
"""

# Nulos en partidos
print("Nulos en partidos antes del tratamiento:")
print(partidos.isna().sum())

# Recuperamos el tipo de resultado con los índices usados al crear partidos.
tipo_resultado = pd.Series(matches_2026["result_type"].values,index=range(1, len(matches_2026) + 1))

# Solo ponemos 0 en penaltis cuando sabemos que no hubo tanda.
sin_tanda = tipo_resultado.reindex(partidos.index).isin(["Regular", "AET"])
partidos.loc[sin_tanda, "penalty_local"] = (partidos.loc[sin_tanda, "penalty_local"].fillna(0))
partidos.loc[sin_tanda, "penalty_visitante"] = (partidos.loc[sin_tanda, "penalty_visitante"].fillna(0))

partidos[columnas_texto_partidos] = (partidos[columnas_texto_partidos].fillna("Desconocido"))

# Conservamos fechas, marcadores y prórroga desconocidos:
#no podemos deducir su valor únicamente por estar vacíos.
print("Nulos en partidos después del tratamiento:")
print(partidos.isna().sum())



# Nulos en jugadores
print("Nulos en jugadores antes del tratamiento:")
print(jugadores.isna().sum())
print("Nombres de jugador nulos:", jugadores.index.isna().sum())

# No modificamos la lista original con remove(), pues se reutiliza en el script.
columnas_texto_jugadores = [col for col in columnas_texto_jugadores if col != "nombre_jugador"]
jugadores[columnas_texto_jugadores] = (jugadores[columnas_texto_jugadores].fillna("Desconocido"))

# Conservamos los nulos numéricos como <NA>.
# No imputamos 0 ni la media porque no conocemos el dato real.
# Los nombres nulos del índice quedan pendientes de recuperación.

#Después del tratamiento:
print("Nulos en jugadores después del tratamiento:")
print(jugadores.isna().sum())



#Nulos en eventos
# Nulos en eventos
print("Nulos en eventos antes del tratamiento:")
print(eventos.isna().sum())

# Conservamos los nulos en tipo_evento para distinguirlos de un valor válido.
# Los registros sin identificación básica se excluirán tras el diagnóstico.
eventos[["nombre_jugador", "seleccion_evento"]] = (eventos[["nombre_jugador", "seleccion_evento"]].fillna("Desconocido"))

print("Nulos en eventos después del tratamiento:")
print(eventos.isna().sum())

"""
Tratamiento de los valores anómalos
"""


"""
Tratamiento de valores anómalos.

Identificamos los valores que no cumplen los rangos o
categorías esperadas de cada DataFrame.
Por ahora solo detectamos y mostramos las anomalías,
sin modificar los datos.
"""

# 1. Valores anómalos en partidos
print("\n========== ANOMALÍAS EN PARTIDOS ==========")

# Los marcadores no pueden ser negativos.
anomalias_marcadores = partidos[
    (partidos["marcador_local"] < 0) |
    (partidos["marcador_visitante"] < 0) |
    (partidos["penalty_local"] < 0) |
    (partidos["penalty_visitante"] < 0)
]

print("\nPartidos con marcadores negativos:")
print(anomalias_marcadores)

# La prórroga únicamente puede tomar los valores SI o NO.
anomalias_prorroga = partidos[
    partidos["prorroga"].notna() &
    ~partidos["prorroga"].isin(["SI", "NO", "Desconocido"])
]

print("\nPartidos con valores de prórroga incorrectos:")
print(anomalias_prorroga)


# 2. Valores anómalos en jugadores
print("\n========== ANOMALÍAS EN JUGADORES ==========")

# Comprobamos que las estadísticas no sean negativas.
columnas_no_negativas = [
    "partidos_seleccion", "valor_mercado",
    "partidos_jugados", "minutos_jugados",
    "goles", "asistencias", "tiros",
    "tarjetas_amarillas", "tarjetas_rojas",
    "paradas", "goles_concedidos"
]

for columna in columnas_no_negativas:
    anomalias = jugadores[jugadores[columna] < 0]

    print(f"\nValores negativos en {columna}:")
    print(anomalias)

# La calificación media debe estar entre 0 y 10.
anomalias_calificacion = jugadores[
    (jugadores["calificacion_media"] < 0) |
    (jugadores["calificacion_media"] > 10)
]

print("\nJugadores con calificaciones fuera de rango:")
print(anomalias_calificacion)


# 3. Valores anómalos en eventos
print("\n========== ANOMALÍAS EN EVENTOS ==========")

# No pueden existir minutos negativos.
minutos_negativos = eventos[eventos["minuto_evento"] < 0]

print("\nEventos con minutos negativos:")
print(minutos_negativos)

# Identificamos minutos superiores a 120 para revisarlos.
# No se eliminan automáticamente, ya que pueden existir
# eventos asociados a una tanda de penaltis.
minutos_altos = eventos[eventos["minuto_evento"] > 120]

print("\nEventos con minutos superiores a 120:")
print(minutos_altos)

# Comprobamos los tipos de eventos reconocidos.
tipos_validos = [
    "Goal", "Assist", "Yellow Card", "Red Card",
    "Penalty Shootout Goal", "Penalty Shootout Miss",
    "VAR Review", "Review VAR"
]

tipos_anomalos = eventos[
    ~eventos["tipo_evento"].isin(tipos_validos)
]

print("\nEventos con tipos no reconocidos:")
print(tipos_anomalos)

# Resumen de las anomalías detectadas
print("\n========== RESUMEN DE ANOMALÍAS ==========")

print("Partidos con marcadores negativos:", len(anomalias_marcadores))
print("Partidos con prórroga incorrecta:", len(anomalias_prorroga))
print("Jugadores con calificación fuera de rango:", len(anomalias_calificacion))
print("Eventos con minutos negativos:", len(minutos_negativos))
print("Eventos con minutos superiores a 120:", len(minutos_altos))
print("Eventos con tipos no reconocidos:", len(tipos_anomalos))


"""
APARTADO 5. Revisión de anomalías en eventos.

Comprobamos los registros originales para determinar
qué eventos deben excluirse y cuáles conservarse.
"""

print("\n========== REVISIÓN DE EVENTOS ==========")

# 1. Eventos con minutos negativos
negativos = registro[registro["minute"] < 0]

print("\nEventos con minutos negativos:")
print(negativos.to_string(index=False))


# 2. Eventos con minutos superiores a 120
altos = registro[registro["minute"] > 120]

print("\nTipos de evento con minuto superior a 120:")
print(
    altos.groupby(["minute", "event_type"]).size()
)


# 3. Eventos sin minuto pero con información
sin_minuto = registro[
    registro["minute"].isna() &
    registro["match_id"].notna() &
    registro["event_type"].notna()
]

print("\nEventos sin minuto recuperables:")
print("Cantidad:", len(sin_minuto))
print(sin_minuto.head(10).to_string(index=False))


# 4. Registros sin información básica
sin_identificacion = registro[
    registro["match_id"].isna() &
    registro["minute"].isna() &
    registro["event_type"].isna() &
    registro["team_id"].isna() &
    registro["player_id"].isna()
]

print("\nRegistros sin información básica:")
print(sin_identificacion.to_string(index=False))


# 5. Comprobar denominaciones de los eventos
print("\nTipos de evento existentes:")
print(registro["event_type"].value_counts(dropna=False))


# 6. Comprobar eventos de tanda de penaltis
tandas = registro[
    registro["event_type"].isin([
        "Penalty Shootout Goal",
        "Penalty Shootout Miss"
    ])
]

print("\nMinutos utilizados en tandas de penaltis:")
print(tandas["minute"].value_counts(dropna=False))



"""
APARTADO 5. Exclusión justificada de anomalías en eventos.
Se aplica tras las comprobaciones previas y se conservan los minutos vacíos
para la interpolación que exige el apartado 7.
"""

# Minutos negativos, superiores a 121 o minuto 121 fuera de una tanda.
tipos_penaltis = ["Penalty Shootout Goal", "Penalty Shootout Miss"]
negativos = eventos["minuto_evento"] < 0
excesivos = eventos["minuto_evento"] > 121
minuto_121_incorrecto = (
    (eventos["minuto_evento"] == 121)
    & ~eventos["tipo_evento"].isin(tipos_penaltis)
)

# Registros sin partido ni tipo de evento: no se pueden identificar.
# No se descartan los que únicamente tienen minuto ausente.
sin_informacion = eventos["index_partido"].isna() & eventos["tipo_evento"].isna()

eliminar = (negativos | excesivos | minuto_121_incorrecto | sin_informacion).fillna(False)
print("\nEventos excluidos por anomalías:", int(eliminar.sum()))
print(eventos.loc[eliminar])
eventos = eventos.loc[~eliminar].copy()

# Se unifican categorías equivalentes de revisión VAR.
eventos["tipo_evento"] = eventos["tipo_evento"].replace({"Review VAR": "VAR Review"})

# Eliminar únicamente copias totalmente idénticas del registro de origen,
# nunca eventos distintos que casualmente coinciden en minuto y jugador.
# Conservamos la correspondencia con el orden original del CSV hasta finalizar.
registro_valido = registro.loc[eventos.index - 1]
duplicados_exactos = registro_valido.duplicated(keep="first")
print("Copias exactas de eventos excluidas:", int(duplicados_exactos.sum()))
eventos = eventos.iloc[(~duplicados_exactos).to_numpy()].copy()

# Volver a enumerar los eventos como exige el enunciado.
eventos.index = range(1, len(eventos) + 1)
eventos.index.name = "index_evento"

# Comprobación final de las decisiones de limpieza.
print("\nEventos restantes:", len(eventos))
print("Minutos ausentes conservados:", eventos["minuto_evento"].isna().sum())
print("Tipos de eventos:")
print(eventos["tipo_evento"].value_counts(dropna=False))
print("Referencias a partidos inexistentes:", (
    eventos["index_partido"].notna() &
    ~eventos["index_partido"].isin(partidos.index)
).sum())

# Comprobaciones adicionales de coherencia tras la limpieza.
print("\nPaíses después de normalizar:")
print(partidos["pais_partido"].value_counts(dropna=False))

# Un índice con nombres puede repetirse cuando dos personas se llaman igual.
# Mostramos esos casos, pero no eliminamos jugadores por coincidencia de nombre:
# las fuentes originales permiten distinguirlos mediante player_id.
nombres_repetidos = jugadores.index.duplicated(keep=False)
print("\nNombres repetidos en jugadores (revisar con player_id):")
print(jugadores.loc[nombres_repetidos, ["seleccion_nacional", "posicion"]])

# Los ceros son válidos numéricamente en la escala de 0 a 10, pero pueden
# codificar falta de evaluación en jugadores con muy pocos minutos.
# Los diagnosticamos sin convertirlos automáticamente en ausentes; la decisión
# deberá justificarse antes de la regresión del apartado 7.
calificaciones_cero = jugadores["calificacion_media"].eq(0).fillna(False)
print("\nCalificaciones iguales a cero:", int(calificaciones_cero.sum()))
print(jugadores.loc[calificaciones_cero, ["seleccion_nacional", "minutos_jugados", "calificacion_media"]])




import re
from datetime import datetime

"""
6. Homogeneización de fechas mediante expresiones regulares.
Se identifica el patrón de cada fecha y se expresa como dd/mm/aaaa.
Se conservan los datos originales en matches_2026.
"""

meses = {
    "jan": 1, "january": 1, "ene": 1, "enero": 1,
    "feb": 2, "february": 2, "febrero": 2,
    "mar": 3, "march": 3, "marzo": 3,
    "apr": 4, "april": 4, "abr": 4, "abril": 4,
    "may": 5, "mayo": 5,
    "jun": 6, "june": 6, "junio": 6,
    "jul": 7, "july": 7, "julio": 7,
    "aug": 8, "august": 8, "ago": 8, "agosto": 8,
    "sep": 9, "september": 9, "septiembre": 9,
    "oct": 10, "october": 10, "octubre": 10,
    "nov": 11, "november": 11, "noviembre": 11,
    "dec": 12, "december": 12, "dic": 12, "diciembre": 12
}

def convertir_fecha(fecha, indice):
    fecha = str(fecha).strip()

    # dd/mm/aaaa, salvo los tres casos ambiguos del formato americano mm/dd/aaaa.
    if re.fullmatch(r"\d{2}/\d{2}/\d{4}", fecha):
        primero, segundo, anio = map(int, fecha.split("/"))
        if indice in [3, 87, 99]:
            mes, dia = primero, segundo
        else:
            dia, mes = primero, segundo

    # mm-dd-aaaa (americano, como 06-18-2026).
    elif re.fullmatch(r"\d{2}-\d{2}-\d{4}", fecha):
        mes, dia, anio = map(int, fecha.split("-"))

    # dd.mm.aaaa.
    elif re.fullmatch(r"\d{2}\.\d{2}\.\d{4}", fecha):
        dia, mes, anio = map(int, fecha.split("."))

    # aaaammdd.
    elif re.fullmatch(r"\d{8}", fecha):
        anio, mes, dia = int(fecha[:4]), int(fecha[4:6]), int(fecha[6:8])

    # Fecha ISO con hora (la hora se elimina porque solo se pide el día).
    elif re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", fecha):
        anio, mes, dia = map(int, fecha[:10].split("-"))

    # dd-mmm-aa: 13-jun-26.
    elif re.fullmatch(r"\d{1,2}-[a-zA-Z]{3}-\d{2}", fecha):
        parte = fecha.lower().split("-")
        dia, mes, anio = int(parte[0]), meses[parte[1]], 2000 + int(parte[2])

    # d de mes de aaaa: 14 de junio de 2026.
    elif re.fullmatch(r"\d{1,2} de [a-zA-Z]+ de \d{4}", fecha, flags=re.IGNORECASE):
        parte = fecha.lower().split(" de ")
        dia, mes, anio = int(parte[0]), meses[parte[1]], int(parte[2])

    # d Mes aaaa: 12 June 2026.
    elif re.fullmatch(r"\d{1,2} [a-zA-Z]+ \d{4}", fecha):
        parte = fecha.lower().split()
        dia, mes, anio = int(parte[0]), meses[parte[1]], int(parte[2])

    # Mes d, aaaa: June 13, 2026.
    elif re.fullmatch(r"[a-zA-Z]+ \d{1,2}, \d{4}", fecha):
        parte = fecha.lower().replace(",", "").split()
        dia, mes, anio = int(parte[1]), meses[parte[0]], int(parte[2])

    # Mmm d aaaa: Jun 14 2026.
    elif re.fullmatch(r"[a-zA-Z]{3} \d{1,2} \d{4}", fecha):
        parte = fecha.lower().split()
        dia, mes, anio = int(parte[1]), meses[parte[0]], int(parte[2])

    else:
        raise ValueError(f"Formato no reconocido en el partido {indice}: {fecha}")

    # datetime verifica que el día y el mes formen una fecha real.
    return datetime(anio, mes, dia).strftime("%d/%m/%Y")

# Se modifica únicamente la columna exigida en el enunciado.
for indice in partidos.index:
    partidos.loc[indice, "fecha_partido"] = convertir_fecha(
        partidos.loc[indice, "fecha_partido"], indice
    )

print("\n========== APARTADO 6. FECHAS HOMOGÉNEAS ==========")
print(partidos[["fecha_partido"]].head(15))
print("Fechas pendientes:", partidos["fecha_partido"].isna().sum())
print("Fechas en formato dd/mm/aaaa:", partidos["fecha_partido"].str.fullmatch(r"\d{2}/\d{2}/\d{4}").sum())
print("Partido 3:", partidos.loc[3, "fecha_partido"])
print("Partido 87:", partidos.loc[87, "fecha_partido"])
print("Partido 99:", partidos.loc[99, "fecha_partido"])
