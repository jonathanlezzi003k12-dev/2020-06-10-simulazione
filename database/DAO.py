from database.DB_connect import  DBConnect
from model.attori import Attori


class DAO:

    @staticmethod
    def getAttori():
        conn= DBConnect.get_connection()



        result=[]


        cursor=conn.cursor(dictionary=True)
        query="SELECT * FROM actors"
        cursor.execute(query)

        for row in cursor:
            result.append(Attori(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getGeneri():
        conn= DBConnect.get_connection()



        result=[]


        cursor=conn.cursor(dictionary=True)
        query="""select distinct (mg.genre) as genere
                from movies_genres mg """
        cursor.execute(query)

        for row in cursor:
            result.append(row["genere"])
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAttoriByGender(idMapAttori,genere):
        conn= DBConnect.get_connection()



        result=[]


        cursor=conn.cursor(dictionary=True)
        query="""select distinct (mr.actor_id)
                from movies_genres mg ,(select *
	            from movies m,roles r
	            where m.id=r.movie_id)as mr
                where mg.movie_id=mr.movie_id
                and mg.genre=%s """
        cursor.execute(query,(genere,))

        for row in cursor:
            result.append(idMapAttori[row["actor_id"]])
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getArchiPesati(imap,genere):
        conn= DBConnect.get_connection()



        result=[]


        cursor=conn.cursor(dictionary=True)
        query="""select r.actor_id as act1,r1.actor_id as act2 , count(DISTINCT r.movie_id) peso
                from roles r, roles r1
                where r.movie_id=r1.movie_id
                and r.movie_id in (select movie_id
                from movies m , movies_genres mg 
                where m.id=mg.movie_id 
                and mg.genre=%s)
                and r.actor_id<r1.actor_id
                group by r.actor_id,r1.actor_id """
        cursor.execute(query,(genere,))

        for row in cursor:
            result.append((imap[row["act1"]],imap[row["act2"]],row["peso"]))
        cursor.close()
        conn.close()
        return result



if __name__=='__main__':
    print(DAO.getGeneri())
    print(type(DAO.getGeneri()))


