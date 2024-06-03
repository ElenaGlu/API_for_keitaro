from fastapi import FastAPI
from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise

import config as c

Tortoise.init_models(["models"], "models")

TORTOISE_ORM = {
    "connections": {
        "default": f"postgres://{c.DB_USER}:{c.DB_PASS}@{c.DB_HOST}:5432/{c.DB_NAME}",
    },
    "apps": {
        "models": {
            "models": ["models", "aerich.models"],
            "default_connection": "default",
        },
    },
    "use_tz": False,
}


def init_db(app: FastAPI) -> None:
    register_tortoise(
        app,
        config=TORTOISE_ORM,
        modules={"models": ["models", "aerich.models"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )
