row_record = '217.168.17.5 - - [ 17/May/2015:08:05:12 +0000] "GET /downloads/product_2 HTTP/1.1" 200 3316 "-" "-"'
r1 = row_record.split() [0]
r2 = row_record.split() [4]
print(r1,",",r2)