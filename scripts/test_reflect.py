import sqlalchemy

# Paramètres de connexion à la base de données
schema = 'test_schema'
ip = '132.207.44.77'
port = '3306'
dialecte = 'mysql'
connecteur = 'pymysql'

nom = 'emilejetzer'
mdp = 'testtest'

url = f'{dialecte}+{connecteur}://{nom}:{mdp}@{ip}:{port}/{schema}'

# Connexion à la base de données
engine = sqlalchemy.create_engine(url, encoding='utf-8')

# Réflexion de la structure de la base de données
md = sqlalchemy.MetaData(schema=schema)
md.reflect(engine)

tables = tuple(md.tables.keys())
for i, t in enumerate(tables):
    print(f'[{i}] {t}')

t = tables[3] # tables[int(input('Quelle table?'))]

commande = sqlalchemy.select(md.tables[t])
print(commande)
with engine.begin() as connexion:
    résultat = connexion.execute(commande)

for iden, local, desc in résultat:
    local = sqlalchemy.select(md.tables[tables[4]].columns['porte'])\
            .where(md.tables[tables[4]].columns['idlocaux'] == local)
    with engine.begin() as connexion:
        local = next(connexion.execute(local))[0]
    print(iden, local, desc)

