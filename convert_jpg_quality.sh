function jpg()
{
    if [ $# -ne 2 ]; then
        echo "Usage: convert_quality <quality> <input_file>"
        return 1
    fi

    # Extract arguments
    local INPUT_FILE=$1
    local QUALITY=$2

    # Extract filename without extension
    local BASENAME="${INPUT_FILE%.*}"

    # Extract extension
    local EXTENSION="${INPUT_FILE##*.}"

    # Construct output filename
    local OUTPUT_FILE="${BASENAME}-${QUALITY}.${EXTENSION}"

    # Run the convert command
    gm convert -quality "${QUALITY}%" "$INPUT_FILE" "$OUTPUT_FILE"

    echo "Converted file saved as: $OUTPUT_FILE"
}
