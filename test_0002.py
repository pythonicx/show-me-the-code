#! /usr/bin/env python3
# -*- coding:utf-8 -*-

from test_0001 import *
import pymysql


def conn_db():
    config = {
        'user': 'root',
        'password': 'root',
        'database': 'python'
    }
    conn = pymysql.connect(**config)
    cursor = conn.cursor()
    return conn, cursor


def exe_update(conn, cur, sql):
    print('sql:',sql)
    re = cur.execute(sql)
    conn.commit()
    return re


def exe_query(cur, sql):
    cur.execute(sql)
    re = cur.fetchall()
    return re


def close_db(conn, cur):
    cur.close()
    conn.close()

if __name__ == "__main__":
    genes = gene_activation_code(1)
    conn, cur = conn_db()
    sql = "insert into gene (gene) values('{}')"

    for gene in genes:
        exe_update(conn, cur, sql.format(gene))

    sql = 'select * from gene'
    r = exe_query(cur, sql)
    print('r',len(r))
    close_db(conn, cur)