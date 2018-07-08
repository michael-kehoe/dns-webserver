from flask import Blueprint

bp = Blueprint('api', __name__)

from dnsserver.api import dns_query, query
