from aiohttp import web
from views import register, AdvertView

app = web.Application()


app.add_routes([
    web.get("/advert/{id}", AdvertView),
    web.post("/advert", AdvertView),
    web.delete("/advert/{id}", AdvertView),
    web.patch("/advert/{id}", AdvertView),
    web.post("/register", register)
    ])


if __name__ == '__main__':
    web.run_app(app, host="127.0.0.1", port=5001)
