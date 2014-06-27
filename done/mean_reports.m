%% Here we are actually calculating the no of reports rated per year as well 
%% as no of reports rated per analyst per year
%% for those analyst who are in a particular range say 100-200 total reports and
%% their stay was between 1-3 yrs for a period of 13 years. THis analysis 
%% has been done monthly as well as yearly.


clc; clear;
conn=database('finance','finance','iof2014','org.postgresql.Driver','jdbc:postgresql://localhost:5432/finance');

disp(['Enter the maximum and minimum no of reports a person could have.',char(10),'P.S.: First enter the minimum in range and then maximum.'])
mini=input('')
maxi=input('')

mini=num2str(mini); maxi=num2str(maxi);
disp(['Enter the range of stay of person at Moodys.',char(10), 'P.S. Enter minimum and then maximum'])
exmi=input('')
exma=input('')

exmi=num2str(exmi); exma=num2str(exma);

disp(['Do you want analysis', char(10),'1. Monthwise',char(10),'2. Yearwise',char(10)])
choice=input('')

switch choice
    case 2
        for i=2000:2013
            a=num2str(i);
            n=[a,'-','12','-','31']; %generating proper date
            m=[a,'-','01','-','01'];
       
            sql=['SELECT COUNT(*) FROM RATINGS1 WHERE RATINGS_DATE> ''',m,''' AND RATINGS_DATE<=''',n,''' AND (A1_NAME IN (SELECT A1_NAME FROM FULL_INFO WHERE TOTAL_REPORTS>=',maxi,' AND TOTAL_REPORTS<',mini,' AND ( (LAST_REPORT-FIRST_REPORT)/365 :: FLOAT>',exmi,') AND ( (LAST_REPORT-FIRST_REPORT)/365 :: FLOAT<=',exma,')) OR A2_NAME IN (SELECT A1_NAME FROM FULL_INFO WHERE TOTAL_REPORTS>=',mini,' AND TOTAL_REPORTS<',maxi,' AND ( (LAST_REPORT-FIRST_REPORT)/365 :: FLOAT>',exmi,') AND ( (LAST_REPORT-FIRST_REPORT)/365 :: FLOAT<=',exma,')));'];
            cursor=exec(conn, sql);
            cursor=fetch(cursor);
            data=cursor.data;
            g(i-2000+1)=cell2mat(data(1,1))
        
            sql=['SELECT COUNT(TEMP.A1_NAME) FROM ((SELECT DISTINCT A1_NAME FROM RATINGS1 WHERE  RATINGS_DATE> ''',m,''' AND RATINGS_DATE<=''',n,''' UNION SELECT DISTINCT A2_NAME FROM RATINGS1 WHERE RATINGS_DATE> ''',m,''' AND RATINGS_DATE<=''',n,''') INTERSECT SELECT A1_NAME FROM FULL_INFO WHERE TOTAL_REPORTS>=',mini,' AND TOTAL_REPORTS<',maxi,'  AND ( (LAST_REPORT-FIRST_REPORT)/365 :: FLOAT>',exmi,') AND ( (LAST_REPORT-FIRST_REPORT)/365 :: FLOAT<=',exma,')) AS TEMP;'];
            cursor=exec(conn, sql);
            cursor=fetch(cursor);
            data1=cursor.data;
            t(i-2000+1)=cell2mat(data1(1,1))
        
        end
        figure(1)
        plot(g./t)
        title(['no of reports rated per analyst for every year by people having between ',mini,' and ',maxi,' reports and exp. between ',exmi,' and ',exma,' years'])
        xlabel('Years from 2000 to 2013')
        ylabel('No of companies rated per analyst')
        
        figure(2)
        plot(g)
        title(['no of reports rated for every year by people having between ',mini,' and ',maxi,' reports and exp. between ',exmi,' and ',exma,' years'])
        xlabel('Years from 2000 to 2013')
        ylabel('No of companies rated')
        
        
    case 1
        for i=2000:2013
            for j=1:12
                p=(i-2000)*12+j;
                k=eomday(i,j);
                a=num2str(i);
                b=num2str(j);
                c=num2str(k);
                
                n=[a,'-',b,'-',c]; %generating proper date
                m=[a,'-',b,'-','01'];
                
                sql=['SELECT COUNT(*) FROM RATINGS1 WHERE RATINGS_DATE> ''',m,''' AND RATINGS_DATE<=''',n,''' AND (A1_NAME IN (SELECT A1_NAME FROM FULL_INFO WHERE TOTAL_REPORTS>=',maxi,' AND TOTAL_REPORTS<',mini,' AND ( (LAST_REPORT-FIRST_REPORT)/365 :: FLOAT>',exmi,') AND ( (LAST_REPORT-FIRST_REPORT)/365 :: FLOAT<=',exma,')) OR A2_NAME IN (SELECT A1_NAME FROM FULL_INFO WHERE TOTAL_REPORTS>=',mini,' AND TOTAL_REPORTS<',maxi,' AND ( (LAST_REPORT-FIRST_REPORT)/365 :: FLOAT>',exmi,') AND ( (LAST_REPORT-FIRST_REPORT)/365 :: FLOAT<=',exma,')));'];
                cursor=exec(conn, sql);
                cursor=fetch(cursor);
                data=cursor.data;
                g(p)=cell2mat(data(1,1))
        
                sql=['SELECT COUNT(TEMP.A1_NAME) FROM ((SELECT DISTINCT A1_NAME FROM RATINGS1 WHERE  RATINGS_DATE> ''',m,''' AND RATINGS_DATE<=''',n,''' UNION SELECT DISTINCT A2_NAME FROM RATINGS1 WHERE RATINGS_DATE> ''',m,''' AND RATINGS_DATE<=''',n,''') INTERSECT SELECT A1_NAME FROM FULL_INFO WHERE TOTAL_REPORTS>=',mini,' AND TOTAL_REPORTS<',maxi,'  AND ( (LAST_REPORT-FIRST_REPORT)/365 :: FLOAT>',exmi,') AND ( (LAST_REPORT-FIRST_REPORT)/365 :: FLOAT<=',exma,')) AS TEMP;'];
                cursor=exec(conn, sql);
                cursor=fetch(cursor);
                data1=cursor.data;
                t(p)=cell2mat(data1(1,1))
                
            end
        end
       
        v=(g./t);
        figure(1)
        plot(v(7:end-5))
        title(['no of reports rated per analyst for every month by people having between ',mini,' and ',maxi,' reports and exp. between ',exmi,' and ',exma,' years'])
        xlabel('Months from JULY 2000 to JULY 2013')
        ylabel('No of companies rated per analyst')
        
        figure(2)
        plot(g(7:end-5))
        title(['no of reports rated for every month by people having between ',mini,' and ',maxi,' reports and exp. between ',exmi,' and ',exma,' years'])
        xlabel('Months from JULY 2000 to JULY 2013')
        ylabel('No of companies rated')
        
        
end


   


