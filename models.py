from sqlalchemy import Column, ForeignKey, Integer, String, Text, Boolean, TIMESTAMP, func, Index #double-check all imports
from sqlalchemy.orm import declarative_base
from db import engine

BaseModel=declarative_base()

class ToDictMixin:
    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class LocationData(BaseModel, ToDictMixin):
    __tablename__ = 'location_data'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    city = Column(String(50))
    state = Column(String(50))
    country = Column(String(50))
    zip_code = Column(String(20))
    created_at = Column(TIMESTAMP, default=func.now())

    __table_args__ = (Index('idx_zip_code', zip_code),) # Index on zip_code. No routes needed as it will be auto utilized

class PlaylistData(BaseModel, ToDictMixin):
    __tablename__ = 'playlist_data'

    playlist_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    playlist_name = Column(String(100), nullable=False)
    song = Column(String(100), nullable=False)
    album = Column(String(100))
    artist = Column(String(100))
    created_at = Column(TIMESTAMP, default=func.now())

class DeviceInfo(BaseModel, ToDictMixin):
    __tablename__ = 'device_info'

    device_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    screen_size = Column(String(50))
    network_connection = Column(String(50))
    device_type = Column(String(50))
    visitor_ip = Column(String(50))
    created_at = Column(TIMESTAMP, default=func.now())

class PlaylistReview(BaseModel, ToDictMixin):
    __tablename__ = 'playlist_reviews'

    review_id = Column(Integer, primary_key=True)
    playlist_id = Column(Integer, ForeignKey('playlist_data.playlist_id', ondelete='CASCADE'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    rating = Column(Integer, nullable=False)
    review_text = Column(Text)
    created_at = Column(TIMESTAMP, default=func.now())
    
class Token(BaseModel, ToDictMixin):
    __tablename__ = 'tokens'
    id = Column(Integer, primary_key=True) # verify setup
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False) # add on 
    access_token = str
    token_type = str

class User(BaseModel, ToDictMixin):
    id = Column(Integer, primary_key=True) # verify setup
    __tablename__ = 'users'
    username = str
    allow_location_tracking = Column(Boolean, default=True) # add on 
    default_zip_code = Column(String(20)) # add on 
    created_at = Column(TIMESTAMP, default=func.now()) # add on 
    
BaseModel.metadata.create_all(engine)
