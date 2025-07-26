#!/usr/bin/python3

TERM_DEFINITION_SEP = 'xdexdexde'
ROW_SEP = ';;;;;'

def parse_and_save_markdown(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    rows = content.strip().split(ROW_SEP)

    with open(output_file, 'w', encoding='utf-8') as md:
        for idx, row in enumerate(rows, 1):
            if "xdexdexde" in row:
                question, answer = row.split(TERM_DEFINITION_SEP, 1)
                question = question.strip()
                answer = answer.strip()
                md.write(f"### Q{idx}: {question}\n")
                md.write(f"**A:** {answer}\n\n")

    print(f"Markdown output saved to: {output_file}")


if __name__ == "__main__":
    parse_and_save_markdown("text", "qa_output.md")
