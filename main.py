from analyzer import IDSAnalyzer
from client import IDSClient

def main():
    analyzer = IDSAnalyzer()
    client = IDSClient("localhost", 8888)

    client.connect_to_server()

    while True:
        data = "Sample network traffic data"
        analysis_result = analyzer.analyze(data)
        print(analysis_result)

    client.close_connection()

if __name__ == "__main__":
    main()

