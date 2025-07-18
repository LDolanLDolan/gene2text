\# 🧬 Gene2Text: Interpretable Codon-by-Codon Describer



\[!\[Live Demo](https://img.shields.io/badge/🚀\_Live\_Demo-Gene2Text-blue?style=for-the-badge)](https://huggingface.co/spaces/LDolan/Gene2Text)

\[!\[Hugging Face Spaces](https://img.shields.io/badge/🤗\_Hugging\_Face-Spaces-yellow?style=for-the-badge)](https://huggingface.co/spaces/LDolan/Gene2Text)

\[!\[GitHub](https://img.shields.io/badge/GitHub-Repository-green?style=for-the-badge\&logo=github)](https://github.com/LDolan/gene2text)

\[!\[Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge\&logo=python)](https://www.python.org/)

\[!\[Gradio](https://img.shields.io/badge/Gradio-Latest-orange?style=for-the-badge)](https://gradio.app/)

\[!\[License: MIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](https://opensource.org/licenses/MIT)



\*\*Transform DNA sequences into readable explanations with AI-powered biological insights!\*\*



> 🎯 \*\*Perfect for students, teachers, researchers, and anyone curious about how DNA codes for life\*\*



\## 🌟 What It Does



Gene2Text takes raw DNA sequences (like `ATGCGTAAA`) and explains each codon in plain English:



```

🚀 Codon 1: ATG → Methionine

&nbsp;  💡 The universal start codon - where protein synthesis begins



🔤 Codon 2: CGT → Arginine  

&nbsp;  💡 Positively charged amino acid - important for protein-DNA interactions



🛑 Codon 3: TAA → STOP

&nbsp;  💡 Amber stop codon - signals end of protein synthesis

```



\## ✨ Key Features



\- 🧬 \*\*Complete Genetic Code\*\*: All 64 codons with biological context

\- 📚 \*\*Educational Descriptions\*\*: Learn what each amino acid does

\- 🔄 \*\*Multiple Reading Frames\*\*: Analyze DNA in all 3 possible reading frames

\- 🧪 \*\*Real Examples\*\*: Pre-loaded sequences from insulin, hemoglobin, and GFP

\- 🎨 \*\*Clean Interface\*\*: Simple, educational design perfect for classrooms

\- ⚡ \*\*Error Handling\*\*: Automatically cleans and validates input sequences

\- 📱 \*\*Mobile Friendly\*\*: Works on any device



\## 🚀 Try It Now!



\*\*👉 \[Launch Gene2Text](https://huggingface.co/spaces/LDolan/Gene2Text) 👈\*\*



\## 🎓 Perfect For



| User Type | Use Case |

|-----------|----------|

| 🎓 \*\*Students\*\* | Learning molecular biology and genetics |

| 👩‍🏫 \*\*Teachers\*\* | Explaining the genetic code in classrooms |

| 🔬 \*\*Researchers\*\* | Quickly interpreting DNA sequences |

| 💻 \*\*Bioinformatics Beginners\*\* | Understanding sequence analysis |

| 🤔 \*\*Curious Minds\*\* | Discovering how DNA codes for proteins |



\## 📖 How to Use



1\. \*\*Enter a DNA sequence\*\* or select an example

2\. \*\*Choose a reading frame\*\* (0, 1, or 2)

3\. \*\*Toggle detailed descriptions\*\* for more biological context

4\. \*\*Click "Analyze Sequence"\*\* to see the results!



\### Example Sequences Included



\- \*\*Basic Example\*\*: `ATG GCT TAA` (start, alanine, stop)

\- \*\*Insulin Gene\*\*: Partial sequence from human insulin

\- \*\*Beta-globin\*\*: From hemoglobin protein  

\- \*\*Green Fluorescent Protein\*\*: From jellyfish GFP



\## 🛠️ Technology Stack



\- \*\*Frontend\*\*: \[Gradio](https://gradio.app/) - Modern web interface

\- \*\*Backend\*\*: Pure Python with complete genetic code

\- \*\*Data\*\*: Standard genetic code table with biological annotations

\- \*\*Deployment\*\*: \[Hugging Face Spaces](https://huggingface.co/spaces)

\- \*\*Version Control\*\*: Git \& GitHub



\## 🏗️ Project Structure



```

gene2text/

├── app.py              # Main Gradio interface

├── codon\_table.py      # Complete genetic code + translation logic

├── requirements.txt    # Python dependencies

└── README.md          # This file

```



\## 🧬 The Science Behind It



\### Central Dogma: DNA → RNA → Protein



1\. \*\*DNA\*\* stores genetic information in 4-letter code (A, T, G, C)

2\. \*\*Codons\*\* are 3-letter "words" that specify amino acids

3\. \*\*Proteins\*\* are built from chains of amino acids

4\. \*\*Reading Frames\*\* matter - shifting by 1 nucleotide changes everything!



\### Special Codons



\- 🚀 \*\*Start Codon (ATG)\*\*: Methionine - where translation begins

\- 🛑 \*\*Stop Codons (TAA, TAG, TGA)\*\*: Signal end of protein

\- 🔤 \*\*Regular Codons\*\*: 61 codons coding for 20 amino acids



\## 🚀 Run Locally



```bash

\# Clone the repository

git clone https://github.com/LDolan/gene2text.git

cd gene2text



\# Install dependencies

pip install -r requirements.txt



\# Run the app

python app.py

```



Then open `http://localhost:7860` in your browser.



\## 🎨 Customization Ideas



Want to extend Gene2Text? Here are some ideas:



\- 🔄 \*\*Reverse translation\*\*: Protein sequence → possible DNA sequences

\- 📊 \*\*Codon usage bias\*\*: Show organism-specific preferences  

\- 🧪 \*\*Mutation analysis\*\*: Compare wild-type vs mutant sequences

\- 📈 \*\*Visualization\*\*: Generate codon wheel or amino acid property charts

\- 🌍 \*\*Multiple organisms\*\*: Support mitochondrial or bacterial codes



\## 📚 Educational Applications



\### In the Classroom

\- \*\*Introductory Biology\*\*: Demonstrate genetic code basics

\- \*\*Molecular Biology\*\*: Explore translation mechanisms

\- \*\*Bioinformatics\*\*: Learn sequence analysis fundamentals

\- \*\*Genetics\*\*: Understand mutation effects



\### For Self-Learning

\- Experiment with real gene sequences

\- Compare sequences from different organisms

\- Understand how mutations affect proteins

\- Learn amino acid properties and functions



\## 🔬 Real-World Applications



Understanding DNA sequences is crucial for:



\- \*\*Medical Genetics\*\*: Diagnosing genetic diseases

\- \*\*Drug Development\*\*: Designing protein-based therapeutics

\- \*\*Biotechnology\*\*: Engineering proteins for industry

\- \*\*Evolution\*\*: Comparing species and tracking changes

\- \*\*Forensics\*\*: DNA fingerprinting and identification



\## 🤝 Contributing



Contributions welcome! Feel free to:



\- 🐛 Report bugs or issues

\- 💡 Suggest new features

\- 📚 Add new example sequences

\- 🎨 Improve the user interface

\- 📖 Enhance documentation



\## 📄 License



This project is licensed under the MIT License - see the \[LICENSE](LICENSE) file for details.



\## 🙏 Acknowledgments



\- Built with \[Gradio](https://gradio.app) for the amazing web interface framework

\- Deployed on \[Hugging Face Spaces](https://huggingface.co/spaces) for free hosting

\- Inspired by the need for accessible bioinformatics education

\- Genetic code based on the universal standard genetic code



\## 📞 Contact \& Support



\- 🌐 \*\*Live Demo\*\*: \[Gene2Text on Hugging Face](https://huggingface.co/spaces/LDolan/Gene2Text)

\- 📧 \*\*GitHub Issues\*\*: \[Report bugs or request features](https://github.com/LDolan/gene2text/issues)

\- 💬 \*\*Discussions\*\*: \[Join the conversation](https://github.com/LDolan/gene2text/discussions)



---



\*\*Made with ❤️ for biology education\*\* | Helping make molecular biology accessible to everyone!



!\[Gene2Text Demo](https://via.placeholder.com/800x400/1f2937/white?text=🧬+Gene2Text+Demo+🧬)

