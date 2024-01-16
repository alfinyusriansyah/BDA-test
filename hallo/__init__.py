import requests
from flask import Flask, request, jsonify
import dotenv
import os
dotenv.load_dotenv()

PB_URL = os.environ.get("PB_URL")

def name():
    try :
        res = requests.get(f"{PB_URL}/api/collections/tes_bda/records")
        data = res.json()
        return jsonify(data)
    except Exception as e :
        return jsonify({"error": str(e)}), 500

def add_name():
    try :
        body = request.get_json()
        res = requests.post(f"{PB_URL}/api/collections/tes_bda/records", json=body)
        data = res.json()
        return jsonify (data), 201
    except Exception as e :
        return jsonify({"error": str(e)}), 500

def update_name(id):
    try :
        body = request.get_json()
        res = requests.patch(f"{PB_URL}/api/collections/tes_bda/records/{id}", json=body)
        data = res.json()
        status_code = res.status_code
        return jsonify (data), status_code
    except Exception as e :
        return jsonify({"error": str(e)}), 500  

def delete_name(id):
    try:
        res = requests.delete(f"{PB_URL}/api/collections/tes_bda/records/{id}")
        data = res.json()
        status_code = res.status_code
        return jsonify (data), status_code
    except Exception as e :
        return jsonify({"error": str(e)}), 500 

def view_name(id):
    try:
        res = requests.get(f"{PB_URL}/api/collections/tes_bda/records/{id}") 
        data = res.json()
        status_code = res.status_code
        return jsonify (data), status_code
    except Exception as e :
        return jsonify({"erro": str(e)}), 500    
        