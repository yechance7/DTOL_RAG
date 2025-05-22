from t2sql.controller.ingest_documentation import train_local
import asyncio
import logging

# set logging
logging.basicConfig(level=logging.INFO)

async def main():
    await train_local()

if __name__ == "__main__":
    asyncio.run(main())