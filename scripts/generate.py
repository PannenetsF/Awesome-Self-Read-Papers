import os
import yaml

from prettytable import PrettyTable
import htmltabletomd


MAGICSTART = '213ev f145 dcs21'
MAGICEND = 'saf3 4rvf45 cda 12'

OUTLINE = 'scripts/outline.yaml'
CATS = 'papers'
def load_yaml_from_fn(fn):
    with open(fn, 'r') as f:
        res = yaml.load(f, Loader=yaml.Loader)
    return res

def load_papers_from_root(root):
    papers = {}
    for fn in os.listdir(root):
        fn = os.path.join(root, fn)
        if fn.endswith('.yaml'):
            paper = load_yaml_from_fn(fn)
            if paper is None:
                continue
            if 'section_name' in paper:
                papers[paper['section_name']] = paper['section']
    return papers

def tag_it(term, key):
    if key not in term:
        return ''
    else:
        if isinstance(term[key], list):
            _res = ''
            for t in term[key]:
                _res += f'{MAGICSTART}{t}{MAGICEND} '
        else:
            _res = f'{MAGICSTART}{term[key]}{MAGICEND} '
        return _res

def from_paper_to_row(paper):
    name = paper['name']
    pub = tag_it(paper, 'publisher')
    year = paper['year']
    tags = tag_it(paper, 'tags')
    logic = paper['logic']
    team = tag_it(paper, 'team')
    read = tag_it(paper, 'read')
    return [pub, year, name, tags, team, read, logic]

def from_table_to_markdown(table):
    html = table.get_html_string()
    html = html.replace(MAGICSTART, '<strong><code>')
    html = html.replace(MAGICEND, '</code></strong>')
    html = htmltabletomd.convert_table(html)
    return html

def get_markdown_table_from_sec(paper_list):
    table = PrettyTable(['Publisher', 'Year', 'Name', 'Tags', 'Team', 'Read', 'Logic'])
    for paper in paper_list:
        table.add_row(from_paper_to_row(paper))
    return from_table_to_markdown(table)

def parse_dict_to_markdown(outline, papers):
    readme = ''
    # title 
    readme += '# ' + outline['title'] + '\n\n\n'
    # abs
    readme += outline['abs'] + '\n\n\n'
    for sec in outline['sections']:
        assert sec in papers
        readme += f'## {sec} \n\n'
        readme += get_markdown_table_from_sec(papers[sec])
    return readme


outline = load_yaml_from_fn(OUTLINE)
papers = load_papers_from_root(CATS)
res = parse_dict_to_markdown(outline, papers)
print(res)