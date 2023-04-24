from immudb import ImmudbClient


def get_database() -> ImmudbClient:
    client = ImmudbClient("127.0.0.1:3322")
    client.login("immudb", "immudb", "logify2")
    configure_database(client)
    return client


def configure_database(client: ImmudbClient):
    client.sqlExec(
        "CREATE TABLE IF NOT EXISTS logs ("
        "id INTEGER AUTO_INCREMENT, "
        "created TIMESTAMP, log BLOB[640], "
        "PRIMARY KEY (id))"
    )

    client.sqlExec("CREATE INDEX IF NOT EXISTS ON logs (created)")
