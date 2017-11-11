import mistune


file = open("/Users/yuanxiansen/Desktop/school_affair/Y2:1/CSE101/ASS/ASS3/README.md", "rb")
string_result = file.read().decode("utf-8")
test = mistune.markdown(string_result)
print(test)