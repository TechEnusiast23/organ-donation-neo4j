from neo4j import GraphDatabase

# Replace with your Aura DB credentials
uri = "neo4j+s://2721e36e.databases.neo4j.io"
user = "f66ca5a4"
password = "gs9qE-X9rHSt7H0SvVBGgBv2gVo9gIp_ztwQH4BucGc"

driver = GraphDatabase.driver(uri, auth=(user, password))

def test_connection():
    with driver.session() as session:
        result = session.run("MATCH (n) RETURN COUNT(n) AS total_nodes")
        for record in result:
            print("Total nodes in database:", record["total_nodes"])

if __name__ == "__main__":
    test_connection()
