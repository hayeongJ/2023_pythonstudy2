from pandas import DataFrame

emp_list = [{"empno":100, "name":"이도", "job_id":"CEO"},
            {"empno":210, "name":"마루치", "job_id":"IT_PROG"},
            {"empno":121, "name":"홍길동", "job_id":"Sales"},
            {"empno":227, "name":"일지매", "job_id":"IT_PROG"},
            {"empno":236, "name":"아수라", "job_id":"Analysis"},
            {"empno":255, "name":"마이클", "job_id":"Sales"},
            {"empno":270, "name":"어두일미", "job_id":"Analysis"},
            {"empno":282, "name":"을불", "job_id":"IT_PROG"}]

df = DataFrame(emp_list)
print(df)
print('-'*50)

group_job = df.groupby('job_id')
print(group_job.groups)
print('-'*50)

# 구체적 자원을 표현하기 위해서는 반복문 사용
for job, group in group_job:
    print(job + ":" + str(len(group)))
    print(group)
    print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
print('-'*50)

# IT_PROG 만 출력하자
for job, group in group_job:
    if(job == 'IT_PROG'):
        print(job + ":" + str(len(group)))
        print(group)
        break;
print('-'*50)

# cnt_df = DataFrame({'count' : group_job.size()})
cnt_df = DataFrame({'count' : group_job.size()}).reset_index()
print(cnt_df)
print('-'*50)

# 중복된 내용
emp_list2 = [{"empno":100, "name":"이도", "job_id":"CEO"},
            {"empno":210, "name":"마루치", "job_id":"IT_PROG"},
            {"empno":121, "name":"홍길동", "job_id":"Sales"},
            {"empno":227, "name":"일지매", "job_id":"IT_PROG"},
            {"empno":236, "name":"아수라", "job_id":"Analysis"},
            {"empno":255, "name":"마이클", "job_id":"Sales"},
            {"empno":270, "name":"어두일미", "job_id":"Analysis"},
            {"empno":282, "name":"을불", "job_id":"IT_PROG"},
            {"empno":236, "name":"아수라", "job_id":"Analysis"},
            {"empno":255, "name":"마이클", "job_id":"Sales"},
            {"empno":270, "name":"어두일미", "job_id":"Analysis"},
            {"empno":282, "name":"을불", "job_id":"IT_PROG"}]

df = DataFrame(emp_list2)
print(df)
print('-'*50)

# 중복된 행 (행 전체가 똑같은 데이터) 들을 찾아서 삭제하기
res = df.duplicated();
print(res)

res2 = df.drop_duplicates()
print(res2)
print('-'*50)

# 이름이 같은 데이터가 있는지 확인
res3 = df.duplicated(['name'])
print(res3)
print('-'*50)

res4 = df.drop_duplicates(['name'])
print(res4)
print("-"*50)