# Scrapiata

Aggregate airports data.

```
virtualenv .env -p py36
source .env/bin/activate
pip install -r requirements.txt
python main.py
cat output.csv | sort > output/output.csv
cat output/output.csv | python check.py | sort
```
