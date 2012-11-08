# -*- coding: utf-8 -*-

from j5.OS import datetime_tz
import datetime

def test_compare_tz_first():
    a = datetime.datetime(2012,3,4,1,2,3)
    b = datetime_tz.datetime_tz(2012,3,4,1,2,3)
    assert a == b

def test_compare_tz_second():
    a = datetime.datetime(2012,3,4,1,2,3)
    b = datetime_tz.datetime_tz(2012,3,4,1,2,3)
    assert b == a

def test_compare_greater():
    a = datetime.datetime(2012,3,4,3,2,3)
    b = datetime_tz.datetime_tz(2012,3,4,1,2,3)
    assert a > b
    assert a >= b
    a = datetime.datetime(2012,3,3,3,2,3)
    assert b > a
    assert b >= a

def test_compare_less():
    a = datetime.datetime(2012,3,4,3,2,3)
    b = datetime_tz.datetime_tz(2012,3,4,1,2,3)
    assert b < a
    assert b <= a
    a = datetime.datetime(2012,3,3,3,2,3)
    assert a < b
    assert a <= b

def test_compare_notequal():
    a = datetime.datetime(2012,3,4,3,2,3)
    b = datetime_tz.datetime_tz(2012,3,4,1,2,3)
    assert a != b
    assert b != a

