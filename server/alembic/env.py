import os
import sys
from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

# -----------------------------------------------------------
# 1. SETUP PATH: Biar folder 'app' kebaca oleh Python
# -----------------------------------------------------------
# Ini naik 2 folder ke atas (dari alembic/env.py -> server/)
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

# 2. IMPORT CONFIG & MODEL
# Kita ambil settingan database dari file .env via config.py
from app.core.config import settings
# Kita ambil Base Model agar Alembic tahu struktur tabel
from app.db.base_class import Base
# Kita import model User supaya terdeteksi (WAJIB!)
from app.models.user import User

# this is the Alembic Config object
config = context.config

# Interpret the config file for Python logging.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# -----------------------------------------------------------
# 3. SET TARGET METADATA
# -----------------------------------------------------------
# Ini yang bikin Alembic tahu tabel apa aja yang harus dibuat
target_metadata = Base.metadata

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    # Kita paksa pakai URL dari .env, bukan dari alembic.ini
    url = settings.DATABASE_URL
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    
    # -----------------------------------------------------------
    # 4. INJECT DATABASE URL DARI .ENV (PENTING)
    # -----------------------------------------------------------
    # Kita override konfigurasi default biar baca password dari .env
    configuration = config.get_section(config.config_ini_section)
    configuration["sqlalchemy.url"] = settings.DATABASE_URL

    connectable = engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()