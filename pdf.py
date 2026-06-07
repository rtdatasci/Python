import fitz  # PyMuPDF
import pandas as pd

def extract_tables_from_pdf(input_pdf_path, output_excel_path, pages='1', min_rows=3, min_cols=3):
    """
    Extract tables from specified pages of a PDF using PyMuPDF and save them to an Excel file.
    :param input_pdf_path: Path to input PDF file.
    :param output_excel_path: Path to output Excel file.
    :param pages: Pages to extract from (e.g., '1', '1-3', or '1,3,5').
    :param min_rows: Minimum rows in a table to consider it valid.
    :param min_cols: Minimum columns in a table to consider it valid.
    """
    doc = fitz.open(input_pdf_path)
    all_tables = []
    
    # Extract text from the specified pages
    for page_num in pages.split(','):
        page = doc[int(page_num)-1]  # Convert to 0-based index
        text = page.get_text('text')  # Extract text as plain text
        
        # Split the text into rows by newlines
        rows = text.split('\n')

        # Filter out empty rows
        rows = [row.strip() for row in rows if row.strip()]
        
        # Assuming a table has consistent spacing between columns, we can split based on spaces
        tables = []
        for row in rows:
            columns = row.split()  # Split by whitespace
            if len(columns) >= min_cols:
                tables.append(columns)

        # Filter tables based on minimum rows and columns
        if len(tables) >= min_rows:
            all_tables.append(pd.DataFrame(tables))

    if all_tables:
        # Save to Excel
        with pd.ExcelWriter(output_excel_path, engine='openpyxl') as writer:
            for i, table in enumerate(all_tables):
                table.to_excel(writer, sheet_name=f'Table_{i+1}', index=False)
        print(f"Extracted {len(all_tables)} relevant tables and saved to {output_excel_path}")
    else:
        print("No relevant tables found.")

# Example usage
input_pdf = "input.pdf"  # Path to your PDF
output_excel = "output.xlsx"  # Path to the output Excel file
pages_to_extract = '14'  # Pages to extract from

extract_tables_from_pdf(input_pdf, output_excel, pages=pages_to_extract)


