from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import delete_tables, create_tables
from router import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("База очищена")
    await create_tables()
    print("База создана")
    yield
    print("База закрыта",)


app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)

import os

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)