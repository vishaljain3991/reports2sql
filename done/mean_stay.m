%% In this file, we are calculating avg stay for employees of Moodys 
%% dependent on the no of reports an employee has over stay at Moodys and
%% his years of stay at Moodys

clc; clear;
conn=database('finance','finance','iof2014','org.postgresql.Driver','jdbc:postgresql://localhost:5432/finance');
disp(['Enter the maximum and minimum no of reports a person could have.',char(10),'P.S.: First enter the minimum in range and then maximum.'])
mini=input('')
maxi=input('')

disp(['Enter the range of stay of person at Moodys.',char(10), 'P.S. Enter minimum and then maximum'])
exmi=input('')
exma=input('')

disp(['Do you want analysis', char(10),'1. Monthwise',char(10),'2. Yearwise',char(10),'3. Monthwise with experience condition', char(10),'4. Yearwise with experience condition'])
choice=input('')

switch choice
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
                %sql=['SELECT AVG((''',n,'''- FIRST_REPORT)/365 :: FLOAT) AS AVG_STAY FROM M_STAY WHERE A1_NAME NOT IN (SELECT A1_NAME FROM M_STAY WHERE LAST_REPORT<=''',m,''' OR FIRST_REPORT>=''',n,''');'];
        
                sql=['SELECT COUNT(*),AVG((''',n,'''-FIRST_REPORT)/365::FLOAT) AS STAY FROM FULL_INFO WHERE A1_NAME IN (SELECT A1_NAME FROM M_STAY WHERE A1_NAME NOT IN (SELECT A1_NAME FROM M_STAY WHERE LAST_REPORT<=''',m,''' OR FIRST_REPORT>=''',n,''')','INTERSECT',' SELECT A1_NAME FROM FULL_INFO WHERE TOTAL_REPORTS<',num2str(maxi),' AND TOTAL_REPORTS>=',num2str(mini),');']
                cursor=exec(conn, sql);
                cursor=fetch(cursor);
                data=cursor.data;
                g(p)=cell2mat(data(1,2))
                t(p)=cell2mat(data(1,1))
            end
        end

        figure(1)
        plot(g(7:end-5))
        title(['avg stay of employees having<= ',num2str(maxi),' reports and > ',num2str(mini),'report'])
        xlabel('Months from JULY 2000 to JULY 2013')
        ylabel('Years')
        
        figure(2)
        plot(t(7:end-5))
        title(['no.of of employees during an year having<= ',num2str(maxi),' reports and > ',num2str(mini),' report'])
        xlabel('Months from JULY 2000 to JULY 2013')
        ylabel('No of employees')
        
    case 3
        for i=2000:2013
            for j=1:12
                p=(i-2000)*12+j;
                k=eomday(i,j);
                a=num2str(i);
                b=num2str(j);
                c=num2str(k);
                n=[a,'-',b,'-',c]; %generating proper date
                m=[a,'-',b,'-','01'];
        %sql=['SELECT AVG((''',n,'''- FIRST_REPORT)/365 :: FLOAT) AS AVG_STAY FROM M_STAY WHERE A1_NAME NOT IN (SELECT A1_NAME FROM M_STAY WHERE LAST_REPORT<=''',m,''' OR FIRST_REPORT>=''',n,''');'];
        
                sql=['SELECT COUNT(*),AVG((LAST_REPORT-FIRST_REPORT)/365::FLOAT) AS STAY FROM FULL_INFO WHERE A1_NAME IN (SELECT A1_NAME FROM M_STAY WHERE A1_NAME NOT IN (SELECT A1_NAME FROM M_STAY WHERE LAST_REPORT<=''',m,''' OR FIRST_REPORT>=''',n,''')','INTERSECT',' SELECT A1_NAME FROM FULL_INFO WHERE TOTAL_REPORTS<=',num2str(maxi),' AND TOTAL_REPORTS>',num2str(mini),' AND ( (LAST_REPORT-FIRST_REPORT)/365 :: FLOAT>',num2str(exmi),' AND (LAST_REPORT-FIRST_REPORT)/365 :: FLOAT<=',num2str(exma),' ));']
                cursor=exec(conn, sql);
                cursor=fetch(cursor);
                data=cursor.data
                g(p)=cell2mat(data(1,2))
                t(p)=cell2mat(data(1,1))
            end
        end

        figure(1)
        plot(g(7:end-5))
        title(['avg stay of employees having<=',num2str(maxi),' reports and >',num2str(mini),' report and stay between',num2str(exmi),' and ',num2str(exma),' years'])
        xlabel('Months from JULY 2000 to JULY 2013')
        ylabel('Years')
        
        figure(2)
        plot(t(7:end-5))
        title(['no. of employees having<=',num2str(maxi),' reports and >',num2str(mini),' report and stay between ',num2str(exmi),' and ',num2str(exma), ' years'])
        xlabel('Months from JULY 2000 to JULY 2013')
        ylabel('No of employees')
        
    case 4
        
        for i=2000:2013
                a=num2str(i);
                n=[a,'-','12','-','31']; %generating proper date
                m=[a,'-','01','-','01'];
                %sql=['SELECT AVG((''',n,'''- FIRST_REPORT)/365 :: FLOAT) AS AVG_STAY FROM M_STAY WHERE A1_NAME NOT IN (SELECT A1_NAME FROM M_STAY WHERE LAST_REPORT<=''',m,''' OR FIRST_REPORT>=''',n,''');'];
        
                sql=['SELECT COUNT(*),AVG((''',n,'''-FIRST_REPORT)/365::FLOAT) AS STAY FROM FULL_INFO WHERE A1_NAME IN (SELECT A1_NAME FROM M_STAY WHERE A1_NAME NOT IN (SELECT A1_NAME FROM M_STAY WHERE LAST_REPORT<=''',m,''' OR FIRST_REPORT>=''',n,''')','INTERSECT',' SELECT A1_NAME FROM FULL_INFO WHERE TOTAL_REPORTS<',num2str(maxi),' AND TOTAL_REPORTS>=',num2str(mini),');']
                cursor=exec(conn, sql);
                cursor=fetch(cursor);
                data=cursor.data;
                g(i-2000+1)=cell2mat(data(1,2))
                t(i-2000+1)=cell2mat(data(1,1))
            
        end

        figure(1)
        plot(g)
        title(['avg stay of employees having<= ',num2str(maxi),' reports and > ',num2str(mini),'report and stay between ',num2str(exmi),' and ',num2str(exma),' years'])
        xlabel('Years from 2000 to 2013')
        ylabel('Years')
        
        figure(2)
        plot(t)
        title(['no.of of employees during an year having<= ',num2str(maxi),' reports and > ',num2str(mini),' report and stay between ',num2str(exmi),' and ',num2str(exma),' years'])
        xlabel('Years from 2000 to 2013')
        ylabel('No of employees')
        
    case 2
        for i=2000:2013
            
                a=num2str(i);
                
                n=[a,'-','12','-','31']; %generating proper date
                m=[a,'-','01','-','01'];
                %sql=['SELECT AVG((''',n,'''- FIRST_REPORT)/365 :: FLOAT) AS AVG_STAY FROM M_STAY WHERE A1_NAME NOT IN (SELECT A1_NAME FROM M_STAY WHERE LAST_REPORT<=''',m,''' OR FIRST_REPORT>=''',n,''');'];
        
                sql=['SELECT COUNT(*),AVG((''',n,'''-FIRST_REPORT)/365::FLOAT) AS STAY FROM FULL_INFO WHERE A1_NAME IN (SELECT A1_NAME FROM M_STAY WHERE A1_NAME NOT IN (SELECT A1_NAME FROM M_STAY WHERE LAST_REPORT<=''',m,''' OR FIRST_REPORT>=''',n,''')','INTERSECT',' SELECT A1_NAME FROM FULL_INFO WHERE TOTAL_REPORTS<',num2str(maxi),' AND TOTAL_REPORTS>=',num2str(mini),');']
                cursor=exec(conn, sql);
                cursor=fetch(cursor);
                data=cursor.data;
                g(i-2000+1)=cell2mat(data(1,2))
                t(i-2000+1)=cell2mat(data(1,1))
            
        end

        figure(1)
        plot(g)
        title(['avg stay of employees having<= ',num2str(maxi),' reports and > ',num2str(mini),'report'])
        xlabel('Years from 2000 to 2013')
        ylabel('Years')
        
        figure(2)
        plot(t)
        title(['no.of of employees during an year having<= ',num2str(maxi),' reports and > ',num2str(mini),' report'])
        xlabel('Years from 2000 to 2013')
        ylabel('No of employees')
        
end
        
        

