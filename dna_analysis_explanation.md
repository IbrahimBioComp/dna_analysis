# DNA Sequence Analysis in Bioinformatics

This guide will explain each part of the Python code used to analyze DNA sequences. The code performs three main tasks: counting nucleotides, finding the reverse complement, and calculating the GC content of a DNA sequence.

## 1. Counting Nucleotides

The first function, `count_nucleotides`, counts the number of each nucleotide (A, T, C, G) in a DNA sequence.

```python
def count_nucleotides(dna_sequence):
    nucleotide_counts = {
        'A': dna_sequence.count('A'),
        'T': dna_sequence.count('T'),
        'C': dna_sequence.count('C'),
        'G': dna_sequence.count('G')
    }
    return nucleotide_counts
```

### Explanation:
- **Function Definition:** The function `count_nucleotides` takes a single argument `dna_sequence`, which is a string representing the DNA sequence.
- **Counting Nucleotides:** Inside the function, a dictionary called `nucleotide_counts` is created. This dictionary stores the counts of each nucleotide (A, T, C, G) by using the `count` method on the `dna_sequence`.
- **Return Statement:** The function returns the dictionary `nucleotide_counts` containing the counts of each nucleotide.

## 2. Finding the Reverse Complement

The second function, `reverse_complement`, finds the reverse complement of a DNA sequence.

```python
def reverse_complement(dna_sequence):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    reverse_complement_sequence = ''.join([complement[base] for base in reversed(dna_sequence)])
    return reverse_complement_sequence
```

### Explanation:
- **Function Definition:** The function `reverse_complement` takes a single argument `dna_sequence`.
- **Complement Mapping:** A dictionary called `complement` is created to map each nucleotide to its complement (A-T, T-A, C-G, G-C).
- **Reverse Complement Calculation:** The function uses a list comprehension to iterate over the reversed `dna_sequence`. For each nucleotide in the reversed sequence, it finds the complement using the `complement` dictionary and joins them together to form the reverse complement sequence.
- **Return Statement:** The function returns the reverse complement sequence.

## 3. Calculating the GC Content

The third function, `gc_content`, calculates the GC content as a percentage of a DNA sequence.

```python
def gc_content(dna_sequence):
    gc_count = dna_sequence.count('G') + dna_sequence.count('C')
    gc_content_percentage = (gc_count / len(dna_sequence)) * 100
    return gc_content_percentage
```

### Explanation:
- **Function Definition:** The function `gc_content` takes a single argument `dna_sequence`.
- **GC Count:** Inside the function, the variable `gc_count` is calculated by summing the counts of 'G' and 'C' nucleotides in the `dna_sequence`.
- **GC Content Percentage:** The GC content percentage is calculated by dividing the `gc_count` by the total length of the `dna_sequence` and then multiplying by 100 to get the percentage.
- **Return Statement:** The function returns the GC content percentage.

## Example Usage

Here's an example DNA sequence and how the functions are used to analyze it:

```python
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
```

### Explanation:
- **Example DNA Sequence:** The variable `example_dna_sequence` is assigned a string representing a DNA sequence.
- **Function Calls:** The functions `count_nucleotides`, `reverse_complement`, and `gc_content` are called with the `example_dna_sequence` to perform the analysis.
- **Print Results:** The results of the analysis are printed to the console.

You can analyse different DNA sequences to get the counts of each nucleotide, the reverse complement, and the GC content percentage by running the codes above.
