from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.activator.service_start_activator import ServiceStartActivator
from app.activator.service_stop_activator import ServiceStopActivator
from app.config.config_manager import ConfigManager
from app.controller.syscheck_controller import router as sys_check_router

settings = ConfigManager()

@asynccontextmanager
async def lifespan(app: FastAPI):
    await ServiceStartActivator().doStart()
    yield
    await ServiceStopActivator().doStop()


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(sys_check_router)

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=settings.AP_PORT)
