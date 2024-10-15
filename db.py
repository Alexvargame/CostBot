import sqlite3

class BotDBClass:

    def __init__(self,db_file):
        self.conn=sqlite3.connect(db_file)
        self.cursor=self.conn.cursor()

    def user_exists(self,user_id):
        result=self.cursor.execute('select "id" from "users" where "user_id"=?',(user_id,)).fetchone()
        return bool(len(result))

    def get_user_id(self,user_id):

        return self.cursor.execute('select "id" from "users" where "user_id"=?',(user_id,)).fetchone()[0]
    def add_user(self,user_id):
        self.cursor.execute("insert into 'users' ('user_id') values (?)",(user_id,))
        return self.conn.commit()

    def add_record(self,user_id,operation, value):
        self.cursor.execute("insert into 'records' ('users_id','operation','value') values (?,?,?)",
                         (self.get_user_id(user_id),operation=='+',value))
        return self.conn.commit()

    def get_records(self,user_id,within='*'):
        if within == "day":
            result = self.cursor.execute(
                "SELECT * FROM `records` WHERE `users_id` = ? AND `date` BETWEEN datetime('now', 'start of day') AND datetime('now', 'localtime') ORDER BY `date`",
                (self.get_user_id(user_id),))
        elif within == "week":
            result = self.cursor.execute(
                "SELECT * FROM `records` WHERE `users_id` = ? AND `date` BETWEEN datetime('now', '-6 days') AND datetime('now', 'localtime') ORDER BY `date`",
                (self.get_user_id(user_id),))
        elif within == "month":
            result = self.cursor.execute(
                "SELECT * FROM `records` WHERE `users_id` = ? AND `date` BETWEEN datetime('now', 'start of month') AND datetime('now', 'localtime') ORDER BY `date`",
                (self.get_user_id(user_id),))
        else:
            result = self.cursor.execute("SELECT * FROM `records` WHERE `user_id` = ? ORDER BY `date`",
                                         (self.get_user_id(user_id),))

        return result.fetchall()

    def close(self):
        self.connection.close()
