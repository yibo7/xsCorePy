from sqlalchemy.testing import in_

from XsCore.db import DbDal
from tests.db.UserEntity import UserEntity

"""
你可以这样扩展某个表的操作功能
"""


class UserDal(DbDal):
    def __init__(self):
        DbDal.__init__(self, UserEntity)

    def getIdIn(self, ids: [int]):
        """
        查询指定id列表的记录
        :param ids: 指定id
        :return:
        """
        users = self.getList(UserEntity.id.in_(ids))
        return users
