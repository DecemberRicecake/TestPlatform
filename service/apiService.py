import requests


def run_testcase(testcase):
    request = testcase['request']
    try:
        url = request['url']
        method = request['method']
        req_kwargs = {'proxies': request['proxies'], 'headers': request['headers'], 'json': request['json']}
    except Exception as e:
        print(e)

    resp_obj = requests.request(url=url, method=method, **req_kwargs)
    diff_content, resp_body = diff_response(resp_obj, testcase['response'])
    success = False if diff_content else True
    return success, diff_content, resp_body


def diff_response(resp_obj, expected_resp_json):
    try:
        resp_body = resp_obj.json()
    except Exception as e:
        print(e)
    cur_data = {
        'status_code': resp_obj.status_code,
        'body': resp_body}
    diff_content = diff_json(cur_data, expected_resp_json)
    return diff_content, resp_body


def diff_json(current_json, expected_json):
    json_diff = {}
    for key, expected_value in expected_json.items():
        value = check_json_value(current_json, key)
        if str(value) != str(expected_value):
            json_diff[key] = {
                'value': value,
                'expected': expected_value
            }
    return json_diff


def check_json_value(json_data, k):
    if isinstance(json_data, dict):
        for key in json_data:
            if key == k:
                value = json_data.get(key, None)
                return value
            elif isinstance(json_data[key], dict):
                value = check_json_value(json_data[key], k)
                if value is not None:
                    return value


'''if __name__ == '__main__':
    success1, diff_content1 = run_testcase(testcase1)
    print(success1)
    print(diff_content1)'''


