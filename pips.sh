for pip in $(cat ds_pips)
do
	echo $pip
	pip3 install pip
done
