---
layout: page
title: Overview
tagline: 
---
{% include JB/setup %}


## Content

The ongoing data deluge, i.e. the generation of large volumes of data, driven
by the increasing digitalization of society and industry, leads to a
significant increase in demand for data storage, processing and analytics
within several industrial domains (see [McKinsey Big Data
Report](http://www.mckinsey.com/insights/mgi/research/technology_and_innovation/
big_data_the_next_frontier_fo r_innovation)). Enterprises are overwhelmed by
the need to store large amounts of transactional and machine-generated data
resulting from the customer, service and manufacturing processes. Examples of
machine-generated data are server logs as well as sensor data that is generated
in finer granularities and frequencies. Further, internal dataset are often
enriched with web and open data from social media, blogs or other open data
sources. The Internet of Things (IoT) will further blur the boundaries between
the physical and the digital world causing an even further increase in the
digital footprint of the world. In this course we will learn about Big Data
applications and their requirements. Further, we will discuss the core
infrastructure necessary to handle the large data volumes and analytical
problems.


## Announcements


<ul class="posts">
  {% for post in site.posts %}
    <li><span>{{ post.date | date_to_string }}</span> &raquo; <a href="{{ BASE_PATH }}{{ post.url }}">{{ post.title }}</a></li>
  {% endfor %}
</ul>


## Time

The course will be held on Mondays. The first class will take place on August 25 at 04:30 pm.


## Topics

This class will cover selected topics from the list below:

1. Big Data Resource Management: YARN, Mesos and Omega
1. NoSQL and Hadoop: Big Table and HBase 
1. Emerging Hadoop Processing Engines: TEZ, Spark and Tachyon
1. SQL on Hadoop: HAWQ, Impala, Hive/TEZ, Hive/Spark
1. Stream Processing (Storm, Spark Streaming) 
1. Data Governance and Security: Kerberos, Gateway Services, Data Lifecycle Management
1. Fault Tolerance: CAP Theorem, Eventual Consistency, Quorum Protocols, Apache Zookeeper, Reliable Hadoop Architectures
1. Amazon and Big Data: Elastic MapReduce, SimpleDB, DynamoDB 
1. Google Big Data Management: GFS, Megastore, Mesas and Spanner 
1. Google Analytics: Pregel and Dremel 
1. Advanced Analytics and Machine Learning (Apache Mahout, MLLib) 
1. Graph Processing Frameworks (Networkx, Graphx, Titan, GraphLab, Giraph)
1. Natural Language Processing 


## Material

Materials for this lecture will be published here.

