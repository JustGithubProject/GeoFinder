import requests
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")
API_KEY = "LaCywmlZJKIsk0YqzRhv5uxKNB628z74"


@app.get("/")
async def read_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/get_location/")
async def get_location(request: Request, city: str = Form(...)):
    url = f"https://www.mapquestapi.com/geocoding/v1/address?key={API_KEY}&location={city}"
    response = requests.get(url).json()
    if response["info"]["statuscode"] == 0:
        lat = response["results"][0]["locations"][0]["latLng"]["lat"]
        lon = response["results"][0]["locations"][0]["latLng"]["lng"]
        return templates.TemplateResponse("result.html",
                                          {"request": request, "city": city, "latitude": lat, "longitude": lon})
    else:
        return templates.TemplateResponse("error.html", {"request": request, "city": city})
