import mysql.connector
from mysql.connector import errorcode


class mysqlError:

    def __init__(self, error: mysql.connector.errors):
        super(mysqlError, self).__init__()
        self.error = error

    def errors(self, error):
        if error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            # TODO: make message here
            return "هناك خطأ ما في اسم المستخدم أو كلمة المرور"
        elif error.errno == errorcode.ER_BAD_DB_ERROR:
            # TODO: make message here
            return "قاعدة البيانات غير موجودة"
        elif error.errno == errorcode.CR_CONN_HOST_ERROR:
            # TODO: make message here
            return error.errno
        elif error.errno == errorcode.ER_TRUNCATED_WRONG_VALUE_FOR_FIELD:
            # TODO: make message here
            return f'you entered str value instead int value error line : {error.errno}'
        elif error.errno == errorcode.ER_WARN_DATA_OUT_OF_RANGE:
            # TODO: make message here
            return f'you entered long value sync file  : {error.errno}'
        elif error.errno == errorcode.ER_BAD_FIELD_ERROR:
            return f'Error from line   bad field error: {error.errno}'
        elif error.errno == errorcode.ER_NO_SUCH_TABLE:
            return f'Error from line : NO SUCH TABLE: {error.errno}'
        elif error.errno == errorcode.ER_WRONG_VALUE_COUNT_ON_ROW:
            return f'Error from line  values provided in the INSERT ' \
                   f'statement is f bigger or smaller than the number of columns the table has: {error.errno}'
        elif error.errno == errorcode.ER_PARSE_ERROR:
            return f'Error from line : PARSE ERROR: {error.errno}'
        elif error.errno == errorcode.ER_DUP_ENTRY:
            return f'Error from line : DUP ENTRY: {error.errno}'
        else:
            return f'Error from line : {error.errno}'
        # TODO: add more errors messages like error 1130

    def __str__(self):
        return self.errors(self.error)
