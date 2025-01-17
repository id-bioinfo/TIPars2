#!/usr/bin/env python3

import argparse
import os


parser = argparse.ArgumentParser()

parser.add_argument("-insertion", "--insertion", action='store_true', help="insert a set of sequences")
parser.add_argument("-placement", "--placement", action='store_true', help="place a set of sequences without modifying the reference tree")
parser.add_argument("-annotation", "--annotation", action='store_true', help="annotate the tree with Pango lineages or other metadata")
parser.add_argument("-annotation_details", "--annotation_details", action='store_true', help="calculate the statistics for the annotation")
parser.add_argument("-refinement", "--refinement", action='store_true', help="refine the tree by annotation and inconsistent tips re-insertion")
parser.add_argument("-refinement_from_annotation", "--refinement_from_annotation", action='store_true', help="refine the tree by given annotation")
parser.add_argument("-tree_BFS", "--tree_BFS", action='store_true', help="collapse tree to bubbles")
parser.add_argument("-graft_subtrees", "--graft_subtrees", action='store_true', help="graft subtrees to a bigtree")
parser.add_argument("-prune_tips", "--prune_tips", action='store_true', help="prune tips from a tree")

parser.add_argument("-t", "--tree", help = "tree file, in Newick format")
parser.add_argument("-s", "--sequence", help="fasta/vcf file contains aligned taxa sequences")
parser.add_argument("-a", "--ancseq", help="fasta/vcf file contains aligned ancestral sequences")
parser.add_argument("-q", "--query", help="fasta/vcf file contains one or multiple query seqence(s)")
parser.add_argument("-f", "--format", default="fasta", help="one of 'fasta', 'vcf'")
parser.add_argument("-m", "--multiplacement", default="true", help="one of 'true', 'false'")
parser.add_argument("-aa", action="store_true", help="TIPars excpets nucleotides by default, use -aa for protein")
parser.add_argument("-cp", "--checkpoint", default="false", help="checkpoint prefix filename for refinement, only for using fasta format; default no checkpoint")
parser.add_argument("-o", "--output", default="TIPars.output", help="outputfile: a tree (insertion/refinment), jplace (placement), tsv (annotation/annotation_details)")
parser.add_argument("-ps", "--print2screen", default="false", help="one of 'true', 'false'(default)")
parser.add_argument("-T", "--threads", default="8", help="number of threads (default = 8), 0 is using all available threads")

#annotation/refinement
parser.add_argument("-l", "--label", help="Pango lineage or other metadata for tips labels")
parser.add_argument("-fs", "--fscore", default="0", help="minimal f1score required for annotation (default = 0)")
parser.add_argument("-as", "--assignment", help="annotation assignment file")

#annotation_details
parser.add_argument("-ct", "--collapsedTree", default="true", help="output lineage collapsed tree")
parser.add_argument("-lt", "--consistentTree", default="false", help="output tree with consistent label tips only")

#tree BFS
parser.add_argument("-nl", "--exploreTreeNodeLimit", default="2000", help="maximum nodes in a bubble for BFS (default = 2000)")
parser.add_argument("-bl", "--smallBubbleLimit", default="5", help="minimal nodes in a bubble for BFS (default = 5)")
parser.add_argument("-cl", "--smallClusterLimit", default="5", help="minimal nodes in a cluster for annotation (default = 5)")
parser.add_argument("-at", "--isOutputUnAnnotaionTips", default="true", help="set 'true' (default; otherwise 'fasle') to indiacte output all taxa no matter they have not been assigned to any ancestral lineage annotation")

#graft subtrees
parser.add_argument("-st", "--subtrees", help="a tsv file contains the subtree filenames and anchors")
parser.add_argument("-og", "--outgroup", help="outgroup name")

#prune tips
parser.add_argument("-rt", "--retain_tips", help="a file contains tip names in one column that are retained in a tree")

