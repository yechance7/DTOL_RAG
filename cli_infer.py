import asyncio
import logging
import sys

from t2sql.agent import get_sql_agent
from t2sql.controller.make_answer import make_answer

# set logging
logging.basicConfig(level=logging.INFO)

agent = get_sql_agent()
async def main(question: str) -> str:
    sql = await make_answer(question, agent)
    print(f"result: {sql}")
    return sql

if __name__ == "__main__":
    stdin = sys.stdin.read()
    print(f"stdin:{stdin}")
    asyncio.run(main(stdin))