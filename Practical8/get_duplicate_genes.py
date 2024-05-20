import re

filename="Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
output_file = "duplicate_genes.fa"
with open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa",'r') as content :
    genes=[]
    gene_id=None
    gene_sequence=""
    genes_str = ""
    output_1= False  #read the fasta file
    
    for line in content:
        if line.startswith(">"):
            if output_1==True and gene_id :
                genes.append((gene_id, gene_sequence))
            gene_id=line[1:].split()[0]
            gene_sequence=""
            output_1=False
            if re.search(r'duplication', line):
                output_1=True
                
        else: 
            if output_1==True :
                gene_sequence+=line   #find the duplicated genes and get their sequence
                    

for gene_id, gene_sequence in genes:
    genes_str += ">" + gene_id + "\n" + gene_sequence + "\n"  #rewrite the information of genes


with open(output_file, 'w') as output:
    output.write(genes_str)  #output the file include the requested genes
            
print(output_file)


  
    


