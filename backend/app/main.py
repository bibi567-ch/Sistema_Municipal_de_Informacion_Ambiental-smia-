from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.database.connection import Base, engine
from app.modules.auth.router import router as auth_router
from app.modules.ciudadano.router import router as ciudadano_router  # ← NUEVO

# Crear tablas automáticamente
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    description="Sistema Municipal de Información Ambiental — GAMLP",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar routers
app.include_router(auth_router,      prefix="/api/v1")
app.include_router(ciudadano_router, prefix="/api/v1")  # ← NUEVO

@app.get("/")
def root():
    return {
        "sistema": settings.APP_NAME,
        "version": settings.VERSION,
        "estado": "operativo",
        "docs": "/api/docs"
    }

@app.get("/health")
def health():
    return {"status": "ok"}




    