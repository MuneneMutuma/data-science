for pip in $(cat ./code/numpy/requirements.txt)
do
    pip install $pip
done