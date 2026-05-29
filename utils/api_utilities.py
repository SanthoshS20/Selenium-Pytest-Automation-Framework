import requests


def make_api_request(method, url, params, json, data, headers, files, timeout):
    try:
        response = requests.request(method=method, url=url, params=params, json=json, data=data, headers=headers,
                                    files=files, timeout=timeout)
        response.raise_for_status()
        return response
    except requests.HTTPError as http_err:
        raise Exception(f"HTTP error occurred: {http_err}")
    except Exception as err:
        raise Exception(f"An error occurred: {err}")


def read_json_data_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            json_data = json.load(file)
        return json_data
    except FileNotFoundError:
        raise Exception(f"file not found: {file_path}")
    except Exception as err:
        raise Exception(f"An error occurred while reading JSON data: {err}")
