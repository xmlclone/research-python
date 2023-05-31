```python
import json
from jsonpath import jsonpath

# 假设resp是requests的响应对象
jsonpath(resp.json(), '$.body')[0]

text = '''
{
    "code": "200",
    "message": "success",
    "body": {
        "list": [
            {
                "createdTime": "2023-05-29T06:02:16.231Z",
                "updatedTime": "2023-05-29T06:02:16.231Z",
                "id": "64743fe899dbe06476f47162",
                "name": "ystest_auto_org2",
                "description": "ystest_auto_org2",
                "orgId": "",
                "userCount": 0,
                "adminAccount": null,
                "default": false
            },
            {
                "createdTime": "2023-05-29T06:02:16.173Z",
                "updatedTime": "2023-05-29T06:02:16.173Z",
                "id": "64743fe899dbe06476f47161",
                "name": "ystest_auto_org1",
                "description": "ystest_auto_org1",
                "orgId": "",
                "userCount": 0,
                "adminAccount": null,
                "default": false
            },
            {
                "createdTime": "2023-05-29T02:56:29.265Z",
                "updatedTime": "2023-05-29T02:56:29.265Z",
                "id": "6474145d99dbe06476f47150",
                "name": "ytest_ts_xiexin_02",
                "description": "1",
                "orgId": "",
                "userCount": 1,
                "adminAccount": [
                    {
                        "id": "64643092ab7e2000206fdf12",
                        "account": "xiexin"
                    }
                ],
                "default": false
            }
        ],
        "page": 1,
        "pageSize": 10,
        "total": 37
    }
}
'''

obj = json.loads(text)

# 获取list第一个元素
jsonpath(obj, '$.body.list[0]')

# 获取list下所有id元素
jsonpath(obj, "$.body.list[*].id")

# 获取id为6474145d99dbe06476f47150节点
jsonpath(obj, "$.body.list[?(@.id=='6474145d99dbe06476f47150')]")

# 获取id为6474145d99dbe06476f47150节点下userCount的值
jsonpath(obj, "$.body.list[?(@.id=='6474145d99dbe06476f47150')].userCount")

# 获取id为6474145d99dbe06476f47150节点下adminAccount节点下account为xiexin的节点
jsonpath(obj, "$.body.list[?(@.id=='6474145d99dbe06476f47150')].adminAccount[?(@.account=='xiexin')]")

# 获取id为6474145d99dbe06476f47150节点下adminAccount节点下account为xiexin的节点的id值
jsonpath(obj, "$.body.list[?(@.id=='6474145d99dbe06476f47150')].adminAccount[?(@.account=='xiexin')].id")
```