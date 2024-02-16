from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from db import session
from typing import List
from models import DeviceInfo, LocationData, PlaylistData, PlaylistReview, Token, User

app= FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get('/')
def home():
    return { "message": "Hello World!"}

@app.get('/devices', response_model=List[dict])
def read_devices():
    devices = session.query(DeviceInfo).all()
    device_list = [device.to_dict() for device in devices]
    return device_list

@app.get('/locations', response_model=List[dict])
def read_locations():
    locations=session.query(LocationData).all()
    locations_list = [location.to_dict() for location in locations]
    return locations_list

@app.get('/playlists', response_model=List[dict])
def read_playlists():
    playlists=session.query(PlaylistData).all()
    playlist_list = [playlist.to_dict() for playlist in playlists]
    return playlist_list

@app.get('/reviews', response_model=List[dict])
def read_reviews():
    reviews=session.query(PlaylistReview).all()
    review_list = [review.to_dict() for review in reviews]
    return review_list 




