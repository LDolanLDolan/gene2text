# Complete genetic code dictionary with biological context
CODON_TABLE = {
    # Start codon
    'ATG': {'amino_acid': 'Methionine', 'type': 'start', 'description': 'The universal start codon - where protein synthesis begins'},
    
    # Stop codons
    'TAA': {'amino_acid': 'STOP', 'type': 'stop', 'description': 'Amber stop codon - signals end of protein synthesis'},
    'TAG': {'amino_acid': 'STOP', 'type': 'stop', 'description': 'Ochre stop codon - signals end of protein synthesis'},
    'TGA': {'amino_acid': 'STOP', 'type': 'stop', 'description': 'Opal stop codon - signals end of protein synthesis'},
    
    # Alanine (A)
    'GCT': {'amino_acid': 'Alanine', 'type': 'regular', 'description': 'Small, hydrophobic amino acid - often found in protein cores'},
    'GCC': {'amino_acid': 'Alanine', 'type': 'regular', 'description': 'Small, hydrophobic amino acid - often found in protein cores'},
    'GCA': {'amino_acid': 'Alanine', 'type': 'regular', 'description': 'Small, hydrophobic amino acid - often found in protein cores'},
    'GCG': {'amino_acid': 'Alanine', 'type': 'regular', 'description': 'Small, hydrophobic amino acid - often found in protein cores'},
    
    # Arginine (R)
    'CGT': {'amino_acid': 'Arginine', 'type': 'regular', 'description': 'Positively charged amino acid - important for protein-DNA interactions'},
    'CGC': {'amino_acid': 'Arginine', 'type': 'regular', 'description': 'Positively charged amino acid - important for protein-DNA interactions'},
    'CGA': {'amino_acid': 'Arginine', 'type': 'regular', 'description': 'Positively charged amino acid - important for protein-DNA interactions'},
    'CGG': {'amino_acid': 'Arginine', 'type': 'regular', 'description': 'Positively charged amino acid - important for protein-DNA interactions'},
    'AGA': {'amino_acid': 'Arginine', 'type': 'regular', 'description': 'Positively charged amino acid - important for protein-DNA interactions'},
    'AGG': {'amino_acid': 'Arginine', 'type': 'regular', 'description': 'Positively charged amino acid - important for protein-DNA interactions'},
    
    # Asparagine (N)
    'AAT': {'amino_acid': 'Asparagine', 'type': 'regular', 'description': 'Polar amino acid - often involved in protein folding and stability'},
    'AAC': {'amino_acid': 'Asparagine', 'type': 'regular', 'description': 'Polar amino acid - often involved in protein folding and stability'},
    
    # Aspartic acid (D)
    'GAT': {'amino_acid': 'Aspartic acid', 'type': 'regular', 'description': 'Negatively charged amino acid - important for enzyme active sites'},
    'GAC': {'amino_acid': 'Aspartic acid', 'type': 'regular', 'description': 'Negatively charged amino acid - important for enzyme active sites'},
    
    # Cysteine (C)
    'TGT': {'amino_acid': 'Cysteine', 'type': 'regular', 'description': 'Contains sulfur - can form disulfide bonds for protein structure'},
    'TGC': {'amino_acid': 'Cysteine', 'type': 'regular', 'description': 'Contains sulfur - can form disulfide bonds for protein structure'},
    
    # Glutamic acid (E)
    'GAA': {'amino_acid': 'Glutamic acid', 'type': 'regular', 'description': 'Negatively charged amino acid - common in enzyme active sites'},
    'GAG': {'amino_acid': 'Glutamic acid', 'type': 'regular', 'description': 'Negatively charged amino acid - common in enzyme active sites'},
    
    # Glutamine (Q)
    'CAA': {'amino_acid': 'Glutamine', 'type': 'regular', 'description': 'Polar amino acid - involved in protein-protein interactions'},
    'CAG': {'amino_acid': 'Glutamine', 'type': 'regular', 'description': 'Polar amino acid - involved in protein-protein interactions'},
    
    # Glycine (G)
    'GGT': {'amino_acid': 'Glycine', 'type': 'regular', 'description': 'Smallest amino acid - provides flexibility in protein structure'},
    'GGC': {'amino_acid': 'Glycine', 'type': 'regular', 'description': 'Smallest amino acid - provides flexibility in protein structure'},
    'GGA': {'amino_acid': 'Glycine', 'type': 'regular', 'description': 'Smallest amino acid - provides flexibility in protein structure'},
    'GGG': {'amino_acid': 'Glycine', 'type': 'regular', 'description': 'Smallest amino acid - provides flexibility in protein structure'},
    
    # Histidine (H)
    'CAT': {'amino_acid': 'Histidine', 'type': 'regular', 'description': 'Can be positively charged - often found in enzyme active sites'},
    'CAC': {'amino_acid': 'Histidine', 'type': 'regular', 'description': 'Can be positively charged - often found in enzyme active sites'},
    
    # Isoleucine (I)
    'ATT': {'amino_acid': 'Isoleucine', 'type': 'regular', 'description': 'Hydrophobic amino acid - important for protein core structure'},
    'ATC': {'amino_acid': 'Isoleucine', 'type': 'regular', 'description': 'Hydrophobic amino acid - important for protein core structure'},
    'ATA': {'amino_acid': 'Isoleucine', 'type': 'regular', 'description': 'Hydrophobic amino acid - important for protein core structure'},
    
    # Leucine (L)
    'TTA': {'amino_acid': 'Leucine', 'type': 'regular', 'description': 'Hydrophobic amino acid - very common in proteins'},
    'TTG': {'amino_acid': 'Leucine', 'type': 'regular', 'description': 'Hydrophobic amino acid - very common in proteins'},
    'CTT': {'amino_acid': 'Leucine', 'type': 'regular', 'description': 'Hydrophobic amino acid - very common in proteins'},
    'CTC': {'amino_acid': 'Leucine', 'type': 'regular', 'description': 'Hydrophobic amino acid - very common in proteins'},
    'CTA': {'amino_acid': 'Leucine', 'type': 'regular', 'description': 'Hydrophobic amino acid - very common in proteins'},
    'CTG': {'amino_acid': 'Leucine', 'type': 'regular', 'description': 'Hydrophobic amino acid - very common in proteins'},
    
    # Lysine (K)
    'AAA': {'amino_acid': 'Lysine', 'type': 'regular', 'description': 'Positively charged amino acid - important for DNA binding'},
    'AAG': {'amino_acid': 'Lysine', 'type': 'regular', 'description': 'Positively charged amino acid - important for DNA binding'},
    
    # Phenylalanine (F)
    'TTT': {'amino_acid': 'Phenylalanine', 'type': 'regular', 'description': 'Aromatic, hydrophobic amino acid - important for protein structure'},
    'TTC': {'amino_acid': 'Phenylalanine', 'type': 'regular', 'description': 'Aromatic, hydrophobic amino acid - important for protein structure'},
    
    # Proline (P)
    'CCT': {'amino_acid': 'Proline', 'type': 'regular', 'description': 'Rigid amino acid - creates kinks and turns in protein structure'},
    'CCC': {'amino_acid': 'Proline', 'type': 'regular', 'description': 'Rigid amino acid - creates kinks and turns in protein structure'},
    'CCA': {'amino_acid': 'Proline', 'type': 'regular', 'description': 'Rigid amino acid - creates kinks and turns in protein structure'},
    'CCG': {'amino_acid': 'Proline', 'type': 'regular', 'description': 'Rigid amino acid - creates kinks and turns in protein structure'},
    
    # Serine (S)
    'TCT': {'amino_acid': 'Serine', 'type': 'regular', 'description': 'Polar amino acid - can be phosphorylated for regulation'},
    'TCC': {'amino_acid': 'Serine', 'type': 'regular', 'description': 'Polar amino acid - can be phosphorylated for regulation'},
    'TCA': {'amino_acid': 'Serine', 'type': 'regular', 'description': 'Polar amino acid - can be phosphorylated for regulation'},
    'TCG': {'amino_acid': 'Serine', 'type': 'regular', 'description': 'Polar amino acid - can be phosphorylated for regulation'},
    'AGT': {'amino_acid': 'Serine', 'type': 'regular', 'description': 'Polar amino acid - can be phosphorylated for regulation'},
    'AGC': {'amino_acid': 'Serine', 'type': 'regular', 'description': 'Polar amino acid - can be phosphorylated for regulation'},
    
    # Threonine (T)
    'ACT': {'amino_acid': 'Threonine', 'type': 'regular', 'description': 'Polar amino acid - can be phosphorylated for regulation'},
    'ACC': {'amino_acid': 'Threonine', 'type': 'regular', 'description': 'Polar amino acid - can be phosphorylated for regulation'},
    'ACA': {'amino_acid': 'Threonine', 'type': 'regular', 'description': 'Polar amino acid - can be phosphorylated for regulation'},
    'ACG': {'amino_acid': 'Threonine', 'type': 'regular', 'description': 'Polar amino acid - can be phosphorylated for regulation'},
    
    # Tryptophan (W)
    'TGG': {'amino_acid': 'Tryptophan', 'type': 'regular', 'description': 'Largest amino acid - important for protein folding and fluorescence'},
    
    # Tyrosine (Y)
    'TAT': {'amino_acid': 'Tyrosine', 'type': 'regular', 'description': 'Aromatic amino acid - can be phosphorylated for signaling'},
    'TAC': {'amino_acid': 'Tyrosine', 'type': 'regular', 'description': 'Aromatic amino acid - can be phosphorylated for signaling'},
    
    # Valine (V)
    'GTT': {'amino_acid': 'Valine', 'type': 'regular', 'description': 'Hydrophobic amino acid - common in protein cores'},
    'GTC': {'amino_acid': 'Valine', 'type': 'regular', 'description': 'Hydrophobic amino acid - common in protein cores'},
    'GTA': {'amino_acid': 'Valine', 'type': 'regular', 'description': 'Hydrophobic amino acid - common in protein cores'},
    'GTG': {'amino_acid': 'Valine', 'type': 'regular', 'description': 'Hydrophobic amino acid - common in protein cores'}
}

