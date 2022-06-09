from math import floor

n_requests = [10, 50, 100,500]
urls = [
    "http://172.16.16.101:8889/rfc2616.pdf",
    "http://172.16.16.101:8889/testing.txt",
    "http://172.16.16.101:8889/pokijan.jpg"
]

for n_request in n_requests:
    for n_concurrent in [1, floor(n_request * 0.25), floor(n_request * 0.5), floor(n_request * 0.75), n_request]:
        for url in urls:
            print(f"ab -n {n_request} -c {n_concurrent} {url}")
        print("\n")