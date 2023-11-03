from fastapi import APIRouter

from fastapi.responses import FileResponse
from pypdf import PdfReader, PdfWriter
from models.utils import ReplacementValues
import os

router = APIRouter()


@router.post("/fill-rite-form/", tags=["utils"])
async def fill_form_endpoint(data: ReplacementValues):
    form_model_path = os.path.dirname(os.path.abspath(
        __file__)) + "/../files/Modelo_Memoria_RITE.pdf"
    try:
        replacement_values = data.data

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

        with open("Memoria RITE.pdf", "wb") as output_stream:
            writer.write(output_stream)

        return FileResponse("Memoria RITE.pdf", filename="Memoria RITE.pdf")

    except Exception as e:
        return str(e)
