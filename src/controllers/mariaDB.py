from flask import render_template,request, redirect, url_for
import src.config.g as g
from src import app
from src.config.db import createDB, installDB,listarBases
import json

