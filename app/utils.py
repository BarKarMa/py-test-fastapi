import hashlib
from app.config import SECRT_KEY

def get_password_hash(password: str) -> str:
  return hashlib.sha256(f'{SECRT_KEY}{password}'.encode('utf8')).hexdigest()

