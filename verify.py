from pathlib import Path
import re
root=Path(__file__).resolve().parent
assert (root/"AGENTS.md").read_bytes()==(root/"CLAUDE.md").read_bytes()
text=(root/"README.md").read_text()
for target in re.findall(r"\]\(([^)]+)\)",text):
    if target.startswith(("https:","http:","#")):continue
    assert (root/target).is_file(), target
for name in ["invoice-automation","financial-modeling-saas","ai-agent-harness","data-platform-mcp"]:
    assert "https://github.com/nasoler123/"+name in text
print("Profile links and instruction parity passed")