#java
parser.add_argument("-xmx", "--xmx", default="4G", help="Java Xmx setting, e.g.,1G,2G,4G,8G")
parser.add_argument("-xms", "--xms", default="512M", help="Java Xms setting, e.g.,512M,1G,2G,4G")
parser.add_argument("-xss", "--xss", default="1M", help="Java Xss setting, e.g.,512K,1M,2M,4M")
parser.add_argument('-v','--version', action='version', version='F1ALA v2.1.0')

args = parser.parse_args()

exec_dir = os.path.dirname(__file__)
## print(exec_dir)

if args.insertion:
    cmd = "java -jar -Xmx" + args.xmx + " -Xms" + args.xms + " -Xss" + args.xss + " " + exec_dir + "/F1ALA.jar" + " insertion " + \
        args.tree + " " + args.sequence + " " + args.ancseq + " " + args.query + " " + args.format + " " + args.multiplacement + " " + \
        str(args.aa) + " " + args.checkpoint + " " + args.output + " " + args.print2screen + " " + args.threads
        
if args.placement:
    cmd = "java -jar -Xmx" + args.xmx + " -Xms" + args.xms + " -Xss" + args.xss + " " + exec_dir + "/F1ALA.jar" + " placement " + \
        args.tree + " " + args.sequence + " " + args.ancseq + " " + args.query + " " + args.format + " " + args.multiplacement + " " + \
        str(args.aa) + " " + args.output + " " + args.print2screen + " " + args.threads
        
if args.annotation:
    cmd = "java -jar -Xmx" + args.xmx + " -Xms" + args.xms + " -Xss" + args.xss + " " + exec_dir + "/F1ALA.jar" + " annotation " + \
        args.tree + " " + args.label + " " + args.fscore + " " + args.output + " " + args.print2screen + " " + args.threads
        
if args.annotation_details:
    cmd = "java -jar -Xmx" + args.xmx + " " + exec_dir + "/F1ALA.jar" + " annotation_details " + \
        args.tree + " " + args.label + " " + args.assignment + " " + args.collapsedTree + " " + args.consistentTree + " " + \
        args.output + " " + args.print2screen + " " + args.threads
        
if args.refinement:
    cmd = "java -jar -Xmx" + args.xmx + " -Xms" + args.xms + " -Xss" + args.xss + " " + exec_dir + "/F1ALA.jar" + " refinement " + \
        args.tree + " " + args.sequence + " " + args.ancseq + " " + args.label + " " + args.format + " " + \
        str(args.aa) + " " + args.checkpoint + " " + args.output + " " + args.print2screen + " " + args.threads
        
if args.refinement_from_annotation:
    cmd = "java -jar -Xmx" + args.xmx + " -Xms" + args.xms + " -Xss" + args.xss + " " + exec_dir + "/F1ALA.jar" + " refinement_from_annotation " + \
        args.tree + " " + args.sequence + " " + args.ancseq + " " + args.label + " " + args.format + " " + args.assignment + " " + \
        str(args.aa) + " " + args.checkpoint + " " + args.output + " " + args.print2screen + " " + args.threads   

if args.tree_BFS:
    cmd = "java -jar -Xmx" + args.xmx + " -Xms" + args.xms + " -Xss" + args.xss + " " + exec_dir + "/F1ALA.jar" + " tree_BFS " + \
        args.tree + " " + args.label + " " + " " + args.exploreTreeNodeLimit + " " + args.smallBubbleLimit + " " + args.smallClusterLimit + " " + \
        args.isOutputUnAnnotaionTips + " " + args.output + " " + args.print2screen + " " + args.threads

if args.graft_subtrees:
    cmd = "java -jar -Xmx" + args.xmx + " -Xms" + args.xms + " -Xss" + args.xss + " " + exec_dir + "/F1ALA.jar" + " graft_subtrees " + \
        args.tree + " " + args.subtrees + " " + args.outgroup + " " + args.output + " " + args.print2screen + " " + args.threads

if args.prune_tips:
    cmd = "java -jar -Xmx" + args.xmx + " -Xms" + args.xms + " -Xss" + args.xss + " " + exec_dir + "/F1ALA.jar" + " prune_tips " + \
        args.tree + " " + args.retain_tips + " " + args.output + " " + args.print2screen + " " + args.threads

os.system(cmd)
