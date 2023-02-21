# 'with' context manager

data_stream = None
try:
    data_stream = open("./myfile.txt")
    for text in data_stream:
        print(text)
except Exception as e:
    print(e)
finally:
    if data_stream is not None:
        data_stream.close()
