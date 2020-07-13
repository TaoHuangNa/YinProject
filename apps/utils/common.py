#!/usr/bin/env python
# encoding: utf-8
"""
@project = YinProject
@file = common
@author = Tao Huang
@create_time = 2020/06/28 15:21
"""
import json
import uuid

from apps.utils.aliyun_sms_send import send_sms


def get_uuid():
    """
    # 获取新的uuid
    """
    return uuid.uuid4().hex


def send__sms(mobile, model, params):
    print(mobile)
    print(model)
    print(params)
    __business_id = get_uuid()
    # 暂时注释
    sms_status = send_sms(__business_id, mobile, "赞多多", model, params)
    print(sms_status)
    sms_status = json.loads(sms_status.decode('utf-8'))
    # sms_status = {'Code': 'OK'}
    return sms_status
# __business_id = uuid.uuid1()
# params = "{\"code\":\"5645\"}"
# print(send_sms(__business_id, "18864838025", "尚企云链", "SMS_152447430", params))
# print(send_sms(__business_id, "18864838025", "赞多多", "SMS_194050695", params))
