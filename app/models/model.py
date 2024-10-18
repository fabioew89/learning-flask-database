from app import app
from app.models import db, Mapped, mapped_column

class Users(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, unique=True, nullable=False)
    username = Mapped[str] = mapped_column(unique=True, nullable=False)
    email = Mapped[str] = mapped_column(unique=True, nullable=False)

with app.app_context():
    db.create_all()
