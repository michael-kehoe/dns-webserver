import pprint
import socket

import dns.flags
import dns.rdatatype
import dns.resolver
import dns.message
from flask import jsonify, request, Response

from dnsserver.api import bp

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

@bp.route('/dns-query', methods=['GET'])
def dns_query():
    raw_query = request.args.get('dns')
    # message = dns.message.from_wire(raw_query)
    # print message
    sock.sendto(raw_query, ('172.22.194.101', 53))
    reply = sock.recv(1024)
    return Response(reply, mimetype='application/dns-message', headers={'content-length': len(reply)})