def clean_sequence(sequence):
    """Clean and validate DNA sequence"""
    # Remove spaces, newlines, and convert to uppercase
    cleaned = sequence.upper().replace(" ", "").replace("\n", "").replace("\t", "")
    
    # Remove any non-DNA characters
    valid_chars = set('ATGC')
    cleaned = ''.join(char for char in cleaned if char in valid_chars)
    
    return cleaned

def translate_dna_to_text(sequence, reading_frame=0, detailed=True):
    """
    Translate DNA sequence to descriptive text
    
    Args:
        sequence (str): DNA sequence
        reading_frame (int): 0, 1, or 2 for different reading frames
        detailed (bool): Whether to include detailed descriptions
    
    Returns:
        str: Formatted explanation of the sequence
    """
    sequence = clean_sequence(sequence)
    
    if len(sequence) == 0:
        return "❌ No valid DNA sequence found. Please enter a sequence with A, T, G, C characters only."
    
    # Adjust for reading frame
    sequence = sequence[reading_frame:]
    
    if len(sequence) < 3:
        return "❌ Sequence too short. Need at least 3 nucleotides to form a codon."
    
    # Split into codons
    codons = [sequence[i:i+3] for i in range(0, len(sequence), 3)]
    
    output = []
    output.append(f"🧬 **DNA Sequence Analysis** (Reading Frame {reading_frame + 1})")
    output.append(f"📊 **Sequence Length:** {len(sequence)} nucleotides ({len(codons)} codons)")
    output.append("")
    
    protein_sequence = []
    
    for i, codon in enumerate(codons):
        if len(codon) == 3:
            codon_info = CODON_TABLE.get(codon)
            
            if codon_info:
                amino_acid = codon_info['amino_acid']
                codon_type = codon_info['type']
                description = codon_info['description']
                
                # Add to protein sequence
                if amino_acid == 'STOP':
                    protein_sequence.append('*')
                elif amino_acid == 'Methionine':
                    protein_sequence.append('M')
                else:
                    protein_sequence.append(amino_acid[0])
                
                # Format output based on codon type
                if codon_type == 'start':
                    output.append(f"🚀 **Codon {i+1}: {codon}** → {amino_acid}")
                elif codon_type == 'stop':
                    output.append(f"🛑 **Codon {i+1}: {codon}** → {amino_acid}")
                else:
                    output.append(f"🔤 **Codon {i+1}: {codon}** → {amino_acid}")
                
                if detailed:
                    output.append(f"   💡 {description}")
                output.append("")
            else:
                output.append(f"❓ **Codon {i+1}: {codon}** → Unknown codon")
                output.append("")
        else:
            output.append(f"⚠️ **Incomplete codon: {codon}** (only {len(codon)} nucleotides)")
            output.append("")
    
    # Add protein sequence summary
    if protein_sequence:
        protein_str = ''.join(protein_sequence)
        output.append("🧪 **Resulting Protein Sequence:**")
        output.append(f"`{protein_str}`")
        output.append("")
        
        # Count amino acids
        start_codons = sum(1 for codon in codons if len(codon) == 3 and CODON_TABLE.get(codon, {}).get('type') == 'start')
        stop_codons = sum(1 for codon in codons if len(codon) == 3 and CODON_TABLE.get(codon, {}).get('type') == 'stop')
        
        output.append(f"📈 **Summary:** {start_codons} start codon(s), {stop_codons} stop codon(s)")
    
    return "\n".join(output)

def get_example_sequences():
    """Return example DNA sequences for testing"""
    return {
        "Basic Example": "ATG GCT TAA",
        "Insulin Gene (partial)": "ATG GCC CTG TGG ATG CGC CTC CTG CCC CTG CTG GCG CTG CTG GCC CTG TGG GGG ACC TCG TCG",
        "Beta-globin (partial)": "ATG GTG CAC CTG ACT CCT GAG GAG AAG TCT",
        "Green Fluorescent Protein (partial)": "ATG AGC AAG GGC GAG GAG CTG TTC ACC GGG GTG GTG CCC ATC CTG GTG GAG CTG"
    }