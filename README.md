# Browser Use Agent Project

Python automation combining AI-driven browser control with PDF table extraction.

## Features

- **Browser Automation**: LLM-powered agents for web tasks (email composition, navigation) using [browser-use](https://github.com/browser-use/browser-use)
- **PDF Processing**: Extract tables from PDFs to Excel with configurable page ranges and filtering

## Setup

```bash
cd browser_use
python -m venv .venv && .venv\Scripts\activate
pip install -r requirements.txt
```

Configure `.env`:
```env
OLLAMA_BASE_URL=http://localhost:11434
BROWSER_USE_API_KEY=your_api_key_here
```

## Usage

### Browser Automation ([`main.py`](main.py))

Edit the `task` parameter to customize agent behavior:

```python
agent = Agent(
    task="Compose a test email with message hi and subject line test and send to jjcamper74@gmail.com",
    llm=ChatOllama(model="deepseek-r1:latest", num_ctx=32000),
    browser=browser,
)
await agent.run()
```

### PDF Extraction ([`pdf.py`](pdf.py))

```python
extract_tables_from_pdf(
    input_pdf="input.pdf",
    output_excel="output.xlsx",
    pages='14',
    min_rows=3,
    min_cols=3
)
```

## Configuration

**Browser path**: Set in [`main.py`](main.py)

| OS | Path |
| --- | --- |
| Windows | `C:\Program Files\Google\Chrome\Application\chrome.exe` |
| macOS | `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome` |

**LLM**: Configure model in [`ChatOllama`](https://python.langchain.com/v0.1/docs/integrations/llms/ollama/) constructor (`model`, `num_ctx`).

## Modules

| File | Purpose |
| --- | --- |
| [`main.py`](main.py) | Browser automation agent |
| [`pdf.py`](pdf.py) | PDF table extraction utility |

**Dependencies**: See [`requirements.txt`](requirements.txt).

## Troubleshooting

- **Browser fails**: Verify Chrome path, check API key in `.env`
- **PDF issues**: Ensure PyMuPDF installed, PDF not password-protected
- **Ollama errors**: Run `curl http://localhost:11434/api/tags` to verify connection

---

**License**: MIT
