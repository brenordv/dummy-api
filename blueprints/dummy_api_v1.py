# -*- coding: utf-8 -*-

from flask import Blueprint, jsonify, request, Response

from utils.generators import get_sha256
from dummy.database import USERS, CATALOG, CD_CATALOG
from dummy.database import convert_user_to_xml


api_v1 = Blueprint("api_v1", "api_v1", url_prefix="/api/v1")


def process_fetch(response_data, use_xml):
    """
    Encapsulating data processing routines.
    :param response_data: data that will be sent back.
    :param use_xml: should use xml
    :return: processed string.
    """
    try:
        if use_xml:
            return Response(convert_user_to_xml(users=response_data), mimetype="text/xml"), 200
        else:
            return jsonify(response_data)

    except KeyError as why_ke:
        return jsonify(str(why_ke)), 500
    except Exception as why_e:
        return jsonify(str(why_e)), 500


@api_v1.route("/ping", methods=["GET", "POST"])
def ping():
    """
    Alive check for the API. No matter what you send or which method you use.
    This route will always respond: Ping? Pong!
    :return: string containing the phrase: Ping? Pong!
    """

    try:

        return jsonify("Ping? Pong!")
    except Exception as why_e:

        return jsonify(why_e), 500


@api_v1.route("/echo", methods=["POST"])
def echo():
    """
    Method used to test how Python is handling PowerBuilder requests.
    Will decode data sent from PB and return it to the requester.
    :return: Decoded data sent from the requester.
    """

    try:
        return request.data.decode("utf-8"), 200

    except UnicodeDecodeError as why_ude:
        return str(why_ude), 500

    except Exception as why_e:
        return str(why_e), 500


@api_v1.route("/hashme", methods=["GET", "POST"])
def gen_hash():
    """
    Returns a random SHA256 hash.
    :return: string with a sha256 hash
    """
    try:
        return Response(get_sha256(), mimetype="text/plain"), 200

    except Exception as why_e:
        return str(why_e), 500


@api_v1.route("/users", methods=["GET"])
def get_users():
    """
    Returns a list of users.
    The Format argument can be used to define if the return is a json or xml.
    """
    try:
        is_xml = request.args.get("format", "json").strip().lower() == "xml"
        if is_xml:
            return Response(convert_user_to_xml(users=USERS), mimetype="text/xml"), 200
        else:
            return jsonify(USERS)

    except KeyError as why_ke:
        return jsonify(str(why_ke)), 500
    except Exception as why_e:
        return jsonify(str(why_e)), 500


@api_v1.route("/catalog", methods=["GET"])
def get_catalog():
    """
    Returns the catalog used in XML handling post.
    http://raccoon.ninja/pt/dev-pt/usando-xpath-para-manipular-xml-python/
    """
    try:
        is_xml = request.args.get("format", "json").strip().lower() == "xml"
        if is_xml:
            return Response(CATALOG["xml"], mimetype="text/xml"), 200
        else:
            return jsonify(CATALOG["json"])

    except KeyError as why_ke:
        return jsonify(str(why_ke)), 500
    except Exception as why_e:
        return jsonify(str(why_e)), 500


@api_v1.route("/cdcatalog", methods=["GET"])
def get_cd_catalog():
    """
    Returns the catalog used in XML handling post.
    http://raccoon.ninja/pt/dev-pt/manipulando-xml-com-python/
    """
    try:
        is_xml = request.args.get("format", "json").strip().lower() == "xml"
        if is_xml:
            return Response(CD_CATALOG["xml"], mimetype="text/xml"), 200
        else:
            return jsonify(CD_CATALOG["json"])

    except KeyError as why_ke:
        return jsonify(str(why_ke)), 500
    except Exception as why_e:
        return jsonify(str(why_e)), 500
