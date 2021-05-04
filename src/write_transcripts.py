output_filepath = './data/text/'

def write_transcripts(transcript_filename, transcript):
    f = open(output_filepath + transcript_filename, 'w+')
    f.write(transcript)
    f.close()