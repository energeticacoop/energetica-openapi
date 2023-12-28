from fastapi import APIRouter

from fastapi.responses import FileResponse
from pypdf import PdfReader, PdfWriter
from models.utils import ReplacementValues
import os

router = APIRouter()



def fill_form(form_model_path: str, output_filename: str, replacement_values: dict):
    try:
        reader = PdfReader(form_model_path)
        writer = PdfWriter()
        writer.append(reader)
        fields = reader.get_fields()

        for page in writer.pages:
            for field in fields:
                if fields[field].value and "{" in fields[field].value and fields[field].value in replacement_values:
                    writer.update_page_form_field_values(
                        page, {field: replacement_values[fields[field].value]}
                    )

        with open(output_filename, "wb") as output_stream:
            writer.write(output_stream)

        return FileResponse(output_filename, filename=output_filename)

    except Exception as e:
        return str(e)

@router.post("/fill-rite-form/", tags=["utils"])
async def fill_form_rite_endpoint(data: ReplacementValues):
    form_model_path = os.path.dirname(os.path.abspath(__file__)) + "/../files/Modelo_Memoria_RITE.pdf"
    return fill_form(form_model_path, "Memoria RITE.pdf", data.data)

@router.post("/fill-mge-form/", tags=["utils"])
async def fill_form_mge_endpoint(data: ReplacementValues):
    form_model_path = os.path.dirname(os.path.abspath(__file__)) + "/../files/Certificado_final_MGE.pdf"
    return fill_form(form_model_path, "Certificado MGE.pdf", data.data)
