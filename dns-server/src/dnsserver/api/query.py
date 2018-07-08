import pprint
import dns.flags
import dns.rdatatype
import dns.resolver

from flask import jsonify, request

from dnsserver.api import bp


@bp.route('/query', methods=['GET'])
def query():
    # Get request arguments
    name = request.args.get('name')
    query_type = request.args.get('type')
    cd = request.args.get('cd', True)
    edns_client_subnet = request.remote_addr
    answers = dns.resolver.query(name, query_type)
    rd = True
    ra = True

    tc = False
    ad = False

    qname = dns.name.from_text(name)
    q = dns.message.make_query(qname, query_type)
    r = dns.query.udp(q, '172.22.194.101')
    print r
    print type(r)
    pprint.pprint(r.__dict__)
    print dns.flags.to_text(r.flags)
    answers = []
    print type(r.answer)
    for answer in r.answer:
        print answer
        print type(answer)
        print dir(answer)
        answers.append({'name': answer.name.to_text(),
                        'type': answer.rdtype,
                        'TTL': answer.ttl,
                        'data': '127.0.0.1'})
    print answers
    return jsonify({'Status': r.rcode(),
                    'TC': tc,
                    'RD': rd,
                    'RA': ra,
                    'AD': ad,
                    'CD': cd,
                    'Question': [{"name": name,
                                 "type": dns.rdatatype.from_text(query_type)}],
                    'Answer': answers,
                    'Additional': [],
                    'edns_client_subnet': edns_client_subnet})
