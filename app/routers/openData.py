import datetime

from fastapi import APIRouter

from app.connections import (get_db_query_result,
                             get_json_from_google_spreadsheet_api)
from app.models.openData import NumericDataResponse

router = APIRouter()


def get_timestamp() -> str:
    return datetime.datetime.utcnow().isoformat()


@router.get("/cooperatives-number", tags=["open data"], response_model=NumericDataResponse)
async def cooperatives_number():
    sql_query = 'SELECT COUNT(*) FROM `ert2_usuarios` WHERE `estado`= 3'
    result = get_db_query_result(sql_query)
    return NumericDataResponse(
        value=result,
        unit="cooperativistas",
        timestamp=get_timestamp()
    )


@router.get("/contracts-number", tags=["open data"], response_model=NumericDataResponse)
async def contracts_number():
    sql_query = 'SELECT MAX(`numero_contrato`) FROM `ert2_contratos`;'
    result = get_db_query_result(sql_query)
    return NumericDataResponse(
        value=result,
        unit="contratos",
        timestamp=get_timestamp()
    )


@router.get("/anual-renewable-production", tags=["open data"], response_model=NumericDataResponse)
async def anual_renewable_production():
    spreadsheet_id = "1seoxuCSRtFLsGWPTgPibCEHuARsF1FlUecl3vLG2HWI"
    named_range = "anualProduction"
    result = get_json_from_google_spreadsheet_api(spreadsheet_id, named_range)
    return NumericDataResponse(
        value=result["values"][0][0],
        unit="kWh",
        timestamp=get_timestamp()
    )


@router.get("/pv-installations-number", tags=["open data"], response_model=NumericDataResponse)
async def pv_installations_number():
    spreadsheet_id = "1seoxuCSRtFLsGWPTgPibCEHuARsF1FlUecl3vLG2HWI"
    named_range = "installationsNumber"
    result = get_json_from_google_spreadsheet_api(spreadsheet_id, named_range)
    return NumericDataResponse(
        value=result["values"][0][0],
        unit="instalaciones",
        timestamp=get_timestamp()
    )


@router.get("/2023-contributions-campaing", tags=["open data"])
async def contributions_campaign():
    sql_query = 'SELECT SUM(importe) as importe_total FROM `ert2_capitalsocial_v2` WHERE campana=5;'
    total_ammount = get_db_query_result(sql_query)
    sql_query = 'SELECT COUNT(*) as numero_participantes FROM `ert2_capitalsocial_v2` WHERE campana=5;'
    contributors_number = get_db_query_result(sql_query)
    return {
        "total_ammount": total_ammount,
        "contributors_number": contributors_number,
    }
