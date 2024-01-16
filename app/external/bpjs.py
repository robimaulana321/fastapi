from fastapi import APIRouter
from datetime import datetime
import requests
import json
import hashlib
import hmac
import base64

route = APIRouter()

addr = "https://ap1.rscm.co.id/index.php/"
    
headers = {
    'x-username': 'UMSI',
    'x-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX25tIjoiVU1TSSIsImtleV9hcGkiOiIwOTFhZTdhMjljNDc5NTg2MGY2OWI0MDc3ZThiNDMyYyJ9.WR8akcjm0VbkkykGoGo2ttOShS9z6Q1Pw7C2MjzlO0Y',
    'Content-Type': 'application/json'
}

# create signature
@route.get("/signature")
async def signature():
    # Define my and key as per question
    conspwd = bytes("rs123cm", 'UTF-8')
    consId  = bytes("1001", 'UTF-8')

    # timestamp
    current_dateTime = datetime.now()
    time_stamp = current_dateTime.timestamp()
    timestamp = bytes(int(time_stamp))
    # return int(time_stamp)   
     
    # signature 
    signature  = hmac.new(conspwd, msg=consId, digestmod=hashlib.sha256)
    signature1 = signature.digest()
    signature2 = base64.urlsafe_b64encode(signature1)

    body = json.dumps({
        "no_nik": "3271022411930002"
    })

    head = {
        "user_key":"7667cde7074611160336da515d9af9f7",
        "X-cons-id":consId,
        "X-timestamp":timestamp,
        "X-signature":signature2,
        "Content-Type": "application/json"
    }

    url = "https://new-apijkn.bpjs-kesehatan.go.id/vclaim-rest/no_nik"

    response = requests.request("GET", url, headers=head, data=body)
    return response.json()

# get kepesertaan bpjs by nik
@route.get("/nik/{no_nik}")
async def info_nik(no_nik:str):
    url = addr+"no_nik"

    body = json.dumps({
            "no_nik": no_nik
        })

    response = requests.request("GET", url, headers=headers, data=body)
    return response.json()

# get kepesertaan bpjs by no kartu bpjs
@route.get("/kartu/{no_kartu}")
async def info_kartu(no_kartu:str):
    url = addr+"no_kartu"

    body = json.dumps({
            "no_kartu": no_kartu
        })

    response = requests.request("GET", url, headers=headers, data=body)
    return response.json()

# get history kunjungan pelayanan
@route.get("/history_kunjungan/tgl_sep/{tgl_sep}/filter/{filter}")
async def history_kunjungan(tgl_sep:str,filter:str):
    url = addr+"history_kunjungan"

    body = json.dumps({
            "tgl_sep": tgl_sep,
            "filter": filter
        })

    response = requests.request("GET", url, headers=headers, data=body)
    return response.json()

# get sep by no sep bpjs
@route.get("/cari_sep/{no_sep}")
async def cari_sep(no_sep:str):
    url = addr+"carisep"

    body = json.dumps({
            "no_sep": no_sep
        })

    response = requests.request("GET", url, headers=headers, data=body)
    return response.json()

# get dpjp
@route.get("/dpjp/jenis/{jenis}/kode/{kode}")
async def dpjp(jenis:int,kode:str):
    url = addr+"dpjp"

    body = json.dumps({
            "jenis": jenis,
            "kode": kode
        })

    response = requests.request("GET", url, headers=headers, data=body)
    return response.json()

# get dpjp kontrol
@route.get("/dpjpkontrol/jenis/{jns_kontrol}/poli/{poli}/tgl/{tgl}")
async def dpjp_kontrol(jns_kontrol:int,poli:str,tgl:str):
    url = addr+"dpjpkontrol"

    body = json.dumps({
            "jns_kontrol": jns_kontrol,
            "poli": poli,
            "tgl": tgl
        })

    response = requests.request("GET", url, headers=headers, data=body)
    return response.json()