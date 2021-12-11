from fastapi import FastAPI, HTTPException
from .models import TbReport
from .typedefs import TReport


API = FastAPI()


@API.get("/reports")
def get_report_from_tb_reports_table(fname: str = None, lname: str = None):
    """Returns a matching name or list of matching names
    
    Most send request with a valid fname and lname or one of either.
    
    Valid Queries
    ------------
    lname=พลเดช&fname=วสันต์

    lname=พลเด

    fname=วสันต์
    """
    if fname == None and lname == None:
        raise HTTPException(status_code=400, detail="Missing fields")
    fname = fname or ''
    lname = lname or ''
    reports = (
        TbReport.select()
        .where(TbReport.first_name.contains(fname) | TbReport.last_name.contains(lname))
        .execute()
    )
    return [TReport(**report.__data__) for report in reports]
