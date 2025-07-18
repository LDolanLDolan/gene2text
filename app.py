import gradio as gr
from codon_table import translate_dna_to_text, get_example_sequences, CODON_TABLE

def process_dna_sequence(sequence, reading_frame, detailed_mode, example_dropdown):
    """Process DNA sequence and return explanation"""
    
    # If user selected an example, use that
    if example_dropdown and example_dropdown != "Choose an example...":
        examples = get_example_sequences()
        if example_dropdown in examples:
            sequence = examples[example_dropdown]
    
    if not sequence or sequence.strip() == "":
        return "Please enter a DNA sequence or select an example."
    
    try:
        result = translate_dna_to_text(sequence, reading_frame, detailed_mode)
        return result
    except Exception as e:
        return f"❌ Error processing sequence: {str(e)}\n\nPlease check your input and try again."

def get_genetic_code_table():
    """Generate a formatted genetic code reference table"""
    output = ["# 🧬 Genetic Code Reference\n"]
    output.append("| Codon | Amino Acid | Type | Description |")
    output.append("|-------|------------|------|-------------|")
    
    # Group by amino acid for better organization
    amino_acid_groups = {}
    for codon, info in CODON_TABLE.items():
        aa = info['amino_acid']
        if aa not in amino_acid_groups:
            amino_acid_groups[aa] = []
        amino_acid_groups[aa].append((codon, info))
    
    # Sort amino acids, with special codons first
    special_order = ['Methionine', 'STOP']
    regular_amino_acids = sorted([aa for aa in amino_acid_groups.keys() if aa not in special_order])
    
    for aa in special_order + regular_amino_acids:
        if aa in amino_acid_groups:
            for codon, info in sorted(amino_acid_groups[aa]):
                icon = "🚀" if info['type'] == 'start' else "🛑" if info['type'] == 'stop' else "🔤"
                output.append(f"| {codon} | {aa} | {icon} | {info['description'][:50]}{'...' if len(info['description']) > 50 else ''} |")
    
    return "\n".join(output)

# Create the Gradio interface
with gr.Blocks(
    title="Gene2Text: DNA Codon Explainer",
    theme=gr.themes.Soft(),
    css="""
    .gradio-container {
        max-width: 1200px !important;
    }
    .output-markdown {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    """
) as app:
    
    gr.Markdown("""
    # 🧬 Gene2Text: Interpretable Codon-by-Codon Describer
    
    **Transform DNA sequences into readable explanations!** This tool takes raw DNA sequences and explains what each three-letter codon codes for, making molecular biology accessible to everyone.
    
    Perfect for:
    - 🎓 **Students** learning molecular biology
    - 👩‍🏫 **Teachers** explaining genetic concepts  
    - 🔬 **Researchers** quickly interpreting sequences
    - 🤔 **Anyone curious** about how DNA codes for proteins
    """)
    
    with gr.Row():
        with gr.Column(scale=2):
            gr.Markdown("## 📝 Input Your DNA Sequence")
            
            # Example dropdown
            example_dropdown = gr.Dropdown(
                choices=["Choose an example..."] + list(get_example_sequences().keys()),
                value="Choose an example...",
                label="📚 Or select an example sequence:",
                info="Choose a pre-loaded example to see how the tool works"
            )
            
            # Main input
            sequence_input = gr.Textbox(
                label="🧬 DNA Sequence",
                placeholder="Enter your DNA sequence here (e.g., ATG GCT TAA)\nSpaces and line breaks will be automatically removed.",
                lines=4,
                info="Enter nucleotides: A, T, G, C only. Other characters will be filtered out."
            )
            
            with gr.Row():
                reading_frame = gr.Radio(
                    choices=[0, 1, 2],
                    value=0,
                    label="📍 Reading Frame",
                    info="Choose which nucleotide to start reading from (0=first, 1=second, 2=third)"
                )
                
                detailed_mode = gr.Checkbox(
                    value=True,
                    label="🔍 Detailed Descriptions",
                    info="Include biological context and amino acid properties"
                )
            
            submit_btn = gr.Button("🔬 Analyze Sequence", variant="primary", size="lg")
        
        with gr.Column(scale=3):
            gr.Markdown("## 📋 Results")
            output_text = gr.Markdown(
                value="Enter a DNA sequence to see the codon-by-codon breakdown here...",
                elem_classes=["output-markdown"]
            )
    
    # Genetic Code Reference (collapsible)
    with gr.Accordion("📖 Genetic Code Reference Table", open=False):
        genetic_code_display = gr.Markdown(get_genetic_code_table())
    
    # Educational content
    with gr.Accordion("💡 How It Works", open=False):
        gr.Markdown("""
        ### The Genetic Code Explained
        
        **DNA → RNA → Protein** is the central dogma of molecular biology:
        
        1. **Codons**: DNA is read in groups of 3 nucleotides called codons
        2. **Translation**: Each codon codes for a specific amino acid (or stop signal)
        3. **Proteins**: Amino acids chain together to form proteins
        4. **Reading Frames**: DNA can be read in 3 different frames, giving different results
        
        **Special Codons:**
        - 🚀 **ATG**: Start codon (Methionine) - where protein synthesis begins
        - 🛑 **TAA, TAG, TGA**: Stop codons - where protein synthesis ends
        
        **Why This Matters:**
        Understanding how DNA codes for proteins helps us comprehend genetics, evolution, 
        disease mechanisms, and biotechnology applications.
        """)
    
    # Event handlers
    submit_btn.click(
        fn=process_dna_sequence,
        inputs=[sequence_input, reading_frame, detailed_mode, example_dropdown],
        outputs=output_text
    )
    
    # Auto-update when example is selected
    example_dropdown.change(
        fn=process_dna_sequence,
        inputs=[sequence_input, reading_frame, detailed_mode, example_dropdown],
        outputs=output_text
    )
    
    # Footer
    gr.Markdown("""
    ---
    **Built with ❤️ for biology education** | Made with [Gradio](https://gradio.app) | 
    Perfect for classrooms, labs, and curious minds everywhere!
    """)

# Launch the app
if __name__ == "__main__":
    app.launch(
        share=True,
        server_name="0.0.0.0",
        server_port=7860,
        show_error=True
    )
