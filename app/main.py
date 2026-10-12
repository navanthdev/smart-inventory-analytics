from sqlalchemy import create_engine,text
from fastapi import FastAPI
import os
from dotenv import load_dotenv
load_dotenv()
app=FastAPI()
HOST=os.getenv('DB_HOST')
PORT=os.getenv('DB_PORT')
NAME=os.getenv('DB_NAME')
USER=os.getenv('DB_USER')
PASSWORD=os.getenv('DB_PASSWORD')
DATABASE_URL = (
f"mysql+pymysql://{USER}:{PASSWORD}"
f"@{HOST}:{PORT}/{NAME}")
engine=create_engine(DATABASE_URL)

@app.get('/test')
def check_db():
    with engine.connect() as connection:
        if connection:
            return{
                'meassage':'successfully connected'
            }
        return{
            'message':'connection failed'
        }

@app.get('/products')
def get_products():
    with engine.connect() as connection:
        query='select * from transactions limit 10'
        result=connection.execute(text(query)).mappings().all()
        if result:
            return result
        return{
            'message':'error caused'
        }

@app.get('/product_summary')
def get_product_summary():
    with engine.connect() as connection:
        query='select customer_id,stock_code,description,sum(quantity) as total_quantity,sum(revenue) as revenue from transactions where customer_id is not null group by customer_id,stock_code,description order by revenue desc limit 10'
        result=connection.execute(text(query)).mappings().all()
        count=len(result)
        if result:
            return{
                'message':'top 10 products by revenue',
                'product_count':count,
                'result':result,
            }
        return{
            'message':'no data found'
        }

@app.get('/product/{stock_id}')
def get_product(stock_id:str):
    with engine.connect() as connection:
        query='select * from transactions where stock_code=:id'
        values={'id':stock_id}
        result=connection.execute(text(query),values).mappings().first()
        if result:
            return result
        else:
            return{
                'message':'no data found'
            }


@app.get('/product_summary/{stock_id}')
def get_product(stock_id:str):
    with engine.connect() as connection:
        query='select stock_code,description,sum(quantity) as total_quantity,sum(revenue) as total_revenue from transactions where stock_code=:stock_id group by stock_code,description'
        values={'stock_id':stock_id}
        result=connection.execute(text(query),values).mappings().first()
        if result:
            return result
        else:
            return{
                'message':'no data found'
            }

@app.get('/sales_summary')
def get_sales_summary():
    with engine.connect() as connection:
        query='select sum(quantity) as total_quantity,sum(revenue) as total_revenue,count(Distinct invoice_no) as total_invoices from transactions'
        result=connection.execute(text(query)).mappings().first()
        if result:
            return result
        return{
            'message':'data not found'
        }

@app.get('/country_revenue/{country}')
def get_revenue_by_country(country:str):
    with engine.connect() as connection:
        query='select country,sum(revenue) as total_revenue from transactions where country=:country group by country'
        values={
            'country':country
        }
        result=connection.execute(text(query),values).mappings().first()
        if result:
            return result
        return{
            'message':'data not found'
        }

@app.get("/monthly_sales")
def get_monthly_sales():
    with engine.connect() as connection:
        query = """
        SELECT
            DATE_FORMAT(InvoiceDate, '%Y-%m') AS year_month,
            SUM(revenue) AS total_revenue
        FROM transactions
        GROUP BY DATE_FORMAT(InvoiceDate, '%Y-%m')
        ORDER BY year_month
        """

        result = connection.execute(
            text(query)
        ).mappings().all()

        return {
            "monthly_sales": [dict(row) for row in result]
        }

@app.get("/country_summary")
def get_country_summary():
    with engine.connect() as connection:
        query = """
        SELECT
            Country AS country,
            SUM(revenue) AS total_revenue
        FROM transactions
        GROUP BY Country
        ORDER BY total_revenue DESC
        LIMIT 10
        """

        result = connection.execute(
            text(query)
        ).mappings().all()


        return {
            "total_countries": len(result),
            "countries": result
        }


@app.get("/top_customers")
def get_top_customers():
    with engine.connect() as connection:
        query = """
        SELECT
            CustomerID AS customer_id,
            SUM(revenue) AS total_revenue
        FROM transactions
        WHERE CustomerID IS NOT NULL
        GROUP BY CustomerID
        ORDER BY total_revenue DESC
        LIMIT 10
        """

        result = connection.execute(
            text(query)
        ).mappings().all()


        return {
            "total_customers": len(result),
            "customers": result
        }