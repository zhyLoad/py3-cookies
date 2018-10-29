import json

class JsonAndDict(object):
    def dict2Json(self,dict):
        return json.dumps(dict)
    def json2Dict(self,json_str):
        return json.loads(json_str)



jd = JsonAndDict()
d1 = {'name':'zhangsan','age':23,'home':'beijing'}
# Dict -> Json
json_str = jd.dict2Json(d1)
print('dict2Json = ',json_str)

# Json -> Dict
d2 = jd.json2Dict(json_str)
print('json2Dict d2[\'age\'] = ',d2['age'])





class Student(object):
    def __init__(self,name,age,home):
        self.name = name
        self.age = age
        self.home = home



s1 = Student('lisi',33,'tianjin')

# Object -> Json   : 方法：object->dict->Json
dict_s1 = {'name':s1.name,'age':s1.age,'home':s1.home}
json_str_1 = json.dumps(dict_s1)
print('Objcet to Json result : ',json_str_1)

# Json -> Object 方法:json ->dict -> object
dict_temp = jd.json2Dict(json_str_1)
s2 = Student(dict_temp['name'],dict_temp['age'],dict_temp['home'])
print('Json to Object result: ', s2.name)
