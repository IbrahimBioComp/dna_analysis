# DNA sequence analysis in bioinformatics

# Function to count nucleotides in a DNA sequence
def count_nucleotides(dna_sequence):
    nucleotide_counts = {
        'A': dna_sequence.count('A'),
        'T': dna_sequence.count('T'),
        'C': dna_sequence.count('C'),
        'G': dna_sequence.count('G')
    }
    return nucleotide_counts

# Function to find the reverse complement of a DNA sequence
def reverse_complement(dna_sequence):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    reverse_complement_sequence = ''.join([complement[base] for base in reversed(dna_sequence)])
    return reverse_complement_sequence

# Function to calculate the GC content of a DNA sequence
def gc_content(dna_sequence):
    gc_count = dna_sequence.count('G') + dna_sequence.count('C')
    gc_content_percentage = (gc_count / len(dna_sequence)) * 100
    return gc_content_percentage

# Example DNA sequence
example_dna_sequence = "ATGCGATACGCTTGC"

# Perform analysis
nucleotide_counts = count_nucleotides(example_dna_sequence)
reverse_complement_sequence = reverse_complement(example_dna_sequence)
gc_content_percentage = gc_content(example_dna_sequence)

# Print results
print(f"DNA Sequence: {example_dna_sequence}")
print(f"Nucleotide Counts: {nucleotide_counts}")
print(f"Reverse Complement: {reverse_complement_sequence}")
print(f"GC Content: {gc_content_percentage:.2f}%")
