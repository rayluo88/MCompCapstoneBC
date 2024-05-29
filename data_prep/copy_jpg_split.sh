#!/bin/bash

# Set the base directories
base_dir=~/finetune_llava_vindr/dataset
jpg_dir=$base_dir/jpg_images
training_dir=$base_dir/jpg_training
test_dir=$base_dir/jpg_test

# Ensure the training and test directories exist
#mkdir -p $training_dir
#mkdir -p $test_dir

# Read the CSV file and process each line
csv_file=~/data/vindr_mammo/vm1.0.0/breast-level_annotations.csv

tail -n +2 $csv_file | while IFS=, read -r study_id patient_id image_id view modality width height birads density split
do
    # Trim any potential newline characters from the split variable
    split=$(echo $split | tr -d '\r\n')
    echo $split

    case "$split" in
        training)
            dest_dir=$training_dir
            ;;
        test)
            dest_dir=$test_dir
            ;;
        *)
            continue
            ;;
    esac

    # Define the source and destination file paths
    src_file=$jpg_dir/${image_id}.jpg
    dest_file=$dest_dir/${image_id}.jpg

    # Copy the file if it exists
    if [ -f $src_file ]; then
        cp $src_file $dest_file
        echo "Copied $src_file to $dest_file"
    else
        echo "File $src_file does not exist"
    fi
done

echo "Copying process completed."