* [Lecture Material](http://fara.cs.uni-potsdam.de/~luckow/fall-2014/)


## Reading Material

Please use the following literature as starting point for your research.


### 1. Introduction and Motivation

1. Tony Hey, Stewart Tansley, Kristin Tolle (Editors), The Fourth Paradigm, <http://research.microsoft.com/en-us/collaboration/fourthparadigm/>, 2009
1. Stephen Wolfram: A New Kind of Science, <http://www.wolframscience.com/>, 2002
1. DJ Patil, Data Jujitsu, O'Reilly, <http://oreillynet.com/oreilly/data/radarreports/data-jujitsu.csp>, 2012
1. Mike Loukides, What is data science, <http://radar.oreilly.com/2010/06/what-is-data-science.html> O'Reilly, 2010
1. Alon Halevy, Peter Norvig, and Fernando Pereira, The Unreasonable Effectiveness of Data, <http://googleresearch.blogspot.de/2009/03/unreasonable-effectiveness-of-data.html>, 2009
1. IDC/EMC Digital Universe Study, <http://www.emc.com/leadership/programs/digital-universe.htm>, 2011
1. McKinsey Global Institute, Big data: The next frontier for innovation, competition, and productivity, <http://www.mckinsey.com/insights/mgi/research/technology_and_innovation/big_data_the_next_frontier_for_innovation>, 2011
1. München Open Data, <http://www.muenchen.de/opendata>
1. Berlin Open Data, <http://daten.berlin.de/>
1. New York Open Data, <http://www.nyc.gov/html/data/about.html>
1. Alex Howard, Data for Public Good, <http://strata.oreilly.com/2012/02/data-public-good.html>, O'Reilly, 2012
1. Jonathan Gray, Liliana Bounegru, Lucy Chambers (editors), The Data Journalism Handbook,  <http://datajournalismhandbook.org/>, 2012

### 2. Distributed and Cloud Computing
1. Peter Mell and Tim Grance. The NIST Definition of Cloud Computing, <http://csrc.nist.gov/groups/SNS/cloud-computing/>
1. Michael Armbrust, Armando Fox, Rean Griffith, Anthony D. Joseph, Randy H. Katz, Andrew Konwinski, Gunho Lee, David A. Patterson, Ariel Rabkin, Ion Stoica, and Matei Zaharia. Above the clouds: A Berkeley View of Cloud Computing. Technical Report University of Berkley, 2009, <http://www.eecs.berkeley.edu/Pubs/TechRpts/2009/EECS-2009-28.pdf>
1. S. Jha, D. Katz, A. Luckow, A. Merzky, K. Stamou, Understanding Scientific Applications for Cloud Environments, submitted to book on Cloud Computing, <http://www.cct.lsu.edu/~sjha/select_publications/cloud_book_chapter.pdf>
1. Amazon Web Services, <http://aws.amazon.com>
1. Amazon Web Services Whitepaper, 2009, <http://awsmedia.s3.amazonaws.com/AWS_Overview_Whitepaper_120809.pdf>
1. Google App Engine. <http://code.google.com/appengine/>
1. Windows Azure. <http://www.microsoft.com/windowsazure/>
1. K. Keahey, I. Foster, T. Freeman, and X. Zhang. Virtual Workspaces: Achieving Quality of Service and Quality of Life in the Grid. Scientific Programming, 13(4):265–275, 2005.
1. Cloud Standards Wiki, <http://cloud-standards.org>
1. Amazon Security Whitepaper,  <http://awsmedia.s3.amazonaws.com/pdf/AWS_Security_Whitepaper.pdf>, 2009
1. Amazon Security Best Practices, 2010, <http://awsmedia.s3.amazonaws.com/Whitepaper_Security_Best_Practices_2010.pdf>
1. OAuth, <http://oauth.net/>
1. Cloud Computing Tutorial. <https://research.microsoft.com/en-us/projects/azure/sc09cc.ppsx>
1. Sriram Krishnan, Programming Windows Azure, O'Reilly, 2010.
1. Thorsten Claus, Daniel Kellmereit, Yasmin Narielvala, The Future of Cloud,
<http://thefutureofcloud.com/>


### 3. Big Data

1. Jeffrey Dean and Sanjay Ghemawat. MapReduce: Simplified Data Processing on Large Clusters. In OSDI’04: Proceedings of the 6th conference on Symposium on Operating Systems Design & Implementation, pages 137–150, Berkeley, CA, USA, 2004. USENIX  Association.
1. Sanjay Ghemawat, Howard Gobioff, and Shun-Tak Leung. The Google File System. SIGOPS Oper. Syst. Rev., 37(5):29–43, 2003.
1. Fay Chang, Jeffrey Dean, Sanjay Ghemawat, Wilson C. Hsieh, Deborah A. Wallach, Mike Burrows, Tushar Chandra, Andrew Fikes, and Robert E. Gruber. Bigtable: a distributed storage system for structured data. In OSDI ’06: Proceedings of the 7th USENIX Symposium on Operating Systems Design and Implementation, pages 15–15, Berkeley, CA, USA, 2006. USENIX Association
1. Shantenu Jha, Judy Qui, Andre Luckow, Geoffrey Fox, A Tale of Two Data-Intensive Paradigms: Applications, Abstractions, and Architectures, <http://arxiv.org/abs/1403.1528>, 2014
1. Eric Baldeschwieler et al., Apache Hadoop YARN: Yet Another Resource Negotiator, <https://www.cs.cmu.edu/~garth/15719/papers/yarn.pdf>
1. Tom White, Hadoop: The Definitive Guide, 3rd Edition, <http://shop.oreilly.com/product/0636920021773.do>
1. Hadoop: Open Source Implementation of MapReduce. <http://hadoop.apache.org/>
1. Hadoop File System. <http://hadoop.apache.org/common/docs/current/hdfs_design.html>
1. Hive Project: <http://hive.apache.org/>
1. Edward Capriolo, Dean Wampler and Jason Rutherglen, Programming Hive, O'Reilly Media, 2012
1. Pig Project, <http://pig.apache.org/>
1. Alan Gates, Programming Pig, 2011
1. Amazon Elastic MapReduce. <http://aws.amazon.com/elasticmapreduce/>
1. Hadoop on Azure. <https://www.hadooponazure.com/>
1. MapReduce: Patterns, Algorithms and Use Cases,  <http://highlyscalable.wordpress.com/2012/02/01/mapreduce-patterns/>
1. Apache HBase, <http://hadoop.apache.org/hbase/>
1. Apache Cassandra, <http://cassandra.apache.org/>
1. Amazon SimpleDB, <http://aws.amazon.com/simpledb/>
1. Jeffrey Dean et. al., Spanner: Google's Globally-Distributed Database, OSDI, 2012, <Spanner: Google's Globally-Distributed Database>
1. Sergey Melnik, Andrey Gubarev, Jing Jing Long, Geoffrey Romer, Shiva Shivakumar, Matt Tolton, Theo Vassilakis, Dremel: Interactive Analysis of Web-Scale Datasets, <http://research.google.com/pubs/pub36632.html>
1. Leslie Lamport, The Part-Time Parliament, <http://research.microsoft.com/en-us/um/people/lamport/pubs/lamport-paxos.pdf>
1. Hasso Plattner, Alexander Zeiler, In-Memory Data Management, Springer, 2011
1. Giuseppe DeCandia, Deniz Hastorun, Madan Jampani, Gunavardhan Kakulapati, Avinash Lakshman, Alex Pilchin, Swaminathan Sivasubramanian, Peter Vosshall and Werner Vogels. Dynamo: Amazon’s Highly Available Key-value Store, 2007, <http://s3.amazonaws.com/AllThingsDistributed/sosp/amazon-dynamo-sosp2007.pdf>
1. E. A. Brewer,  Towards robust distributed systems. <http://www.cs.berkeley.edu/~brewer/cs262b-2004/PODC-keynote.pdf> In Proceedings of the 19th Annual ACM Symposium on Principles of Distributed Computing (July 16-19, Portland, Oregon), 2000
1. Werner Vogels, Eventually Consistent - Revisited, <http://www.allthingsdistributed.com/2008/12/eventually_consistent.html>, 2008
1. Gedik, Bugra and Andrade, Henrique and Wu, Kun-Lung and Yu, Philip S. and Doo, Myungcheol, SPADE: The System S Declarative Stream Processing Engine, Proceedings of the 2008 ACM SIGMOD international conference on Management of data, 2008
1. IBM Infosphere Streams, <http://www-01.ibm.com/software/data/infosphere/streams/>
1. Twitter Storm, <http://storm-project.net/>
1. Apache Zookeeper, <http://zookeeper.apache.org/>
1. Cloudera, BranchReduce: Distributed Branch-and-Bound on YARN, <http://www.cloudera.com/resource/hadoop-summit-2012-branchreduce-distributed-branch-and-bound-on-yarn-presentation-slides/>
1. Jason Baker, Chris Bond, James C. Corbett, JJ Furman, Andrey Khorlin, James Larson,
Jean-Michel Leon, Yawei Li, Alexander Lloyd, Vadim Yushprakh, Megastore: Providing Scalable, Highly Available Storage for Interactive Services, 2011
1. Grzegorz Malewicz et.al., Pregel: a system for large-scale graph processing, <http://googleresearch.blogspot.de/2009/06/large-scale-graph-computing-at-google.html>, 2009
1. Joseph M. Hellerstein, Christopher Ré, Florian Schoppmann, Zhe Daisy Wang, Eugene Fratkin, Aleksander Gorajek, Kee Siong Ng, Caleb Welton, Xixuan Feng, Kun Li, Arun Kumar, The MADlib Analytics Library or MAD Skills, the SQL, Technical Report University of Berkley, <http://www.greenplum.com/sites/default/files/Madlib_Whitepaper.pdf>, 2012
1. Google App Engine Map Reduce, <http://code.google.com/p/appengine-mapreduce/>
1. Google Big Query, <https://developers.google.com/bigquery/>
1. Prediction API, <https://developers.google.com/prediction/>
1. Greenplum Database, <http://www.greenplum.com/products/greenplum-database>
1. Hortonworks, <http://www.hortonworks.com>
1. Cloudera, <http://www.cloudera.com>
1. MapR, <http://www.mapr.com>
1. Lars George, HBase: The Definitive Guide, O'Reilly, 2011
1. Lars George, HBase vs. BigTable Comparison, <http://www.larsgeorge.com/2009/11/hbase-vs-bigtable-comparison.html>, 2009
1. MapReduce Patterns, <http://highlyscalable.wordpress.com/2012/02/01/mapreduce-patterns/>
1. Lawrence Page and Sergey Brin and Rajeev Motwani and Terry Winograd, The PageRank Citation Ranking: Bringing Order to the Web, Stanford Technical Report, <http://ilpubs.stanford.edu:8090/422/>, 1999
1. M. Schatz, CloudBurst: Highly Sensitive Short Read Mapping with MapReduce, <http://sourceforge.net/apps/mediawiki/cloudburst-bio/index.php?title=CloudBurst>, 2009 
1. Apache Drill, <http://www.slideshare.net/jasonfrantz/drill-bay-area-hug-20120919/13>
1. Apache Flume, <http://flume.apache.org/>

### 4. Data Analytics
1. Apache Mahout, <http://mahout.apache.org>
1. Sean Owen, Robin Anil, Ted Dunning, and Ellen Friedman, Mahout in Action, Manning, 2011
1. Cloudera, Mahout, CDH3 and Recommendations, <http://www.cloudera.com/resource/hadoop-summit-2012-branchreduce-distributed-branch-and-bound-on-yarn-presentation-slides/>
1. Scikit Learn, <http://scikit-learn.org/>
1. Scikit Learn Tutorial, <http://www.youtube.com/watch?v=Zd5dfooZWG4&feature=player_embedded#!>
1. Jacob Perkins, Python Text Processing with NTLK 2.0 Cookbook, Packt Publishing, 2010
1. Steven Bird, Ewan Klein, and Edward Loper, Natural Language Processing with Python, O'Reilly, 2009
1. Greg Linden, Brent Smith, and Jeremy York, Amazon.com
Recommendations Item-to-Item Collaborative Filtering, IEEE Computer Society, 
2003
1. Toby Segaran, Programming Collective Intelligence, O'Reilly, 2007
1. Drew Conway, John Myles White, Machine Learning for Hackers, O'Reilly, 2012 
1. Test, Learn, Adapt: Developing Public Policy with Randomised Controlled Trials: <http://www.pacts.org.uk/docs/pdf-bank/TLA-1906126.pdf>
1. Jimmy Lin and Chris Dyer, Data-Intensive Text Processing with MapReduce, Morgan & Claypool Publishers, 2010, <http://mapreduce.cc/>
1. Stanford Large Network Dataset Collection, <http://snap.stanford.edu/data/index.html>
1. Sherif Skar, Processing large-scale graph data: A guide to current
technology,  <http://www.ibm.com/developerworks/library/os-giraph/os-giraph-pdf.pdf>
1. Graphx, <https://spark.apache.org/graphx/>
1.  UC Irvine Machine Learning Repository, <http://archive.ics.uci.edu/ml/datasets.html>

### 5. Visualization
1. Robert Kabacoff, R in Action, Manning, 2011
1. Hadley Wickham, ggplot2 - Elegant Graphics for Data Analysis, 2009
1. D3: Data-driven Documents, <http://d3js.org/>
1. Jeff Hammerbach, Toby Segaran, Beautiful Data, O'Reilly, 2009
1. Julie Steele, Noah Iliinsky, Beautiful Visualizations, O'Reilly, 2010


## Grading

This is a pass/fail course. Students will be able to enroll in the course for 1 to 3 credit hours.  

## Policies

***Late Instructor***
Your instructor will make every effort to be in class on time, or to inform you
of any delay or cancellation. In the unusual event that he should not arrive in
class or send word by 15 minutes from the class start time, the class is
officially cancelled.

***Attendance Policy***
Attendance will not be graded, but we will take note of who attends, including occasionally circulating a sign-up sheet during class. If you miss a class, you
are responsible for obtaining lecture notes, handouts, and homework assignments
from fellow students. In the event that you are truly sick with a contagious
condition such as the flu, please do not expose your fellow students and
instructors to such illnesses. 

***Academic Integrity***
“As members of the Clemson University community, we have inherited Thomas Green Clemson’s vision of this institution as a “high seminary of learning.” Fundamental to this vision is a mutual commitment to truthfulness, honor, and responsibility, without which we cannot earn the trust and respect of others. Furthermore, we recognize that academic dishonesty detracts from the value of a Clemson degree. Therefore, we shall not tolerate lying, cheating, or stealing in any form.”

The instructor takes academic integrity extremely seriously and expects students to do so too. Scientific progress requires scientists to be honest in reporting their methods and results, the extent of their own contributions, and to accurately represent the research and ideas of other scientists. Failures of academic integrity such as plagiarism (i.e., representing the ideas or words of another as if they are your own) are always an insult to instructors and other students. Cheating, plagiarism, and all other academic integrity violations will handle according to the University policies regarding classroom expectations and academic integrity violation, as specified at http://www.clemson.edu/academics/academic-integrity/

***Collaboration Policy*** 
In and out of class assignments are opportunities for learning and discovery. Collaboration between students on homework assignments in this class is permitted. Collaboration includes students working together to gain an understanding of course concepts, active discussions with the instructor and other people to learn about course material, and other activities in which a student is actively seeking to learn and understand the topics covered in the course. I do expect that you understand and can explain any homework solution that you submit, no matter how you worked on it. 

As has always been the case, however, plagiarism is not allowed. Taking assignments from other classmates or downloading completed assignments from websites is not allowed. These are activities that are simply meant to earn a score, not understand the course material. If you collaborate with other students in class or use sources other than those provided for everyone in the course (e.g., instructor, recommended textbook, the course web site, or the lectures) to help yourself learn and understand, then you must give appropriate credit to those collaborators and/or sources. As long as you acknowledge the collaboration that occurred, your grade will not be affected nor will you be charged with academic misconduct. On the other hand, a failure to acknowledge collaborations or give appropriate credit to sources of help (other than course materials or personnel as noted above) will be treated as plagiarism. 

***Contributorship Statement*** 
To ensure that you acknowledge contributions, collaborations and sources, you are required to include a contributorship statement at the beginning of every assignment that you submit. The statement should say: 
"I worked on this assignment alone, using only course materials." 
OR 
"I worked on this assignment with [give the names of the people you worked with]. My role in completing the assignment was [provide description of all your contributions], while [provide names of other collaborators] role in completing the assignment was [provide a description of their contributions]. We consulted related material that can be found at [cite any other materials not provided as course materials]." 
Any assignment that does not include a collaboration statement will not receive a grade until the statement is provided.


## Acknowledgements

![Amazon Web Services](http://awsmedia.s3.amazonaws.com/AWS_Logo_PoweredBy_127px.png)