from sqlalchemy import create_engine
import Database.info as info
def getBotDBEngine():
    uri = "mysql+pymysql://" + info.user + ":" + info.password + "@" + info.host + "/" + info.database
    return create_engine(uri)