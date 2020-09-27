row_record = '217.168.17.5 - - [ 17/May/2015:08:05:12 +0000] "GET /downloads/product_2 HTTP/1.1" 200 3316 "-" "-"'
split = row_record.split()
r1 = split [0]
r2 = split [4]
r3 = split [6]
r4 = split [7]
print('remote_IP_address:',r1, '\nrequest_datetime:',r2, '\nrequest_method:',r3, '\nrequested_resource:',r4)

