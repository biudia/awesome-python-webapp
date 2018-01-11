import httplib,urllib,urllib2,re,time,json,gzip

# encoding:utf-8
import time
import re

##@outputSchema("requesttime:chararray")
def transfer_lib(lib_id):
    if len(lib_id)<6 : 
        new_id = str(int(lib_id)+700000)
        return new_id
    else : return lib_id

print transfer_lib('700')    