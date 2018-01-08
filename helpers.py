import csv
import requests
import json

from flask import redirect, render_template, request, session
from functools import wraps


def lookup(ing):
    """Looks up recipes with the ing typed in by user"""
    API_KEY = "ad80a2237cbf79b038de84b0cf097901"
    url = "http://food2fork.com/api/search?key=" + API_KEY + "&q=chocolate+" + ing
    r = requests.get(url)
    return json.loads(r.text)["recipes"]


def apology(message, code=400):
    """Renders message as an apology to user."""
    return render_template("apology.html", top=code, bottom=message), code
