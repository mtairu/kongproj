import datetime
from pydantic import BaseModel
from typing import Optional, Union, Any


class TReport(BaseModel):
    active: int
    admin_note: str
    create_date: datetime.datetime
    date: Any
    detail_text: str
    first_name: str
    idcard: str
    last_active: str
    last_name: str
    price: int
    product: str
    province_id: int
    report_code: str
    report_id: int
    user_contact: str
    user_contact_number: Optional[Union[int, str]]
    user_id: int
    website: str

