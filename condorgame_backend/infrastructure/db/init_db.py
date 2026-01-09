from sqlmodel import SQLModel, create_engine, Session

from condorgame_backend.utils.times import HOUR, DAY, MINUTE
from . import DbPredictionRepository
from .db_tables import ModelRow, LeaderboardRow, PredictionRow, PredictionConfigRow
from ...entities.prediction import PredictionConfig, PredictionParams

import os

DATABASE_URL = f"postgresql+psycopg2://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@" \
               f"{os.getenv('POSTGRES_HOST')}:{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"

engine = create_engine(DATABASE_URL)

HORIZON1 = 1 * HOUR
HORIZON2 = 1 * DAY

STEPS_H1 = (1 * MINUTE, 5 * MINUTE, 15 * MINUTE, 30 * MINUTE, 1 * HOUR)
STEPS_H2 = (5 * MINUTE, 1 * HOUR, 6 * HOUR, 24 * HOUR)

PREDICTION_INTERVAL_H1 = 12 * MINUTE
PREDICTION_INTERVAL_H2 = 1 * HOUR


def default_prediction_config():
    return [
        PredictionConfig(PredictionParams('BTC', HORIZON2, STEPS_H2), PREDICTION_INTERVAL_H2, True, 1),
        PredictionConfig(PredictionParams('BTC', HORIZON1, STEPS_H1), PREDICTION_INTERVAL_H1, True, 2),

        PredictionConfig(PredictionParams('ETH', HORIZON2, STEPS_H2), PREDICTION_INTERVAL_H2, True, 3),
        PredictionConfig(PredictionParams('ETH', HORIZON1, STEPS_H1), PREDICTION_INTERVAL_H1, True, 4),

        PredictionConfig(PredictionParams('XAUT', HORIZON2, STEPS_H2), PREDICTION_INTERVAL_H2, True, 5),
        PredictionConfig(PredictionParams('XAUT', HORIZON1, STEPS_H1), PREDICTION_INTERVAL_H1, True, 6),

        PredictionConfig(PredictionParams('SOL', HORIZON2, STEPS_H2), PREDICTION_INTERVAL_H2, True, 7),
        PredictionConfig(PredictionParams('SOL', HORIZON1, STEPS_H1), PREDICTION_INTERVAL_H1, True, 8),
    ]


def init_db() -> None:
    print("➡️  Creating tables if they do not exist...")
    SQLModel.metadata.create_all(engine)
    print("✅ Database initialization complete.")

    session = Session(engine)
    prediction_repo = DbPredictionRepository(session)

    # todo improve the update
    prediction_repo.delete_configs()
    prediction_repo.save_all_configs(default_prediction_config())


if __name__ == "__main__":
    init_db()
