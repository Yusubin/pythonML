import pymysql

def update(vo):
    try:
        con = pymysql.connect(
            host='database-1.cgind9azzzrj.ap-northeast-2.rds.amazonaws.com',
            port=3306,
            user='root',
            password='himedia00-=',
            db='shop2',
            charset='utf8'
        )
        cur = con.cursor();

        sql = "update servicecenter set service_cate = %s where service_idx= %s"

        result=cur.execute(sql,vo)
        con.commit()
        con.close()
        print('전송결과>',result)
    except Exception as e:
        print("db연결중 에러발생")
        print("에러 정보", e)
def read(service_idx):
    try:
        con = pymysql.connect(
            host='database-1.cgind9azzzrj.ap-northeast-2.rds.amazonaws.com',
            port=3306,
            user='root',
            password='himedia00-=',
            db='shop2',
            charset='utf8'
        )
        cur = con.cursor();
   # and service_cate IS NULL
        sql = "select * from servicecenter where service_idx = %s "

        result=cur.execute(sql,service_idx)
        con.commit()
        con.close()
        print('전송결과>',service_idx)
        if(result==1):
            one = cur.fetchone()
            print(one)
            return one
        else :
            one =None
            return one
        conn.close()
    except Exception as e:
        print("db연결중 에러발생")
        print("에러 정보", e)

def readAll():
    try:
        conn = pymysql.connect(
            host='database-1.cgind9azzzrj.ap-northeast-2.rds.amazonaws.com',
            port=3306,
            user='root',
            password='himedia00-=',
            db='shop2',
            charset='utf8'
        )

        print('1. 연결 성공!!', conn.host_info)

        # 연결된 통로(stream)을 통해, SQL문을 보내보자.
        # 2. 연결된 통로를 지정(접근할 수 잇는) 커서 객체를 흭득
        cur = conn.cursor()

        # 3. sql문을 보내보자 where service_cate IS NULL and service_idx_re = 0
        sql = 'select service_idx from servicecenter where service_cate IS NULL'
        # 커서로 sql문을 보냄.
        result = cur.execute(sql)
        # read인 경우, 커서로 연결통로(스트림)에 검색결과를 꺼내주어야 한다
        row = cur.fetchall() #row하나만 꺼내
        return row
        print(row)
        print('sql문 전송 결과>', result)
        conn.close()
    except Exception as e:
        print("db 연결 중 에러발생!!")
        print('에러정보>> ', e)



def readAll2():
    try:
        conn = pymysql.connect(
            host='database-1.cgind9azzzrj.ap-northeast-2.rds.amazonaws.com',
            port=3306,
            user='root',
            password='himedia00-=',
            db='shop2',
            charset='utf8'
        )

        print('1. 연결 성공!!', conn.host_info)

        # 연결된 통로(stream)을 통해, SQL문을 보내보자.
        # 2. 연결된 통로를 지정(접근할 수 잇는) 커서 객체를 흭득
        cur = conn.cursor()

        # 3. sql문을 보내보자 where service_cate IS NULL and service_idx_re = 0
        sql = 'select * from servicecenter'
        # 커서로 sql문을 보냄.
        result = cur.execute(sql)
        # read인 경우, 커서로 연결통로(스트림)에 검색결과를 꺼내주어야 한다
        row = cur.fetchall() #row하나만 꺼내
        return row
        print(row)
        print('sql문 전송 결과>', result)
        conn.close()
    except Exception as e:
        print("db 연결 중 에러발생!!")
        print('에러정보>> ', e)



