import os

from fastapi import APIRouter
from fastapi.responses import FileResponse
from pypdf import PdfReader, PdfWriter

from app.models.utils import MgeReplacementValues, RiteReplacementValues

router = APIRouter()


def fill_form(form_model_path: str, output_filename: str, replacement_value_opening_character: str, replacement_values: dict):
    try:
        reader = PdfReader(form_model_path)
        writer = PdfWriter()
        writer.append(reader)
        fields = reader.get_fields()

        for page in writer.pages:
            for field in fields:
                if fields[field].value and replacement_value_opening_character in fields[field].value and fields[field].value in replacement_values:
                    writer.update_page_form_field_values(
                        page, {field: replacement_values[fields[field].value]}
                    )

        with open(output_filename, "wb") as output_stream:
            writer.write(output_stream)

        return FileResponse(output_filename, filename=output_filename)

    except Exception as e:
        return str(e)


@router.post("/fill-rite-form/", tags=["utils"])
async def fill_form_rite_endpoint(data: RiteReplacementValues):
    form_model_path = os.path.dirname(os.path.abspath(
        __file__)) + "/../files/Modelo_Memoria_RITE.pdf"
    replacement_value_opening_character = "{"
    return fill_form(form_model_path, "Memoria RITE.pdf", replacement_value_opening_character, data.data)


@router.post("/fill-mge-form/", tags=["utils"])
async def fill_form_mge_endpoint(data: MgeReplacementValues):
    form_model_path = os.path.dirname(os.path.abspath(
        __file__)) + "/../files/Certificado_final_MGE.pdf"
    replacement_value_opening_character = "<"
    return fill_form(form_model_path, "Certificado MGE.pdf", replacement_value_opening_character, data.data)
