for i in $(cat ./bacteria.list)
do 
	#bucket=$(cat bacteria.bucket)
	zip -r ./bactopia/"$i"/"$i".zip ./bactopia/"$i"/output
done

aws s3api list-buckets --query "Buckets[].Name" >bucket.list

for i in $(cat bacteria.list)
do
	if grep -qw "$i"  bucket.list; then
		aws s3 cp ./bactopia/"$i"/"$i".zip s3://"$i"
	else
		aws s3 mb s3://"$i"
		aws s3 cp ./bactopia/"$i"/"$i".zip s3://"$i"
	fi
done
