from typing import Annotated

from fastapi import FastAPI, Query, Depends

from logify.db import get_database
from logify.types import RequestLog
from immudb import ImmudbClient
from starlette_prometheus import metrics, PrometheusMiddleware
from prometheus_client import Counter


app = FastAPI()

app.add_middleware(PrometheusMiddleware)
app.add_route("/metrics/", metrics)

LOGS = Counter("logs_stored", "logs stored")


@app.post("/logs")
def store_logs(
    logs: list[RequestLog], db: Annotated[ImmudbClient, Depends(get_database)]
):
    LOGS.inc(len(logs))
    db.sqlExec(
        "INSERT INTO logs (created, log) VALUES (@created, @log)",
        {"created": logs[0].date_time, "log": logs[0].log.encode("utf-8")},
    )


@app.get("/logs")
def get_logs(
    db: Annotated[ImmudbClient, Depends(get_database)],
    last: int = Query(default=0, description="Number of logs to return, 0=all"),
):
    result = db.sqlQuery(
        f"SELECT * FROM logs ORDER BY created DESC LIMIT {int(last)}",
    )
    return result
