>>> l = [1,2,3,4]

>>> map(lambda x:x,  l)
[1, 2, 3, 4]
>>> map(lambda x: x**2,  l)
[1, 4, 9, 16]
>>> reduce(lambda x,y: x+y,  l)


# Word count
text_rdd = sc.textFile("hdfs://ip-10-186-164-81:8022/user/luckow/input/")
text_rdd.collect()
text_rdd.count()

text_rdd.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1)).reduceByKey(lambda x,y: x+y).collect()

# NASA
text_rdd = sc.textFile("hdfs://ip-10-186-164-81:8022/user/luckow/input-nasa/")
text_rdd.filter(lambda x: len(x)>8).map(lambda x: (x.split()[-2],1)).reduceByKey(lambda x,y: x+y).collect()