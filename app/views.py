from aiohttp import web
from model import Session, UserModel, AdvertModel
from sqlalchemy.exc import IntegrityError
from errors import BadRequest, NotFound
from validation import register_schema, advert_schema, validate_data


async def register(request):
    json_data = await request.json()
    user = validate_data(json_data, register_schema)
    with Session() as session:
        new_user = UserModel(**user)
        session.add(new_user)
        try:
            session.commit()
        except IntegrityError:
            raise BadRequest("Email уже существует")
        return web.json_response({
            "user_id": new_user.user_id,
            "email": new_user.email,
            "password": new_user.password
        })


class AdvertView(web.View):

    async def get(self):
        id = self.request.match_info['id']
        with Session() as session:
            advert = session.query(AdvertModel).get(id)
            if advert is None:
                raise NotFound("Пользователь не найден")
            return web.json_response({
                "id": advert.advert_id,
                "title": advert.title,
                "description": advert.description,
                "created_time": str(advert.created_time),
                "author": advert.author
            })

    async def post(self):
        json_data = await self.request.json()
        advert_data = validate_data(json_data, advert_schema)
        with Session() as session:
            advert = AdvertModel(**advert_data)
            session.add(advert)
            session.commit()
            return web.json_response({
                "id": advert.advert_id,
                "title": advert.title,
                "description": advert.description,
                "created_time": str(advert.created_time),
                "author": advert.author
            })

    async def delete(self):
        id = self.request.match_info['id']
        with Session() as session:
            advert = session.query(AdvertModel).get(id)
            if advert is None:
                raise NotFound("Пользователь не найден")
            else:
                session.delete(advert)
                session.commit()
                return web.json_response({"Статус": "Удален"})

    async def patch(self):
        id = self.request.match_info['id']
        json_data = await self.request.json()
        advert_data = validate_data(json_data, advert_schema)
        with Session() as session:
            advert = session.query(AdvertModel).get(id)
            for field, val in advert_data.items():
                setattr(advert, field, val)
            session.add(advert)
            session.commit()
            return web.json_response({
                "id": advert.advert_id,
                "title": advert.title,
                "description": advert.description,
                "created_time": str(advert.created_time),
                "author": advert.author
                })
