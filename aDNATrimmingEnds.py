from __future__ import with_statement
from getopt import getopt, GetoptError
from Bio import SeqIO
from Bio.SeqIO.QualityIO import FastqGeneralIterator
from sys import argv,stderr, stdin, exit, stdout
import resource

def trimEnds_fastq(seq_infile, outfile):
	'''
	'''
	outRec=[]
	handle = open(outfile, "w")
	for title, seq, qual in FastqGeneralIterator(open(seq_infile)):
	    try:
	        if seq[0] == "T":
	    	    if seq[1] == "T":
	    		    seq=seq[2:]
	    		    qual=qual[2:]
	    	    else:
	    		    seq=seq[1:]
	    		    qual=qual[1:]
	        if seq[-1] == "A":
	    	    if seq[-2] == "A":
	    		    seq=seq[:-2]
	    		    qual=qual[:-2]
	    	    else:
	    		    seq=seq[:-1]
	    		    qual=qual[:-1]
	        handle.write("@%s\n%s\n+\n%s\n" % (title, seq, qual))
	    except:
	    	print title
	handle.close()

if __name__ == "__main__":
    try:
        opts, args = getopt(argv[1:], "hdm",["help", "debug"])
    except GetoptError, err:
        print str(err)
        print >> stderr, __doc__
        exit(2) 

    for o, a in opts:
        if o in ("-h", "--help"):
            print >> stderr, __doc__
            exit()
        elif o in ("-d", "--debug"):
            debug_flag = True
        else:
            assert False, "unhandled option"

    if len(args) > 3:
        print >> stderr, __doc__
        exit(3)
    seq_infile=args[0]
    outfile=args[1]
    trimEnds_fastq(seq_infile, outfile)
    print resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
