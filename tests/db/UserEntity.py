
from sqlalchemy import Column, Integer, String

from XsCore.db import Base

"""
        实体类一般只需要定义数据字段映射，字段的类型一般是如下十一种：

        第一种：Integer     |   age = Column(Integer)
        第二种：String      |   name = Column(String(20))
        第三种：Float       |   price = Column(Float)
        第四种：DECIMAL     |   Column(DECIMAL(7,3))
        第五种：Boolean     |   delete = Column(Boolean)
        第六种：Enum        |   sex = Column(Enum("男","女"))
        第七种：Date        |   create_time = Column(Date)
        第八种：DateTime    |   create_time = Column(DateTime)
        第九种：Time        |   create_time = Column(Time)
        第十种：Text        |   content = Column(Text)
        第十一种：LongText   |   content = Column(LONGTEXT)

"""


class UserEntity(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50))
    password = Column(String(32))
