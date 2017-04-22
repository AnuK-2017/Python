################################
#  Step1: Connect to the database
################################
import sqlite3
# provide the database name, sqlite file will be automatically created
conn = sqlite3.connect('accounts.db')

conn.execute('''CREATE TABLE STOCK_INFO
                (STOCK_DATE DATE PRIMARY KEY,
                OPEN_VAL NUMBER NOT NULL,
                HIGH_VAL NUMBER NOT NULL,
                LOW_VAL NUMBER NOT NULL,
                CLOSE_VAL NUMBER,
                VOLUME NUMBER
                );''')

print("Table created successfully")
# commit and close the connection
conn.commit()
# conn.close()
#################################
# Step2: Insert values into table
#################################
conn.execute('''INSERT INTO STOCK_INFO(STOCK_DATE,OPEN_VAL, HIGH_VAL, LOW_VAL, CLOSE_VAL, VOLUME)
                VALUES('04/21/2017',140.54,141.23,140.00,140.44,17320928);''')

conn.execute('''INSERT INTO STOCK_INFO(STOCK_DATE,OPEN_VAL, HIGH_VAL, LOW_VAL, CLOSE_VAL, VOLUME)
                VALUES('04/20/2017',141.22,	142.92,	141.16,	142.44,	23294040);''')

conn.execute('''INSERT INTO STOCK_INFO(STOCK_DATE,OPEN_VAL, HIGH_VAL, LOW_VAL, CLOSE_VAL, VOLUME)
                VALUES('04/19/2017',140.54,141.23,140.00,140.44,17320928);''')

conn.execute('''INSERT INTO STOCK_INFO(STOCK_DATE,OPEN_VAL, HIGH_VAL, LOW_VAL, CLOSE_VAL, VOLUME)
                VALUES('04/18/2017',141.88,	142,140.45,	140.68,	17302160);''')

# commit and close the connection
conn.commit()
# conn.close()
####################################
# Step3: View the values from table
####################################
val = conn.execute("Select STOCK_DATE,OPEN_VAL, HIGH_VAL,LOW_VAL,CLOSE_VAL,VOLUME FROM STOCK_INFO")
for c in val:
    print("STOCK_DATE:",c[0])
    print("OPEN_VAL:", c[1])
    print("HIGH_VAL:", c[2])
    print("LOW_VAL:", c[3])
    print("CLOSE_VAL:", c[4])
    print("VOLUME:", c[5])
conn.close()
