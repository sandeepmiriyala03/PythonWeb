from sqlalchemy import create_engine

connection_string = (
    "postgresql+psycopg2://"
    "neondb_owner:npg_5J0HaXlALTBE"
    "@ep-orange-hill-atrmkf0s-pooler.c-9.us-east-1.aws.neon.tech"
    "/neondb"
    "?sslmode=require&channel_binding=require"
)

engine = create_engine(
    connection_string,
    echo=True
)

