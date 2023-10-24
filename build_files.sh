echo "BUILD START"
pyhton3.9 -m pip install -r requirements.txt
pyhton3.9 -m manage.py collectstatic --noinput --clear
echo "BUILD END"