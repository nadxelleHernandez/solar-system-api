from flask import Blueprint, jsonify, abort, make_response,request
from app.models.moon import Moon
from app.models.planet import Planet

from app import db
from app.routes.helpers import validate_model, validate_request_body

moons_bp = Blueprint("moons_bp", __name__, url_prefix="/moons")
required_attributes = [ "name","size", "description", "gravity" ]

@moons_bp.route("",methods=["GET"])
def get_all_moons():
    moon_query = Moon.query  
    
    name_query = request.args.get("moon_name")
    if name_query:
        moon_query = moon_query.filter(Moon.name.ilike(f"%{name_query}%"))

    sort_query = request.args.get("sort")
    if sort_query:
        if sort_query == "desc":
            moon_query = moon_query.order_by(Moon.name.desc())
        else:
            moon_query = moon_query.order_by(Moon.name.asc())

    moons = moon_query.all()
    moons_response = []
    for moon in moons:
        moons_response.append(moon.to_dict())
    return jsonify(moons_response)
                
@moons_bp.route("/<moon_id>",methods=["GET"])
def get_moon(moon_id):
    moon = validate_model(Moon, moon_id)
    moon_info = moon.to_dict()
    moon_info["planet"] = moon.planet.name
    return jsonify(moon_info)

@moons_bp.route("/<moon_id>",methods=["PUT"])
def update_moon(moon_id):
    moon_info = validate_model(Moon, moon_id)
    request_body = request.get_json(silent=True)  
    validate_request_body(request_body, required_attributes)

    moon_info.name = request_body["name"]
    moon_info.description= request_body["description"]
    moon_info.size = request_body["size"]
    moon_info.gravity = request_body["gravity"]

    db.session.commit()
    
    return make_response(jsonify(f"Moon {moon_info.name} successfully updated"), 200)

@moons_bp.route("/<moon_id>",methods=["DELETE"])
def delete_moon(moon_id):
    moon_info = validate_model(Moon, moon_id)
    
    db.session.delete(moon_info)
    db.session.commit()
    
    return make_response(jsonify(f"Moon {moon_info.name} successfully deleted"), 200)
