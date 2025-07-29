import pandas as pd

def generate_html_report(csv_file='data/sample_log.csv', html_out='docs/example_report.html'):
    df = pd.read_csv(csv_file)
    html = df.to_html(index=False)
    with open(html_out, 'w') as f:
        f.write("<h2>Network Health Report</h2>")
        f.write(html)

if __name__ == "__main__":
    generate_html_report()
