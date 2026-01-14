import gradio as gr
from brochure import generate_brochure

def run_brochure(company_name, website_url):
    try:
        return generate_brochure(company_name, website_url)
    except Exception as e:
        return f"Error: {str(e)}"

with gr.Blocks(title="Company Brochure Generator") as demo:
    gr.Markdown("## 📘 AI Company Brochure Generator")
    gr.Markdown(
        "Generate a professional company brochure using public company websites "
        "(best results with official homepages)."
    )

    company = gr.Textbox(
        label="Company Name",
        placeholder="e.g. Hugging Face, Stripe, Notion"
    )

    url = gr.Textbox(
        label="Company Website",
        placeholder="https://huggingface.co"
    )

    generate_btn = gr.Button("Generate Brochure 🚀")

    # 👇 Copy icon appears automatically on hover (Gradio 6.x)
    output = gr.Markdown(label="Generated Brochure")

    generate_btn.click(
        fn=run_brochure,
        inputs=[company, url],
        outputs=output
    )

demo.launch(share=True, inbrowser=True)
