# coding: utf-8
__author__ = 'annika'
__date__ = '2019-01-29 19:51'

_status_flag='status'
_message_flag='message'

success_code_1=0
auth_failure_code=-1
parameters_missing_code=-2
empty_page_code=-3
unknow_error_code=-4
method_error_code=-5
type_error_code = -6

def success_msg(data=None):
	msg = {
		_status_flag: success_code_1,
		_message_flag: ''
	}
	if data is not None:
		msg.update(data)
	return msg

auth_failure_msg={
	_status_flag: auth_failure_code,
	_message_flag: u'身份验证失败',
}

parameters_missing_msg={
	_status_flag: parameters_missing_code,
	_message_flag: u'参数缺失',
}

empty_page_msg={
	_status_flag: empty_page_code,
	_message_flag: u'没有更多了',
}

def unknow_error_msg(e):
	return {
		_status_flag: unknow_error_code,
		_message_flag: e,
	}

def method_error_msg(method):
	return {
		_status_flag: method_error_code,
		_message_flag: 'Only'+method,
	}

def failure_msg(msg, status=unknow_error_code):
	return {
		_status_flag: status,
		_message_flag: msg,
	}
