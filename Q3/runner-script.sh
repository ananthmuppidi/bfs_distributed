#!/usr/bin/bash
STREAM_JAR=$1       
LOCAL_INP=$2        
HDFS_INP=$3         
HDFS_OUT=$4      

FILES=./

NUM_ITERATIONS=3

HDFS_INP="${HDFS_INP%/}"
HDFS_OUT="${HDFS_OUT%/}"
LOCAL_INP="${LOCAL_INP%/}"
FILES="${FILES%/}"

echo "STREAM_JAR: $STREAM_JAR"
echo "LOCAL_INP: $LOCAL_INP"
echo "HDFS_INP: $HDFS_INP"
echo "HDFS_OUT: $HDFS_OUT"
echo "FILES: $FILES"

HDFS_INTERMEDIATE="${HDFS_INP}/intermediate"

hdfs dfs -rm -r ${HDFS_INP} 
hdfs dfs -rm -r ${HDFS_OUT} 
hdfs dfs -rm -r ${HDFS_INTERMEDIATE}

hdfs dfs -mkdir -p ${HDFS_INP}
hdfs dfs -put ${LOCAL_INP}/* ${HDFS_INP}/

INPUT_FOLDER=${HDFS_INP}
for ((i=1; i<=NUM_ITERATIONS; i++)); do
    OUTPUT_FOLDER=${HDFS_INTERMEDIATE}/iteration_$i
    echo -e "Iteration $i: \033[32m $INPUT_FOLDER, $OUTPUT_FOLDER\033[0m"
    hadoop jar $STREAM_JAR \
        -D mapred.reduce.tasks=3 \
        -input ${INPUT_FOLDER} \
        -output ${OUTPUT_FOLDER} \
        -mapper "mapper.py" \
        -reducer "reducer.py" \
        -file ${FILES}/mapper.py \
        -file ${FILES}/reducer.py 
    INPUT_FOLDER=${OUTPUT_FOLDER}
done


hadoop jar $STREAM_JAR \
        -D mapred.reduce.tasks=3 \
        -input ${HDFS_INTERMEDIATE}/iteration_$NUM_ITERATIONS \
        -output ${HDFS_OUT} \
        -mapper "mapper_stage2.py" \
        -reducer "reducer_stage2.py" \
        -file ${FILES}/mapper_stage2.py \
        -file ${FILES}/reducer_stage2.py 

hdfs dfs -rm -r ${HDFS_INTERMEDIATE}