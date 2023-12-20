from sqlalchemy import Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class   tb_tablet(Base):
    __tablename__ = 'tb_tablet'
    nama_tablet: Mapped[str] = mapped_column(primary_key=True)
    harga: Mapped[int] = mapped_column()
    ram: Mapped[int] = mapped_column()
    kapasitas_baterai: Mapped[int] = mapped_column()
    chipset: Mapped[int] = mapped_column()
    memori_internal: Mapped[int] = mapped_column()  
    
    def __repr__(self) -> str:
        return f"tb_tablet(nama_tablet={self.tablet!r}, harga={self.harga!r})"
