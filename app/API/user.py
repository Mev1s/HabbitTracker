# standard
import typing

# custom
import fastapi
import pydantic

# project


app = fastapi.FastAPI(debug=True)


@app.get("/users")
async def get_users():
    return {"users": [{"id": 1, "name": ""}]}
