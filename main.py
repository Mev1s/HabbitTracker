import asyncio
from app.database.setup import create_tables
from app.API.routes.app import create_app

app = create_app()


async def main():
    await create_tables()


if __name__ == "__main__":
    asyncio.run(main())
