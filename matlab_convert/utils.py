# -*- coding: utf-8 -*-
"""
Created on Thu Jan 04 10:35:33 2018

@author: ldh
"""
# utils.py
import datetime as dt
import numpy as np
import pandas as pd


def array_decorator(func):
    return np.frompyfunc(func,1,1)

@array_decorator
def time_matlab2py(date_time_ordinal):
    '''
    Convert matlab format of time or datetime to the format of python.
    Accurate to 1 second.
    
    Parameters
    -----------
    date_time_ordinal
        the matlab format of ordianl time.
    
    Returns
    --------
    python normal format of time like YYYY-mm-dd HH:MM:SS
    
    Notes
    -------
    0      736819.593056    600340  36.4200 2017-05-04 14:14:00
    1      736819.593750    600340  36.3999 2017-05-04 14:15:00
    2      736819.594444    600340  36.3500 2017-05-04 14:16:00
    3      736819.595139    600340  36.3100 2017-05-04 14:17:00
    4      736819.595833    600340  36.2299 2017-05-04 14:18:00
    5      736819.596528    600340  36.1899 2017-05-04 14:19:00
    '''
    
    int_part = int(date_time_ordinal)
    float_part = date_time_ordinal - int_part
    seconds = int(float_part * 24 * 60 * 60) + 1
    
    date_part = dt.datetime.fromordinal(int_part - 366 )
    time_part = dt.timedelta(seconds = seconds) 
    date_time = date_part + time_part
    time_adjustor = pd.offsets.DateOffset(second = 0,microsecond = 0)
    date_time = date_time + time_adjustor
    return date_time

@array_decorator
def time_py2matlab(date_time):
    '''
    Convert normal format of time to matlab ordianl time.
    Accurate to 1 second.
    
    Parameters
    -----------
    date_time
        the normal datetime like '2017-05-04 14:15:36'
        
    Returns
    ---------
    matlab ordinal format of time.
    '''
    date_time_obj = dt.datetime.strptime(date_time,'%Y-%m-%d %H:%M:%S')
    int_part = date_time_obj.date().toordinal() + 366
    time_part = date_time_obj.time()
    float_part = time_part.hour * 60.0 * 60.0 + time_part.minute * 60.0 + time_part.second
    float_part = float_part / 86400.0
    return int_part + float_part

if __name__ == '__main__':
    a = time_py2matlab(pd.Series(['2017-05-04 14:15:36','2017-05-04 14:18:00']))
    b = time_py2matlab(['2017-05-04 14:15:36','2017-05-04 14:18:00'])

    



