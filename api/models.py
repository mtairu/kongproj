import os
from peewee import *


database = MySQLDatabase(
    user=os.environ["DB_USER"],
    password=os.environ["DB_PASS"],
    database=os.environ["DB_NAME"],
    host=os.environ["DB_HOST"],
)


class UnknownField(object):
    def __init__(self, *_, **__):
        pass


class BaseModel(Model):
    class Meta:
        database = database


class TbReport(BaseModel):
    active = IntegerField(constraints=[SQL("DEFAULT 1")])
    admin_note = TextField(null=True)
    create_date = CharField()
    date = CharField()
    detail_text = TextField(null=True)
    first_name = CharField(index=True)
    idcard = CharField(index=True, null=True)
    last_active = CharField()
    last_name = CharField(index=True)
    price = IntegerField()
    product = CharField()
    province_id = IntegerField()
    report_code = CharField()
    report_id = AutoField()
    user_contact = TextField(null=True)
    user_contact_number = TextField(null=True)
    user_id = IntegerField()
    website = CharField(null=True)

    class Meta:
        table_name = "tb_report"


class TbReportBank(BaseModel):
    bank_id = IntegerField(index=True)
    bank_number = CharField(index=True)
    report_bank_active = IntegerField(constraints=[SQL("DEFAULT 1")])
    report_bank_id = AutoField()
    report_id = IntegerField()

    class Meta:
        table_name = "tb_report_bank"
