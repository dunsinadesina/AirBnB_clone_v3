#!/usr/bin/python3
"""he status of your API"""
import models
from models import storage
from models.base_model import BaseModel
from flask import jsonify
from api.v1.views import app_views


@app_views.route("/status", strict_slashes=False)
def returnapistatus():
	"""returns api status"""
	return jsonify(status="OK")
