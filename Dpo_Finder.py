#!/usr/bin/env python

from Bio.Blast.Applications import NcbiblastpCommandline
import argparse


def blastp(query_seq, db_name):
    # 创建 NcbiblastpCommandline 对象，调用本地版的 blastp 命令
    cline = NcbiblastpCommandline(query=args.input, db=db_name, evalue=0.01, outfmt='"6 qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore"')
    # 运行blastp
    stdout, stderr = cline()
    return stdout


if __name__ == '__main__':
    # 定义命令行参数
    parser = argparse.ArgumentParser(description='Perform BLASTP search with custom database')
    parser.add_argument('-i', '--input', help='Input query sequence file in FASTA format',
                        required=True)
    parser.add_argument('-d', '--database', help='Name of the BLASTP database to be searched',
                        required=True)
    parser.add_argument('-o', '--output', help='Output file for BLASTP best match results in TSV format',
                        required=True)

    # 解析命令行参数
    args = parser.parse_args()

    if args.display_help:
        parser.print_help()
    else:
        # 读取查询序列并运行blastp
        with open(args.input) as f:
            query_seq = f.read()
            blast_output = blastp(query_seq, args.database)

        # 将 blastp 结果写出到指定文件
        with open(args.output, "w") as f:
            f.write("query_id\thit_id\tpident\tlength\tmismatch\tgapopen\tqstart\tqend\tsstart\tsend\tevalue\tbitscore\n")
            f.write(blast_output)

        # 如果需要将输出转换为 XML 格式，可以使用以下代码
        # blast_records = NCBIXML.parse(StringIO(blast_output))
        # with open('output.xml', 'w') as output_xml:
        #     output_xml.write(blast_output)
