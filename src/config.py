from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASE_PATH = BASE_DIR / "database" / "customer_platform.db"

MODEL_PATH = BASE_DIR / "models" / "customer_model.pkl"

DATA_PATH = BASE_DIR / "data" / "raw" / "marketing_campaign.csv"