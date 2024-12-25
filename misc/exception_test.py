# https://stackoverflow.com/questions/1278705/when-i-catch-an-exception-how-do-i-get-the-type-file-and-line-number
import os
import sys

try:
    print(5 / 0)
except Exception as e:
    print(sys.exc_info()[0].__name__, os.path.basename(sys.exc_info()[2].tb_frame.f_code.co_filename),
          sys.exc_info()[2].tb_lineno)
    print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)

# "Best (recommended) practice: replace all exc_type, exc_value, exc_traceback
# with sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2]
try:
    print()
    # raise NotImplementedError("No error")
except Exception as e:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(exc_type, fname, exc_tb.tb_lineno)
