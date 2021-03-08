from flask import Response

def respond(df):
    return Response(
        df.to_csv(),
        mimetype="text/csv",
        headers={"Content-disposition": "attachment; filename=y_test.csv", "Content-Type": "text/csv"})
