import sys
import json
import requests


HR = "message me"
HR_URL = "http://api.hackerrank.com/checker/submission.json"

LANG = {"java8": 43, "java7": 3,
        "python2": 5, "python3": 30,
        "c": 1, "cpp": 2}


if len(sys.argv) < 4:
    print("usage:")
    print("python3 hackerrank.py [source_file] [testcase_file] [language]")
    print("supported languages: " + str(",".join(x for x in LANG)))
else:
    test_code = sys.argv[1]
    test_in = sys.argv[2]
    test_lang = sys.argv[3]

    source_text = "".join(line for line in open(test_code))
    test_in_str = "".join(line for line in open(test_in))
    language = LANG[test_lang]

    data = {"source": source_text,
            "lang": language,
            "api_key": HR,
            "testcases": json.dumps([test_in_str]),
            "wait": "false"}

    response = requests.post(HR_URL, data=data).json()

    for key in response["result"]:
        print(key, response["result"][key])
