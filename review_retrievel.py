import psycopg2

class ReviewRetrievalModel:
    def __init__(self):
        self.conn = psycopg2.connect(
            host="localhost",
            database="mad",
            user="postgres",
            password="1234"
        )
        self.cursor = self.conn.cursor()

    def get_reviews(self, color, storage_size, rating):
        query = "SELECT * FROM reviews WHERE 1=1"

        if color:
            query += f" AND color='{color}'"

        if storage_size:
            query += f" AND storage_size='{storage_size}'"

        if rating:
            query += f" AND rating>='{rating}'"

        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        reviews = []

        for row in rows:
            review = {
                'id': row[0],
                'title': row[1],
                'text': row[2],
                'color': row[3],
                'storage_size': row[4],
                'rating': row[5]
            }
            reviews.append(review)

        return reviews
