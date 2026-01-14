import json
from dotenv import load_dotenv
from openai import OpenAI
from scrapper import Website
from prompts import LINK_SYSTEM_PROMPT, BROCHURE_SYSTEM_PROMPT
load_dotenv(override=True)
client = OpenAI()

def select_links(website: Website):
    prompt = "Links:\n" + "\n".join(website.links)

    response = client.chat.completions.create(
        model="gpt-4.1-nano",
        messages=[
            {"role": "system", "content": LINK_SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        response_format={"type": "json_object"}
    )

    return json.loads(response.choices[0].message.content)

def generate_brochure(company_name: str, url: str):
    website = Website(url)
    links = select_links(website)

    full_text = website.get_contents()

    for link in links["links"]:
        full_text += "\n\n" + Website(link["url"]).get_contents()

    full_text = full_text[:20_000]

    response = client.chat.completions.create(
        model="gpt-4.1-nano",
        messages=[
            {"role": "system", "content": BROCHURE_SYSTEM_PROMPT},
            {"role": "user", "content": full_text}
        ]
    )

    return response.choices[0].message.content
