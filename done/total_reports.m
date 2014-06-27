clc; clear;
conn=database('finance','finance','iof2014','org.postgresql.Driver','jdbc:postgresql://localhost:5432/finance');
%% Here we are actually calculating the no of firms rated by analysts 
%% in a particular range say 100-200 for every year right from 2000-2013
%% But you need to change the range every time.

sql=['SELECT TO_CHAR(RATINGS_DATE,','''YYYY-MM''',') AS YEAR_MONTH, COUNT(*) AS TOTL_REPORTS  FROM RATINGS1 GROUP BY YEAR_MONTH ORDER BY YEAR_MONTH;'];
cursor=exec(conn, sql);
cursor=fetch(cursor);
data=cursor.data;
data
g=cell2mat(data(:,2))
t=char(data(:,1))
figure(1)
plot(g(3:end)/100)


        

