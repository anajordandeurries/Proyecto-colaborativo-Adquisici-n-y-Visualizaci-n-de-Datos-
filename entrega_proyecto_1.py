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

    Entrega: 12 de Octubre 206

"""

# Realización de las exportaciones necesarias:
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from IPython.display import display


"""
1. Exploración inical de todos los documentos:
    Comenzaremos explorando todos los csv proporcionados para entender su contenido, formato y tamaño.
"""

# 1. 2001eurocopa_fem_stats.csv
femenino = pd.read_csv("2001eurocopa_fem_stats.csv")
display(femenino.head())
print("Dimensiones:", femenino.shape)
print("\nInformación del dataset:")
femenino.info()

print("\nResumen estadístico:")
display(femenino.describe(include="all"))


# 2. 2026match_lineups.csv
lineups = pd.read_csv("2026match_lineups.csv", sep = ";")

display(lineups.head())
print("Dimensiones:", lineups.shape)
print("\nInformación del dataset:")
lineups.info()

print("\nResumen estadístico:")
display(lineups.describe(include="all"))


# 3. 2026match_register.csv
registro = pd.read_csv("2026match_register.csv", sep = ";")

display(registro.head())
print("Dimensiones:", registro.shape)
print("\nInformación del dataset:")
registro.info()

print("\nResumen estadístico:")
display(registro.describe(include="all"))


# 4. 2026nationalteams.csv
equip_nacional = pd.read_csv("2026nationalteams.csv")

display(equip_nacional.head())
print("Dimensiones:", equip_nacional.shape)
print("\nInformación del dataset:")
equip_nacional.info()

print("\nResumen estadístico:")
display(equip_nacional.describe(include="all"))


# 5. 2026player_stats.csv
stats = pd.read_csv("2026player_stats.csv", sep = ";")

display(stats.head())
print("Dimensiones:", stats.shape)
print("\nInformación del dataset:")
stats.info()

print("\nResumen estadístico:")
display(stats.describe(include="all"))


# 6. 2026squads_and_players.csv
players = pd.read_csv("2026squads_and_players.csv", sep = ";")

display(players.head())
print("Dimensiones:", players.shape)
print("\nInformación del dataset:")
players.info()

print("\nResumen estadístico:")
display(players.describe(include="all"))


# 7. index_referees.csv
index_referees = pd.read_csv("index_referees.csv", sep = ";")

display(index_referees.head())
print("Dimensiones:", index_referees.shape)
print("\nInformación del dataset:")
index_referees.info()

print("\nResumen estadístico:")
display(index_referees.describe(include="all"))


# 8. matches_mundial202.csv
matches_202 = pd.read_csv("matches_mundial202.csv")

display(matches_202.head())
print("Dimensiones:", matches_202.shape)
print("\nInformación del dataset:")
matches_202.info()

print("\nResumen estadístico:")
display(matches_202.describe(include="all"))


# 9. matches_mundial2026.csv
matches_2026 = pd.read_csv("matches_mundial2026.csv", sep = ";")

display(matches_2026.head())
print("Dimensiones:", matches_2026.shape)
print("\nInformación del dataset:")
matches_2026.info()

print("\nResumen estadístico:")
display(matches_2026.describe(include="all"))


# 10. tournament_stages.csv
tournament = pd.read_csv("tournament_stages.csv")

display(tournament.head())
print("Dimensiones:", tournament.shape)
print("\nInformación del dataset:")
tournament.info()

print("\nResumen estadístico:")
display(tournament.describe(include="all"))


# 11. worldcup_venues.csv
venues = pd.read_csv("worldcup_venues.csv", sep = ";")

display(venues.head())
print("Dimensiones:", venues.shape)
print("\nInformación del dataset:")
venues.info()

print("\nResumen estadístico:")
display(venues.describe(include="all"))



"""
2. Crear las variables.
    Crearemos 3 DataFrames a los que posteriormente iremos añadiendo información.
"""
partidos = pd.DataFrame()
jugadores =  pd.DataFrame()
eventos =  pd.DataFrame()


"""  
3. Añadir información a las variables.
    A partir de los DataFrames importados, crearemos las variables partidsos, jugadores y eventos, con las columnas, los índices y los nombres
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

#hacemos esto para que map no falle, con los valores nulos.
selecciones_con_id = equip_nacional.dropna(subset=["team_id"])
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

#Asginar tipo de dato numérico y de txto
columnas_enteras_partidos = ["marcador_local", "marcador_visitante", "penalty_local", "penalty_visitante"]
columnas_texto_partidos = ["ronda", "estadio", "ciudad_partido", "pais_partido", "seleccion_local", "seleccion_visitante", "prorroga", "arbitro_partido"]

partidos[columnas_enteras_partidos] = partidos[columnas_enteras_partidos].astype("Int64")
partidos[columnas_texto_partidos] = partidos[columnas_texto_partidos].astype("string")

print(partidos.dtypes)

print(partidos)




# Ahora jugadores
jugadores["nombre_jugador"] = stats["player_name"]

#usamos la leyenda que hicimos antes para que no falle map.
jugadores["seleccion_nacional"] = stats["team_id"].map(leyenda_seleccion)

leyenda_club = dict(zip(players["player_id"], players["club_team"]))
jugadores["club_jugador"] = stats["player_id"].map(leyenda_club)

leyenda_partidos_seleccion = dict(zip(players["player_id"], players["caps"]))
jugadores["partidos_seleccion"] = stats["player_id"].map(leyenda_partidos_seleccion)

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
partidos = partidos.drop_duplicates()
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


# Duplicados en eventos, sin considerar su identificador
columnas_comparacion = ["match_id", "minute", "player_id", "event_type", "team_id"]

# Mostramos los casos con sus identificadores originales para revisarlos.
display(registro[registro.duplicated(subset=columnas_comparacion, keep=False)])

# Aplicamos este criterio si hemos confirmado que son copias del mismo evento.
columnas_comparacion_eventos = ["index_partido", "minuto_evento", "nombre_jugador","tipo_evento", "seleccion_evento"]

print("Eventos repetidos:", eventos.duplicated(subset=columnas_comparacion_eventos).sum())
eventos = eventos.drop_duplicates(subset=columnas_comparacion_eventos)

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

columnas_texto_jugadores.remove("nombre_jugador")
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

eventos[columnas_texto_eventos] = (eventos[columnas_texto_eventos].fillna("Desconocido"))

print("Nulos en eventos después del tratamiento:")
print(eventos.isna().sum())