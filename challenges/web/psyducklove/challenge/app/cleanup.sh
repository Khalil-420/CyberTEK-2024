while true
do
    echo 'Running cleanup'

    id_list=$(find ./uploads -mindepth 1 -maxdepth 1 -type d -printf "%f\n")

    echo "Cleaning static folder"
    for id in $id_list; do
        rm ./static/imgs/$id*
    done

    echo "Cleaning uploads folder"
    rm -rf ./uploads/*


    echo "Cleaning cache"
    rm -rf ./static/cache/*
    
    echo "----"
    
    sleep 600
done