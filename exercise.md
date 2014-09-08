---
layout: page
title: "Exercise"
description: ""
---
{% include JB/setup %}



# Infrastruktur

* Linux Cluster hosted at Amazon EC2
* Ubuntu 12.04
* Python 2.7.3, Python Documentation: <http://docs.python.org/>
* Hostname: `cloud.luckow-hm.de (54.83.41.227)`
* HDFS Web: <http://cloud.luckow-hm.de:50070/>


<br/>

# 1. Using SSH and Linux
<br/>
Data/Tools:
* Use an SSH client of your choice (e.g. Putty for Windows or SSH in your Linux/Mac OS Terminal)
* Data: `cloud.luckow-hm.de:/data/NASA_access_log_Jul95`


1. Please login into the Hadoop cluster on Amazon!

1. Answer the following questions using the command (`hadoop dfsadmin -report`):
    * How big is the Hadoop cluster?
    * How many data nodes are used?
    		
	
1. Upload the file `cloud.luckow-hm.de:/data/NASA_access_log_Jul95` to your HDFS home directory! How many blocks does HDFS

<br/>


# 2. Commandline Data Analytics
<br/>  

Data/Tools:
* <http://ita.ee.lbl.gov/html/contrib/NASA-HTTP.html>
* Commandline data tools <https://github.com/bitly/data_hacks>
* Data: `cloud.luckow-hm.de:/data/NASA_access_log_Jul95`
<br/> 

1. Use the commands `head`, `cat`, `uniq`, `wc`, `sort`, `find`, `xargs`, `awk` um die NASA Access Logs auszuwerten:

	1. Which page was called the most?
 	1. What was the most frequent return code?
	1. How many errors occured? What is the percentage of errors?

<br/> 
	
# 3. MapReduce Hello World

Data/Tools:
* `hadoop jar /opt/cloudera/parcels/CDH/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar wordcount`

1. Run the WordCount example of Hadoop:
	1. Create two test files containing text and upload them to HDFS!
	1. Use the MapReduce program WordCount for countint the words!


