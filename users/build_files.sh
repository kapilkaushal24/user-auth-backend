echo "BUILD START"
python3.12.7 -m pip install -r requirements.txt
python3.12.7 manage.py collectstatic --noiput --clear
echo "BUILD END"