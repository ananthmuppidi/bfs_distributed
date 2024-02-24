STREAM_JAR=$1       # Path to the Hadoop Streaming JAR
LOCAL_INP=$2        # Local directory containing input files
HDFS_INP=$3         # HDFS directory to store the initial input files
HDFS_OUT=$4         # HDFS directory to store the final output files
FILES=$5            # Path to mapper and reducer files

# Specify the number of iterations
NUM_ITERATIONS=3

# Normalize input paths to remove trailing slashes (if any)
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

# Create the HDFS input directory and copy local input files to it
hdfs dfs -mkdir -p ${HDFS_INP}
hdfs dfs -put ${LOCAL_INP}/* ${HDFS_INP}/

INPUT_FOLDER=${HDFS_INP}
for ((i=1; i<=NUM_ITERATIONS; i++)); do
    if [ $i -eq $NUM_ITERATIONS ]; then
        OUTPUT_FOLDER=${HDFS_OUT}
    else
        OUTPUT_FOLDER=${HDFS_INTERMEDIATE}/iteration_$i
    fi
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
